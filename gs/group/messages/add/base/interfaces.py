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
from zope.interface.interface import Interface
from zope.schema import ASCIILine, Text
from gs.auth.token import AuthToken


class IGSGroupExists(Interface):
    # TODO: Create a base email-address type

    email = ASCIILine(title='Email Address',
                      description='The email address to check',
                      required=True)

    token = AuthToken(title='Token',
                      description='The authentication token',
                      required=True)


class IGSAddEmail(Interface):
    emailMessage = Text(title='Email Message',
                        description='The email message to add',
                        required=True)

    groupId = ASCIILine(title='Group Identifier',
                        description='The identifier of the group to add the '
                            'message to.',
                        required=True)

    token = AuthToken(title='Token',
                      description='The authentication token',
                      required=True)
