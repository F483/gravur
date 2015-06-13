######
gravur
######

|BuildLink|_ |CoverageLink|_ |LicenseLink|_ |IssuesLink|_


.. |BuildLink| image:: https://travis-ci.org/F483/gravur.svg
.. _BuildLink: https://travis-ci.org/F483/gravur

.. |CoverageLink| image:: https://coveralls.io/repos/F483/gravur/badge.svg
.. _CoverageLink: https://coveralls.io/r/F483/gravur

.. |LicenseLink| image:: https://img.shields.io/badge/license-MIT-blue.svg
.. _LicenseLink: https://raw.githubusercontent.com/F483/gravur/master/LICENSE

.. |IssuesLink| image:: https://img.shields.io/github/issues/F483/gravur.svg
.. _IssuesLink: https://github.com/F483/gravur/issues


Secure censorship resistant bitcoin messaging application.


============
Installation
============

::

  pip install gravur


=============
Basic roadmap
=============

What will be done in which order, the later the more vague.
This will be fleshed out over time.

 - Prerequisites
   - Store data in nulldata output
   - Store data in hash160 output
   - Sign data
   - Verify signature
 - Messages
   - Public broadcast (unencrypted cryptograffiti.info compatible)
   - Private message (encrypted)
   - Blockchain scanner
 - Wallet
   - .. _HD BIP32: https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki
   - .. _Secure SPV Backend: https://en.bitcoin.it/wiki/Thin_Client_Security
   - Electrum compatible
 - OS Distributions with auto updaters
   - Windows
   - Mac
   - Linux

