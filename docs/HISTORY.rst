Changelog
=========

2.1.2 (2015-04-23)
------------------

* Fixing the logging of an error

2.1.1 (2015-01-27)
------------------

* Ensuring the content-type is ``text/html`` when returning from
  the ``gs-group-messages-add-email.html`` form

2.1.0 (2015-01-14)
------------------

* Following the ``DuplicateMessageError`` to the
  ``gs.group.list.store`` product
* Naming the ReStructuredText files as such
* Pointing at the new GitHub_ repository

.. _GitHub: https://github.com/groupserver/gs.group.messages.add.base

2.0.3 (2014-06-13)
------------------

* Updating the product dependencies

2.0.2 (2014-02-06)
------------------

* Switching to absolute-import, and Unicode literals

2.0.1 (2012-08-21)
------------------

* Catching duplicate messages, and report it to the user

2.0.0 (2012-08-01)
------------------

* New entry point
* Moved the script to ``gs.group.messages.add.smtp2gs``
* Added documentation

1.0.0 (2012-06-22)
------------------

* Initial version, based on code from
  ``Products.XWFMailingListManager``
