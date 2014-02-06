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
from __future__ import unicode_literals
from pytz import UTC
from datetime import datetime
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from zope.component.interfaces import IFactory
from zope.interface import implements, implementedBy
from Products.XWFCore.XWFUtils import munge_date
from Products.GSAuditTrail import IAuditEvent, BasicAuditEvent, AuditQuery
from Products.GSAuditTrail.utils import event_id_from_data

SUBSYSTEM = 'gs.group.messages.add'
import logging
log = logging.getLogger(SUBSYSTEM)

UNKNOWN = '0'  # Unknown is always "0"
ADD_EMAIL = '1'


class AddEmailAuditEventFactory(object):
    """A Factory for add-email events."""
    implements(IFactory)

    title = 'GroupServer Add-Email Event Factory'
    description = 'Creates a GroupServer event auditor for add-email events'

    def __call__(self, context, event_id, code, date,
        userInfo, instanceUserInfo, siteInfo, groupInfo,
        instanceDatum='', supplementaryDatum='', subsystem=''):
        """Create an event"""
        assert subsystem == SUBSYSTEM, 'Subsystems do not match'

        if code == ADD_EMAIL:
            event = AddEvent(context, event_id, date, siteInfo,
                             instanceDatum, supplementaryDatum)
        else:
            event = BasicAuditEvent(context, event_id, UNKNOWN, date,
              userInfo, instanceUserInfo, siteInfo, groupInfo,
              instanceDatum, supplementaryDatum, SUBSYSTEM)
        assert event
        return event

    def getInterfaces(self):
        return implementedBy(BasicAuditEvent)


class AddEvent(BasicAuditEvent):
    ''' An audit-trail event representing an email being added to a list.'''
    implements(IAuditEvent)

    def __init__(self, context, id, d, siteInfo, instanceDatum,
                 supplementaryDatum):
        """ Create an event"""
        BasicAuditEvent.__init__(self, context, id, ADD_EMAIL, d, None,
          None, siteInfo, None, instanceDatum, supplementaryDatum, SUBSYSTEM)

    def __unicode__(self):
        retval = 'Email (%s) added to a list (%s) on %s (%s).' %\
            (self.instanceDatum, self.supplementaryDatum,
             self.siteInfo.name, self.siteInfo.id)
        return retval

    def __str__(self):
        retval = unicode(self).encode('ascii', 'ignore')
        return retval

    @property
    def xhtml(self):
        cssClass = 'audit-event gs-group-messages-add-base-%s' % self.code
        retval = '<span class="%s">Added an email (%s) to %s.</span>' % \
          (cssClass, self.instanceDaturm, self.supplementaryDatum)

        retval = '%s (%s)' % \
          (retval, munge_date(self.context, self.date))
        return retval


class AddAuditor(object):
    """An auditor for adding an email.
    """
    def __init__(self, context):
        """Create an auditor."""
        self.context = context

    @Lazy
    def siteInfo(self):
        retval = createObject('groupserver.SiteInfo', self.context)
        return retval

    @Lazy
    def factory(self):
        retval = AddEmailAuditEventFactory()
        return retval

    @Lazy
    def queries(self):
        retval = AuditQuery()
        return retval

    def info(self, code, instanceDatum='', supplementaryDatum=''):
        """Log an info event to the audit trail.
            * Creates an ID for the new event,
            * Writes the instantiated event to the audit-table, and
            * Writes the event to the standard Python log.
        """
        d = datetime.now(UTC)
        eventId = event_id_from_data(self.siteInfo, self.siteInfo,
                                     self.siteInfo, code, instanceDatum,
                                     supplementaryDatum + SUBSYSTEM)

        e = self.factory(self.context, eventId, code, d, None, None,
                         self.siteInfo, None, instanceDatum,
                         supplementaryDatum, SUBSYSTEM)

        self.queries.store(e)
        log.info(e)
        return e
