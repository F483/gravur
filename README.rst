######
gravur
######

A simple, secure and feature rich bitcoin wallet with additional blockchain
apps. All data is stored on the blockchain.

Donations: 1Dnpy4qd5XSsiAgwX8EqYbR2DLV2kB1Kha


=====
Goals
=====

 * Simple bitcoin wallet that is easily understandable for novices.
 * Integrated useful blockchain apps (messages, invoices, signing, escrow, ...).
 * Strong security (SPV Wallet that doesn't require trusted third parties).
 * Cross platform (Android, iOS, Windows, Mac, Linux)


========
Features
========

 * A fully featured bitcoin wallet.
 * Identities/Contacts: A signed address alias used to enable additional features.
 * Censorship resistant public broadcast messages (much like tweets).
 * Private encryped messages.
 * Document signatures and proof of existance.
 * Shared wallets (using multisig)
 * Escrow (using multisig).


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
