# coding=utf-8
from email.parser import Parser
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.auth.token import log_auth_error
from adder import Adder
from audit import AddAuditor, ADD_EMAIL
from base import ListInfoForm
from interfaces import IGSAddEmail
import base64

class AddEmail(ListInfoForm):
    label = u'Add an email'
    pageTemplateFileName = 'browser/templates/addemail.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(IGSAddEmail, render_context=False)
    
    def __init__(self, context, request):
        ListInfoForm.__init__(self, context, request)

    @form.action(label=u'Add', failure='handle_add_action_failure')
    def handle_add(self, action, data):
        try:
            msg = base64.b64decode(data['emailMessage'])
        except TypeError:
            # wasn't base64 encoded. Try and proceed anyway!
            msg = data['emailMessage']
        
        # Audit
        auditor = AddAuditor(self.context)
        length = '%d bytes' % len(data['emailMessage'])
        auditor.info(ADD_EMAIL, length, data['groupId'])
        # Note the site ID
        adder = Adder(self.context, self.request, self.siteInfo.id, 
                      data['groupId'])
        adder.add(msg)
        self.status = u'Done'

    def handle_add_action_failure(self, action, data, errors):
        log_auth_error(self.context, self.request, errors)
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'
        assert type(self.status) == unicode
