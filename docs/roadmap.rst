#######
Roadmap
#######

What will be done in which order, the later the more vague. This will be
fleshed out over time.


 - Prerequisites

   - Static github page

   - Lighthouse project

   - Store data in nulldata output

   - Store data in hash160 output

   - Sign data

   - Verify signature

 - Messages

   - Public broadcast (unencrypted cryptograffiti.info compatible)

   - Private message (encrypted)

   - Hidden private message (encrypted, no metadata)

   - Blockchain scanner

 - Wallet

   - `HD BIP32 <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`_

   - `Secure SPV Backend <https://en.bitcoin.it/wiki/Thin_Client_Security>`_

   - Electrum compatible

 - OS Distributions with auto updaters

   - Windows

   - Mac

   - Linux

 - Security (research required)

   - Always use Tor

   - Transaction padding for uniform sizes

   - Additional random burn for hash160 data outputs to hide message.

   - `Coinjoin for additional privacy <http://joinmarket.io/>`_.
