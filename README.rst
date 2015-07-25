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


=====
Goals
=====

 * Simple bitcoin wallet that is easily understandable for novices.
 * Integrated useful blockchain apps (messages, invoices, signing, escrow, ...).
 * Strong security (SPV Wallet that doesn't require trusted third parties). 
 * Cross platform (Android, iOS, Windows, Mac, Linux)


=====================================
Installation for development (Ubuntu)
=====================================

::

  # install kivy
  sudo add-apt-repository ppa:kivy-team/kivy
  sudo apt-get install python-kivy
  sudo apt-get install python3-kivy

  # download gravur
  git clone https://github.com/F483/gravur && cd gravur

  # setup python 2 virtualenv
  virtualenv -p /usr/bin/python2 --system-site-packages env/py2
  env/py2/bin/python setup.py develop

  # setup python 3 virtualenv
  virtualenv -p /usr/bin/python3 --system-site-packages env/py3
  env/py3/bin/python setup.py develop

  # run gravur with python 2 using the bitcoin testnet
  env/py2/bin/python -m gravur --testnet <TEST_WIF>

  # run gravur with python 3 using the bitcoin testnet
  env/py3/bin/python -m gravur --testnet <TEST_WIF>

  # see Makefile for some convenient shortcuts
