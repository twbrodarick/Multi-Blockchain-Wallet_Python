{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "import subprocess\n",
    "import json\n",
    "import os\n",
    "from constants import *\n",
    "from bit import wif_to_key, PrivateKeyTestnet\n",
    "from bit.network import NetworkAPI\n",
    "from web3 import Web3\n",
    "from web3.middleware import geth_poa_middleware\n",
    "from eth_account import Account"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "w3 = Web3(Web3.HTTPProvider(\"http://127.0.0.1:8545\"))\n",
    "mnem = os.getenv('MNEMONIC')\n",
    "php = 'php.exe ./hd-wallet-derive/hd-wallet-derive.php'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "def derive_wallets(mnemonic, coin, numderive):\n",
    "    cmd = f'{php} -g --mnemonic={mnem}  --numderive='+str(numderive)+' --coin='+str(coin)+' --format=json'\n",
    "    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)\n",
    "    (output, err) = p.communicate()\n",
    "    p_status = p.wait()\n",
    "    return json.loads(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "coins = {'eth': derive_wallets(mnemonic=mnem, coin=ETH, numderive=3), 'btc-test': derive_wallets(mnemonic=mnem, coin=BTCTEST, numderive=3)}\n",
    "\n",
    "eth_priv_key = coins['eth'][0]['privkey']\n",
    "btctest_priv_key = coins['btc-test'][0]['privkey']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "    \"btc-test\": [\n",
      "        {\n",
      "            \"address\": \"mvUyjXK5HE6oMwqbKcBsXxFuqMyYdd3T6P\",\n",
      "            \"index\": 0,\n",
      "            \"path\": \"m/44'/1'/0'/0/0\",\n",
      "            \"privkey\": \"cT47rTHUVJVMEQgX2GjhYrQbWy3CriRML35PuiWZHKjwThnn7ibp\",\n",
      "            \"pubkey\": \"02753facd488377b85e9cf41d16b614f30391d8a78c1c6e92e0dda36bd7493c4cd\",\n",
      "            \"pubkeyhash\": \"a42a419377dcde836d1e9a4e42e3e595cd076f9b\",\n",
      "            \"xprv\": \"tprv8jijGDxZUNE5Je9xSPatNCdfS1m8fiNwQayXhnefJo2X6RiWGdyNS1hhRQ4nk12S7upiBL1rDJ2HDCxXr2rRMg77GtbiQanVdYBLrPyHfT7\",\n",
      "            \"xpub\": \"tpubDGQmQdzocjukC7BkL3FUmcHn13H4q3ZqytaJzJgxj4puvuyGu2nxcWKZbWfQbwK8TBZwC6ZFmvRQeruezs3WP4TQ5T3uLARq1Pxcn99e7WN\"\n",
      "        },\n",
      "        {\n",
      "            \"address\": \"mzMYtMmoDnowdFVpWV7agRvNioQKDFzt3t\",\n",
      "            \"index\": 1,\n",
      "            \"path\": \"m/44'/1'/0'/0/1\",\n",
      "            \"privkey\": \"cNiFYyuYPxYVEtCjcpbBVAvXHxs9oz9GcLfpryf8jCJo6ZRNKvRH\",\n",
      "            \"pubkey\": \"0355670b82624978de2d88f2a40819a1e8ebee46aec87f3a1efe5d069a62f8b6e8\",\n",
      "            \"pubkeyhash\": \"cea31b1405c26382ae3b31712cb6b7a3341919cf\",\n",
      "            \"xprv\": \"tprv8jijGDxZUNE5K6ZBYd9sYKeSwiK9a3MNnNqwdhBP8w41Eapn4iaW4aGqW5vZDFWT5uea3TmR9ywHrWjpicmMJqbojDGdDJse5K2DMN72FjU\",\n",
      "            \"xpub\": \"tpubDGQmQdzocjukCZaySGpTwjJZWjq5jNYHMgSivDDgZCrQ555Yh7Q6F4thgFCxUSXKgejD9mjUJtndYaMzL9skq8JcPawJvDCh6TeNVPXouoi\"\n",
      "        },\n",
      "        {\n",
      "            \"address\": \"mpAMGqvdXxdc1KCf7o3CU37XoW2e6p5QvD\",\n",
      "            \"index\": 2,\n",
      "            \"path\": \"m/44'/1'/0'/0/2\",\n",
      "            \"privkey\": \"cU82JCCKavgsQB7xGyzCjVcPqDNYQvJn3otQYfyNJrdBhHP9py7R\",\n",
      "            \"pubkey\": \"031cb97d35f878d441371e79b02faa8ad05f06c2279666d1dfb0409144c478ce94\",\n",
      "            \"pubkeyhash\": \"5ed39431714e1e8ede3b422e6bf5264d95582b14\",\n",
      "            \"xprv\": \"tprv8jijGDxZUNE5P1F4nE2T4oNuB5BnRjD4jLP7PyPUwBioXmmLoyHQBhFNn2bp2x6ZQ87QcaQHUgpi7HvXDmCdFzbbWTcEZQeJFiDnPWsL8jq\",\n",
      "            \"xpub\": \"tpubDGQmQdzocjukGUGrfsh3UD31k6hib4PyJdytgVRnMTXCNG27SN6zNBsExAEAP3hzxgYWew6QjjSEym9jANLxsSEQurVxmq8MG6BHZ4MVrBS\"\n",
      "        }\n",
      "    ],\n",
      "    \"eth\": [\n",
      "        {\n",
      "            \"address\": \"0x73024f7Da4d0832757f74cc96c1505Cd0dc8F79A\",\n",
      "            \"index\": 0,\n",
      "            \"path\": \"m/44'/60'/0'/0/0\",\n",
      "            \"privkey\": \"0xa59612407ae28116c0b14973fc18e5d2841224609223462d1ecad3b6c93227a1\",\n",
      "            \"pubkey\": \"02a91a6e39852e0b894fa12cf2e0d85c12a83e7e961f26bd96fe23e9b09b5bce25\",\n",
      "            \"pubkeyhash\": \"a0974977d7274baf33c4dc7134d0b9005da7d780\",\n",
      "            \"xprv\": \"xprvA359ATKe4X4Ap1QQmCrNfqWvzAHk6NaGAg2y4dZc3AQRqoWgQfY8PVW8tsJHNmsSxQtPZmavLR9vZwbZdgWTyQ88oyRdjJxhXiMfw8BNtfB\",\n",
      "            \"xpub\": \"xpub6G4VZxrXttcU2VUssEPP2yTfYC8EVqJ7XtxZs1yDbVwQibqpxCrNwHpck8Mbf1B5YzqskuWaP5NUmAMKhJHS6YJJAJGqeY3RokhZ41sxYmr\"\n",
      "        },\n",
      "        {\n",
      "            \"address\": \"0x800902267C23c788169B9e85e287204ed4b2Cd56\",\n",
      "            \"index\": 1,\n",
      "            \"path\": \"m/44'/60'/0'/0/1\",\n",
      "            \"privkey\": \"0xaa9cd0bab4c68cd589093c0488b337ee8e16184bea333608f318cd1d778aca22\",\n",
      "            \"pubkey\": \"03b756ba3bb91aba93ef3e3bfbb2aec29285312530897490da2a23aef697366100\",\n",
      "            \"pubkeyhash\": \"1414b057b65670d902c2fff6117342fee079c93f\",\n",
      "            \"xprv\": \"xprvA359ATKe4X4ArybBv6ZsGkGBR68KK9XJitKBja6dBwWKDQ3GQT4sauFcmCP2kqL2dKshy81Yi9EcnqkpyZ9aAeidHCS53xsNWG15xpN8GTm\",\n",
      "            \"xpub\": \"xpub6G4VZxrXttcU5Tff286sdtCuy7xoicFA67EnXxWEkH3J6CNQwzP88ha6cVT9T1Q5s9YZaXdxvGDSkrvxYQtC9mDfgKukiSvvFMpfPq2Bnqc\"\n",
      "        },\n",
      "        {\n",
      "            \"address\": \"0xFd00e85F8B88489065D503e29C84dCe60E6Bcef1\",\n",
      "            \"index\": 2,\n",
      "            \"path\": \"m/44'/60'/0'/0/2\",\n",
      "            \"privkey\": \"0x4f0c4422d5e6c5653079606d72a6946b22725a8ba2ea54d9ef6ee08eb030de27\",\n",
      "            \"pubkey\": \"034bd768dffeacf8a6ab41fec085bc63fe440c5e971d7a86cc007b7f1965a67034\",\n",
      "            \"pubkeyhash\": \"14caa464193e13e32b496f875063d2f7725b9cd1\",\n",
      "            \"xprv\": \"xprvA359ATKe4X4AtC1AVQc6bjLbMMV681DBwDeQvDfGPWS3puNThWEF38wKaXBQVwKwaUaJTPeVMvWbSeoXjBCiWB5HXUBTj5fkj5BU7VCi2MF\",\n",
      "            \"xpub\": \"xpub6G4VZxrXttcU6g5dbS96xsHKuPKaXTw3JSa1ic4swqy2hhhcF3YVawFoRp8WDKSLA2PLijKYVxXSfrr6PJMuUR2cEEKZrYF9NDhSnCz4DyQ\"\n",
      "        }\n",
      "    ]\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "print(json.dumps(coins, indent=4, sort_keys=True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "def priv_key_to_account(coin, priv_key):\n",
    "    if coin == ETH:\n",
    "        return Account.privateKeyToAccount(priv_key)\n",
    "    if coin == BTCTEST:\n",
    "        return PrivateKeyTestnet(priv_key)\n",
    "    \n",
    "eth_account = priv_key_to_account(ETH,eth_priv_key)\n",
    "btc_account = priv_key_to_account(BTCTEST,btctest_priv_key)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<eth_account.signers.local.LocalAccount object at 0x000001B13CF4FD88>\n",
      "<PrivateKeyTestnet: mvUyjXK5HE6oMwqbKcBsXxFuqMyYdd3T6P>\n"
     ]
    }
   ],
   "source": [
    "print(eth_account)\n",
    "print(btc_account)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_tx(coin, account, to, amount):\n",
    "    if coin == ETH:\n",
    "        gasEstimate = w3.eth.estimateGas(\n",
    "            {\"from\": account.address, \"to\": to, \"amount\":amount}\n",
    "        )\n",
    "        tx = {\n",
    "            \"from\": account.address,\n",
    "            \"to\": to,\n",
    "            \"value\": amount,\n",
    "            \"gas\":  gasEstimate,\n",
    "            \"gasPrice\": w3.eth.gasPrice,\n",
    "            \"nonce\": w3.eth.getTransactionCount(account.address),\n",
    "            \"chainID\": w3.net.chainID\n",
    "        }\n",
    "        \n",
    "        return tx\n",
    "    \n",
    "    if coin == BTCTEST:\n",
    "        \n",
    "        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTCTEST)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mvUyjXK5HE6oMwqbKcBsXxFuqMyYdd3T6P"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "def send_tx(coin, account, to, amount):\n",
    "    if coin == ETH:\n",
    "        raw_tx = create_tx(coin, account, to, amount)\n",
    "        signed_tx = account.sign_transaction(raw_tx)\n",
    "        \n",
    "        return w3.eth.sendRawTransaction(signed_tx.rawTransaction).hex()\n",
    "    \n",
    "    if coin == BTCTEST:   \n",
    "        raw_tx = create_tx(coin, account, to, amount)\n",
    "        signed_tx = account.sign_transaction(raw_tx)\n",
    "        \n",
    "        return NetworkAPI.broadcast_tx_testnet(signed)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "jupyter": {
     "source_hidden": true
    }
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python PyViz",
   "language": "python",
   "name": "pyviz"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
