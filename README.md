# Multi-Blockchain-Wallet_Python

## Dependencies

1. Install PHP on your operating system
2. Clone the hd-wallet-derive tool.
3. Install bit Python Bitcoin library.
4. Install web3.py Python Ethereum library.

## Transacting with Blockchain 
1. Create a Mnemonic and designate as an environment variable
2. Derive the wallet keys

## Python Shell Commands
1. <python>
2. <from wallet import *>
3. BTC-Test transaction
    * <BTCTEST_account = priv_key_to_account(BTCTEST, privkey_BTCTEST)>
    * <send_tx(BTCTEST,BTCTEST_account,'mvUyjXK5HE6oMwqbKcBsXxFuqMyYdd3T6P', 0.000001)>
      *Account recipient and BTC amount are examples used for this exercise.
  
4. ETH transaction
    * <ETH_account = priv_key_to_account(ETH, privkey_ETH)>
    * <send_tx(ETH, ETH_account, '0x3217c2f345FB50D5B939E6F6fd264e7d77324644', 5)>
      *Account recipient and ETH amount are examples used for this exercise.
