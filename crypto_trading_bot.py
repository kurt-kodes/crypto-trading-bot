import random
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_price():
    """Simulate getting a random crypto price."""
    return round(random.uniform(30000, 60000), 2)

def trade_action(price, last_price):
    """Simple trading strategy based on price changes."""
    if price < last_price * 0.95:
        return "BUY"
    elif price > last_price * 1.05:
        return "SELL"
    else:
        return "HOLD"

def main():
    balance = 5000  # USD balance
    holdings = 0  # BTC holdings
    last_price = get_price()
    
    logging.info("Starting Crypto Trading Bot...")
    
    while True:
        price = get_price()
        action = trade_action(price, last_price)
        
        logging.info(f"Price: ${price}, Action: {action}")
        
        if action == "BUY" and balance >= price:
            holdings += 1
            balance -= price
            logging.info(f"Bought 1 BTC at ${price}. New balance: ${balance}")
        elif action == "SELL" and holdings > 0:
            holdings -= 1
            balance += price
            logging.info(f"Sold 1 BTC at ${price}. New balance: ${balance}")
        
        last_price = price  # Update last price
        time.sleep(2)  # Wait 2 seconds before next trade check

if __name__ == "__main__":
    main()
