# coding=utf-8
from zope.interface.interface import Interface
from zope.schema import ASCIILine, Text
from gs.auth.token import AuthToken

class IGSGroupExists(Interface):
    # TODO: Create a base email-address type
    email = ASCIILine(title=u'Email Address',
                      description=u'The email address to check',
                      required=True)
    token = AuthToken(title=u'Token',
                      description=u'The authentication token',
                      required=True)

class IGSAddEmail(Interface):
    emailMessage = Text(title=u'Email Message',
                        description=u'The email message to add',
                        required=True)
    groupId = ASCIILine(title=u'Group Identifier',
                        description=u'The identifier of the group to add the '\
                            'message to.',
                        required=True)
    token = AuthToken(title=u'Token',
                      description=u'The authentication token',
                      required=True)
