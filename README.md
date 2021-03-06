## Dependencies

1. Install PHP on your operating system
2. Clone the hd-wallet-derive tool
3. Install bit Python Bitcoin library
4. Install web3.py Python Ethereum library


## Transacting with Blockchain
* Create a Mnemonic and designate as an environment variable

**BTC-Test transaction**
- <BTCTEST_account = priv_key_to_account(BTCTEST, privkey_BTCTEST)>	
- <send_tx(BTCTEST,BTCTEST_account,'mvUyjXK5HE6oMwqbKcBsXxFuqMyYdd3T6P', 0.000001)>	
- *Account recipient and BTC amount are only examples used for this exercise*


**ETH transaction**
- <ETH_account = priv_key_to_account(ETH, privkey_ETH)>	
- <send_tx(ETH, ETH_account, '0x3217c2f345FB50D5B939E6F6fd264e7d77324644', 5)>	
- *Account recipient and ETH amount are only examples used for this exercise*


## Output
* BTC transactions do not output in terminal but can be run in python to find tx hashs to verify 	 
* ETH tx will output in terminal


### Notes
* Used Kovan network for this exercise, hence the chainID = 42 used in wallet.py	
* See Original Instructions in **Images** folder for directions on transacting on custom blockchain	
* Kovan network was used for simplicity because the first address pulled in derive_wallets function was already funded on Kovan network
