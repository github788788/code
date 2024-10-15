exec(open('util.py').read())

import subprocess

# Path to the Chrome executable
chrome_path = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

# Open a new window
subprocess.run([chrome_path, '--incognito', '--new-window'])








"""
import yfinance as yf
stock = yf.Ticker("MSFT")
hist = stock.history(period="5y")
array = dataframe_to_list2([hist])
pri(array)
"""