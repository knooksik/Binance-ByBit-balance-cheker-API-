from binance.client import Client
from pybit.unified_trading import HTTP
import tkinter as tk


from config import BINANCE_API_KEY, BINANCE_API_SECRET, BYBIT_API_KEY, BYBIT_API_SECRET, OKX_API_KEY, OKX_API_SECRET, OKX_PASSPHRASE


#  Clients
binance_client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
bybit_client = HTTP(testnet=False, api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET)



#  TOP 50 Coins, as ByBit can proceed only 10 tokens per 1 time
coin_groups = [
    ["USDT", "USDC", "BTC", "ETH", "BNB", "XRP", "SOL", "ADA", "DOGE", "TRX"],
    ["DOT", "MATIC", "AVAX", "WBTC", "LINK", "LTC", "XLM", "SHIB", "TON", "BCH"],
    ["SUI", "ATOM", "DOGE", "NEAR", "ALGO", "ICP", "FTM", "EURO", "PEPE", "ARB"]
]

# --- Binance ---
def get_binance_balance():
    total = 0.0
    try:
        account = binance_client.get_account()
        for a in account['balances']:
            amt = float(a['free'])
            if amt <= 0:
                continue
            sym = a['asset']
            if sym == "USDT":
                total += amt
            else:
                price = float(binance_client.get_symbol_ticker(symbol=f"{sym}USDT")['price'])
                total += amt * price
    except Exception as e:
        print("Binance error:", e)
    return total

# --- ByBit SPOT ---
def get_bybit_spot_balance():
    total = 0.0
    try:
        resp = bybit_client.get_spot_asset_info(accountType="SPOT")
        assets = resp.get('result', {}).get('spot', {}).get('assets', [])
        for a in assets:
            amt = float(a.get('free', 0))
            if amt <= 0:
                continue
            sym = a.get('coin')
            if sym == "USDT":
                total += amt
            else:
                price = float(bybit_client.get_tickers(category="spot", symbol=f"{sym}USDT")['result']['list'][0]['lastPrice'])
                total += amt * price
    except Exception as e:
        print("ByBit SPOT error:", e)
    return total

# --- ByBit FUND ---
def get_bybit_fund_balance(groups):
    total = 0.0
    for group in groups:
        for coin in group:
            try:
                resp = bybit_client.get_coins_balance(accountType="FUND", coin=coin)
                bal = resp.get('result', {}).get('balance', [])
                if not bal:
                    continue
                amt = float(bal[0].get('walletBalance', 0))
                if amt <= 0:
                    continue
                if coin == "USDT":
                    total += amt
                else:
                    price = float(bybit_client.get_tickers(category="spot", symbol=f"{coin}USDT")['result']['list'][0]['lastPrice'])
                    total += amt * price
            except:
                pass
    return total

#GUI
root = tk.Tk()
root.title("Crypto Balance Checker")
root.geometry("450x300")
root.resizable(False,False)

result_text = tk.Text(root, font=("Consolas", 12), height=12, width=50)
result_text.pack(pady=10)

# --- Check all balances ---
def check_balances():
    result_text.delete("1.0", tk.END)
    binance_total = get_binance_balance()
    spot_total = get_bybit_spot_balance()
    fund_total = get_bybit_fund_balance(coin_groups)
    bybit_total = spot_total + fund_total
    grand_total = binance_total + bybit_total

    result_text.insert(tk.END, f"Binance:       {binance_total:.2f} USDT\n")
    result_text.insert(tk.END, f"ByBit SPOT:    {spot_total:.2f} USDT\n")
    result_text.insert(tk.END, f"ByBit FUND:    {fund_total:.2f} USDT\n")
    result_text.insert(tk.END, f"ByBit TOTAL:   {bybit_total:.2f} USDT\n")
    result_text.insert(tk.END, f"GRAND TOTAL:   {grand_total:.2f} USDT\n")

check_button = tk.Button(root, text="CHECK", command=check_balances, font=("Arial", 14), bg="#FF0000", fg="white")
check_button.pack(pady=10)

root.mainloop()
