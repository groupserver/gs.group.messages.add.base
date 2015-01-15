# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2012, 2014, 2015 OnlineGroups.net and Contributors.
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
import codecs
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()
with codecs.open(os.path.join("docs", "HISTORY.rst"),
                 encoding='utf-8') as f:
    long_description += '\n' + f.read()

setup(
    name='gs.group.messages.add.base',
    version=version,
    description="The core code for ading a message to a GroupServer group",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Zope Public License',
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules", ],
    keywords='groupserver, message, post, email, list',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='https://github.com/groupserver/gs.group.member.add.base/',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.group', 'gs.group.messages',
                        'gs.group.messages.add'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'pytz',
        'zope.browserpage',
        'zope.cachedescriptors',
        'zope.component',
        'zope.formlib',
        'zope.interface',
        'zope.schema',
        'zope.tal',
        'zope.tales',
        'Zope2',
        'gs.auth.token',
        'gs.content.form.base',
        'gs.email',
        'gs.group.list.store',
        'gs.group.member.canpost',
        'gs.profile.notify',
        'Products.GSAuditTrail',
        'Products.XWFMailingListManager',  # For the mailing list
        'Products.XWFCore',
    ],
    entry_points={
    },
)
