# -*- coding: utf-8 -*-
############################################################################
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
############################################################################
from __future__ import absolute_import, unicode_literals
from logging import getLogger
log = getLogger('gs.group.messages.add.base.Adder')
from zope.cachedescriptors.property import Lazy
from Products.XWFMailingListManager.utils import MAIL_PARAMETER_NAME


class Adder(object):
    def __init__(self, context, request, siteId, groupId):
        assert context, 'No context'
        self.context = context
        assert request, 'No request'
        self.request = request
        assert siteId, 'No siteId'
        self.siteId = siteId
        assert groupId, 'No groupId'
        self.groupId = groupId

    @Lazy
    def list(self):
        listManager = self.context.ListManager
        assert hasattr(listManager, self.groupId),\
            'No such list "%s"' % self.groupId
        retval = listManager.get_list(self.groupId)
        assert retval
        return retval

    def add(self, message):
         # munge the message into the request. This is priority to remove!
        self.request.form[MAIL_PARAMETER_NAME] = message
        retval = self.list.manage_mailboxer(self.request)
        if not retval:
            m = 'No post ID returned. This might be normal, or it might '\
                'be a problem if the poster did not exist.'
            log.warn(m)
        return retval
