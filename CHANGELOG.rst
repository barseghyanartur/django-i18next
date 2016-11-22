Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: none

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.1.3
-----
2016-11-22

- Code cleanup.
- Fixes in installable demo.

0.1.2
-----
2016-11-20

- Compatibility with Django 1.9 and 1.10.
- Minor improvements and code clean-up.

0.1.1
-----
2015-04-09

- Clean up requirements.
- Announce Django 1.4 support.
- Change status to beta.

0.1
---
2015-04-09

- Initial release.
