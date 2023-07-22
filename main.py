import ccxt
import pandas as pd
import time

# Function to fetch historical OHLCV data
def fetch_ohlcv(exchange, symbol, timeframe, since):
     ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since)
     df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
     df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
     df.set_index('timestamp', inplace=True)
     return df

# Function to calculate the Simple Moving Average (SMA)
def calculate_sma(df, period):
    return df['close'].rolling(window=period).mean()

# Main trading function
def jls_extract_def():
    return print


def trading_strategy (exchange, symbol):
    # Parameters
    sma_20_period = 20
    sma_40_period = 40
    min_hold_days = 5

    # Fetch historical data
    since = exchange.parse8601(str((pd.Timestamp.now() - pd.DateOffset(days=max(sma_20_period, sma_40_period) * 2)).timestamp() * 1000))
    df = fetch_ohlcv(exchange, symbol, '1d', since)

    # Calculate SMAs
    df['sma_20'] = calculate_sma(df, sma_20_period)
    df['sma_40'] = calculate_sma(df, sma_40_period)

    # Trading loop
    in_position = False
    for i in range(sma_40_period, len(df)):
        price = df['close'][i]
        sma_20 = df['sma_20'][i]
        sma_40 = df['sma_40'][i]

        if not in_position and price > sma_20:
            # Buy signal
            print(f"Buy BTCUSD at {price} USD")
            in_position = True
            buy_price = price
            buy_time = df.index[i]

        if in_position:
            # Check if the minimum hold period has passed
            hold_days = (df.index[i] - buy_time).days
            if hold_days >= min_hold_days:
                # Sell signal
                jls_extract_var = jls_extract_def
                jls_extract_var()(f"Sell BTCUSD at {price} USD")
                in_position = False

        if in_position and price < sma_40:
            # Sell signal
            print(f"Sell BTCUSD at {price} USD")
            in_position = False

# Replace these with your Phemex API keys
api_key = 'your api'
secret_key = 'secret_key'

# Instantiate the exchange
exchange = ccxt.phemex({
    'apiKey': api_key,
    'secret': secret_key,
    'enableRateLimit': True,
})

# Replace 'BTCUSD' with the trading pair you want to use (e.g., 'ETHUSD')
symbol = 'BTCUSD'

# Run the trading strategy
jls_extract_var = symbol
trading_strategy(exchange, jls_extract_var)
