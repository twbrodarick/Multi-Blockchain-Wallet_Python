#!/usr/bin/env python
# coding: utf-8

# In[117]:


import subprocess
import json
import os
from constants import *
from bit import wif_to_key, PrivateKeyTestnet
from bit.network import NetworkAPI
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account


# In[118]:


w3 = Web3(Web3.HTTPProvider("https://kovan.infura.io/v3/1fa351728e874efcac3aabd55f70a089"))
mnem = os.getenv('MNEMONIC')
php = 'php.exe ./hd-wallet-derive/hd-wallet-derive.php'


# In[119]:


def derive_wallets(mnemonic, coin, numderive):
    cmd = f'{php} -g --mnemonic={mnem} --numderive='+str(numderive)+' --coin='+str(coin)+' --cols=all --format=jsonpretty'   
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return json.loads(output) 

coins = {'eth':derive_wallets(mnemonic=mnem,coin=ETH,numderive=3),'btc-test': derive_wallets(mnemonic=mnem,coin=BTCTEST,numderive=3)}

privkey_BTCTEST = coins['btc-test'][0]['privkey']
privkey_ETH = coins['eth'][0]['privkey']


# In[120]:


def priv_key_to_account(coin, privkey):
    if coin == ETH:
        return Account.privateKeyToAccount(privkey)
    if coin == BTCTEST:
        return PrivateKeyTestnet(privkey)

ETH_account = priv_key_to_account(ETH, privkey_ETH)
BTCTEST_account = priv_key_to_account(BTCTEST, privkey_BTCTEST)

                                                               


# In[121]:


def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas({"from": account.address, "to": to, "value":amount})
        
        tx = {
        "from": account.address,
        "to": to,
        "value": amount,
        "gas":  gasEstimate,
        "gasPrice": w3.eth.gasPrice,
        "nonce": w3.eth.getTransactionCount(account.address),
        "chainId": 42
        }
        
        return tx
    
    if coin == BTCTEST:
        
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])


# In[122]:


def send_tx(coin, account, to, amount):
    if coin == ETH:
        init_tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(init_tx)
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction).hex()
    
    if coin == BTCTEST:   
        init_tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(init_tx)      
        return NetworkAPI.broadcast_tx_testnet(signed_tx)


# In[123]:


send_tx(BTCTEST,BTCTEST_account,'mvUyjXK5HE6oMwqbKcBsXxFuqMyYdd3T6P', 0.000001)


# ## 

# In[126]:


BTCTEST_account.get_transactions()


# In[127]:


send_tx(ETH, ETH_account, '0x3217c2f345FB50D5B939E6F6fd264e7d77324644', 5)


# In[128]:


w3.eth.getBalance(ETH_account.address)


# In[ ]:





# In[ ]:




