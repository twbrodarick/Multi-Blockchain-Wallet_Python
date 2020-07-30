{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 265,
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
   "execution_count": 266,
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
   "execution_count": 267,
   "metadata": {},
   "outputs": [],
   "source": [
    "def derive_wallets(mnemonic, coin, numderive):\n",
    "    cmd = f'{php} -g --mnemonic={mnem} --numderive='+str(numderive)+' --coin='+str(coin)+' --cols=all --format=jsonpretty'   \n",
    "    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)\n",
    "    (output, err) = p.communicate()\n",
    "    return json.loads(output) \n",
    "\n",
    "coins = {'eth':derive_wallets(mnemonic=mnem,coin=ETH,numderive=3),'btc-test': derive_wallets(mnemonic=mnem,coin=BTCTEST,numderive=3)}\n",
    "\n",
    "privkey_BTCTEST = coins['btc-test'][0]['privkey']\n",
    "privkey_ETH = coins['eth'][0]['privkey']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 268,
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
   "execution_count": 269,
   "metadata": {},
   "outputs": [],
   "source": [
    "def priv_key_to_account(coin, privkey):\n",
    "    if coin == ETH:\n",
    "        return Account.privateKeyToAccount(privkey)\n",
    "    if coin == BTCTEST:\n",
    "        return PrivateKeyTestnet(privkey)\n",
    "\n",
    "ETH_account = priv_key_to_account(ETH, privkey_ETH)\n",
    "BTCTEST_account = priv_key_to_account(BTCTEST, privkey_BTCTEST)\n",
    "\n",
    "                                                               "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_tx(coin, account, to, amount):\n",
    "    if coin == ETH:\n",
    "        gasEstimate = w3.eth.estimateGas({\"from\": account.address, \"to\": to, \"amount\":amount})\n",
    "        \n",
    "        tx = {\n",
    "        \"from\": account.address,\n",
    "        \"to\": to,\n",
    "        \"value\": amount,\n",
    "        \"gas\":  gasEstimate,\n",
    "        \"gasPrice\": w3.eth.gasPrice,\n",
    "        \"nonce\": w3.eth.getTransactionCount(account.address),\n",
    "        \"chainID\": w3.net.chainID\n",
    "        }\n",
    "        \n",
    "        return tx\n",
    "    \n",
    "    if coin == BTCTEST:\n",
    "        \n",
    "        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 271,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'{\"unspents\":[{\"amount\":1000000,\"confirmations\":-1781835,\"script\":\"76a914a42a419377dcde836d1e9a4e42e3e595cd076f9b88ac\",\"txid\":\"183d6bc256c6a77a66ed6625200ffacbf08b80aaa6b18305ff38e3027dfeefb4\",\"txindex\":0,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":20000,\"confirmations\":-1781332,\"script\":\"76a914a42a419377dcde836d1e9a4e42e3e595cd076f9b88ac\",\"txid\":\"bec823537c455bca2435eab66940d4f6e535719f627fe48097f48feaa4d100ad\",\"txindex\":0,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":10000,\"confirmations\":-1781332,\"script\":\"76a914a42a419377dcde836d1e9a4e42e3e595cd076f9b88ac\",\"txid\":\"3c0efd997836e1d5aeedc41f2748a9a86293742a65372065ee9082c12b859c85\",\"txindex\":0,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":10000,\"confirmations\":-1781332,\"script\":\"76a914a42a419377dcde836d1e9a4e42e3e595cd076f9b88ac\",\"txid\":\"047e0f7e96e2e4c65be4a3c30dd05279487e52c2e147bb8c275b34c32469f717\",\"txindex\":0,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":1000,\"confirmations\":-1781076,\"script\":\"76a914a42a419377dcde836d1e9a4e42e3e595cd076f9b88ac\",\"txid\":\"3fd5bf7e36499d4ec4a65e8274f92273165aa0cfeeef197a331b6bb15cc06fca\",\"txindex\":2,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":1000,\"confirmations\":-1781069,\"script\":\"76a914a42a419377dcde836d1e9a4e42e3e595cd076f9b88ac\",\"txid\":\"a87aa337315d2208d3ca714ebd0c40d5e21ef4132a4c774c251eb34238a4831b\",\"txindex\":0,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":149408,\"confirmations\":-1781069,\"script\":\"76a914a42a419377dcde836d1e9a4e42e3e595cd076f9b88ac\",\"txid\":\"ca35927ea1c7980d7ed3214e96a71e5fe3d762a67f68ef6a70db954ec20cafc3\",\"txindex\":1,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false}],\"outputs\":[[\"mvUyjXK5HE6oMwqbKcBsXxFuqMyYdd3T6P\",10000],[\"mvUyjXK5HE6oMwqbKcBsXxFuqMyYdd3T6P\",940784]]}'"
      ]
     },
     "execution_count": 271,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "create_tx(BTCTEST,BTCTEST_account,'mvUyjXK5HE6oMwqbKcBsXxFuqMyYdd3T6P',0.0001)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
   "metadata": {},
   "outputs": [],
   "source": [
    "def send_tx(coin, account, to, amount):\n",
    "    if coin == ETH:\n",
    "        raw_tx = create_tx(coin, account.address, to, amount)\n",
    "        signed_tx = account.sign_transaction(raw_tx)\n",
    "        \n",
    "        return w3.eth.sendRawTransaction(signed_tx.rawTransaction).hex()\n",
    "    \n",
    "    if coin == BTCTEST:   \n",
    "        raw_tx = create_tx(coin, account, to, amount)\n",
    "        signed_tx = account.sign_transaction(raw_tx)\n",
    "        \n",
    "        return NetworkAPI.broadcast_tx_testnet(signed_tx)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 273,
   "metadata": {},
   "outputs": [],
   "source": [
    "send_tx(BTCTEST,BTCTEST_account,'mvUyjXK5HE6oMwqbKcBsXxFuqMyYdd3T6P',0.0001)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 274,
   "metadata": {},
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
