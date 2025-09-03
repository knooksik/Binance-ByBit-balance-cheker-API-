# Binance & ByBit Balance Checker

**Description:**  
Python script for checking balances on Binance and ByBit. Calculates total balance in USDT, supports the top 50 popular cryptocurrencies, and can be easily extended for additional features.  

**Features:**  
- Check balances on Binance  
- Check balances on ByBit (SPOT + FUND)  
- Supports popular coins  
- Easy configuration via `config.py`  
- Can be extended with Telegram notifications  

---

## Project Structure
balance_checker/
├── balance_checker.py # Main script

├── config.py # API keys configuration

├── requirements.txt # Project dependencies

└── README.md # Instructions


---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/knooksik/Binance-ByBit-balance-cheker-API-
cd Binance-ByBit-balance-cheker-API-
```
    
2. Create a virtual environment (recommended):
```
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```

## Configuration (config.py)
Create config.py in the project root and add your API keys:
```
# Binance API
BINANCE_API_KEY = "your_binance_api_key"
BINANCE_API_SECRET = "your_binance_api_secret"

# ByBit API
BYBIT_API_KEY = "your_bybit_api_key"
BYBIT_API_SECRET = "your_bybit_api_secret"
```
⚠️ Do not share your API keys publicly.

## Usage
Run the script:
```
python balance_checker.py
```
Example output:
```
Binance:       53.76 USDT
ByBit SPOT:    0.00 USDT
ByBit FUND:    0.00 USDT
ByBit TOTAL:   0.00 USDT
GRAND TOTAL:   53.76 USDT
```

## Extension

Add new coins: edit the coin_groups list in balance_checker.py.

Add other exchanges (e.g., OKX): create a new client and balance functions similar to Binance/ByBit.

Telegram notifications: integrate python-telegram-bot for automated price reports.

## Requirements

Python 3.10+ (recommended 3.11–3.13)

requests

python-binance

pybit-unified

Install dependencies:
```
pip install requests python-binance pybit-unified
```

## License

MIT License – free to use and modify.
