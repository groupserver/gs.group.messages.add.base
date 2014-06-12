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
from zope.cachedescriptors.property import Lazy
from gs.content.form.base import SiteForm


class ListInfoForm(SiteForm):
    def __init__(self, context, request):
        SiteForm.__init__(self, context, request)
        self.map = {}

    @Lazy
    def mailingListManager(self):
        assert self.context
        retval = self.context.ListManager
        assert retval
        return retval

    def get_siteId_groupId_for_email(self, emailAddr):
        # TODO: making a nice big cache would be great
        if emailAddr not in self.map:
            try:
                l = self.mailingListManager.get_listFromMailto(emailAddr)
            except AttributeError:
                self.map[emailAddr] = (None, None)
            else:
                self.map[emailAddr] = (l.getProperty('siteId'), l.getId())
        retval = self.map[emailAddr]
        assert len(retval) == 2
        return retval

    def get_site_id(self, emailAddr):
        retval = self.get_siteId_groupId_for_email(emailAddr)[0]
        return retval

    def get_group_id(self, emailAddr):
        retval = self.get_siteId_groupId_for_email(emailAddr)[1]
        return retval
