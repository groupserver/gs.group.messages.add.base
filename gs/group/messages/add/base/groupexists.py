# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import unicode_literals, absolute_import
from json import dumps as to_json
from zope.component import createObject
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.auth.token import log_auth_error
from .base import ListInfoForm
from .interfaces import IGSGroupExists


class GroupExists(ListInfoForm):
    label = 'Check if a group exists'
    pageTemplateFileName = 'browser/templates/groupexists.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(IGSGroupExists, render_context=False)

    def __init__(self, context, request):
        ListInfoForm.__init__(self, context, request)

    def get_url_for_site(self, siteId):
        retval = None
        if siteId:
            s = getattr(self.context.Content, siteId)
            retval = createObject('groupserver.SiteInfo', s).url
        return retval

    @form.action(label='Check', failure='handle_check_action_failure')
    def handle_check(self, action, data):
        emailAddr = data['email']
        siteId = self.get_site_id(emailAddr)
        d = {
            'email': emailAddr,
            'siteId': siteId,
            'groupId': self.get_group_id(emailAddr),
            'siteURL': self.get_url_for_site(siteId),
            }
        self.status = 'Done'
        retval = to_json(d)
        return retval

    def handle_check_action_failure(self, action, data, errors):
        log_auth_error(self.context, self.request, errors)
        if len(errors) == 1:
            self.status = '<p>There is an error:</p>'
        else:
            self.status = '<p>There are errors:</p>'
        assert type(self.status) == unicode
