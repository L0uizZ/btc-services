"""
-------------------------------------------------
# Bitcoin - Blockchain Interaction
-------------------------------------------------
"""
__author__ = "Louis Hinz"
__version__ = "0.0.1"

import pandas as pd
import sys

btc_address = sys.argv[1]
url = 'https://blockchain.info/rawaddr/' + btc_address
wallet = pd.read_json(url, lines=True)
balance = float(wallet.final_balance)/100000000
inbound = float(wallet.total_received)/100000000
outbound = float(wallet.total_sent)/100000000
print("[*| BALANCE:\t\t"+str(balance)+" BTC")
print("[*| RECEIVED:\t\t"+str(inbound)+" BTC")
print("[*| SENT:\t\t"+str(outbound)+" BTC")