from web3 import Web3

binance_testnet_rpc_url = 'https://api.avax-test.network/ext/bc/C/rpc'
web3 = Web3(Web3.HTTPProvider(binance_testnet_rpc_url))
print(f"Is connected: {web3.is_connected()}") 
print(f"gas price: {web3.eth.gas_price} BNB")  # кол-во Wei за единицу газа
print(f"current block number: {web3.eth.block_number}")
print(f"number of current chain is {web3.eth.chain_id}")  # 97

wallet_address = "XXX"  # ваш адрес
checksum_address = Web3.to_checksum_address(wallet_address)
balance = web3.eth.get_balance(checksum_address)
print(f"balance of {wallet_address}={Web3.from_wei(balance, 'ether')} Avax")

