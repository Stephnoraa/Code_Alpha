import requests
import json
from datetime import datetime


class SimplePortfolioTracker:
    def __init__(self):
        self.portfolio = {}
        self.cash = 10000  # Starting with $10,000 cash

    def add_stock(self, ticker, shares, price=None):
        """Add a stock to the portfolio"""
        ticker = ticker.upper()

        # Get current price if not provided
        if price is None:
            price = self.get_stock_price(ticker)
            if price is None:
                print(f"Could not get price for {ticker}")
                return False

        # Add to portfolio
        if ticker in self.portfolio:
            # Calculate new average price
            current_shares = self.portfolio[ticker]["shares"]
            current_price = self.portfolio[ticker]["avg_price"]
            total_shares = current_shares + shares
            total_cost = (current_shares * current_price) + (shares * price)
            new_avg_price = total_cost / total_shares

            self.portfolio[ticker]["shares"] = total_shares
            self.portfolio[ticker]["avg_price"] = new_avg_price
        else:
            self.portfolio[ticker] = {
                "shares": shares,
                "avg_price": price
            }

        # Update cash
        self.cash -= shares * price
        print(f"Added {shares} shares of {ticker} at ${price:.2f}")
        return True

    def remove_stock(self, ticker, shares, price=None):
        """Sell stock from portfolio"""
        ticker = ticker.upper()

        if ticker not in self.portfolio:
            print(f"You don't own any {ticker} shares")
            return False

        if shares > self.portfolio[ticker]["shares"]:
            print(f"You only have {self.portfolio[ticker]['shares']} shares of {ticker}")
            return False

        # Get current price if not provided
        if price is None:
            price = self.get_stock_price(ticker)
            if price is None:
                print(f"Could not get price for {ticker}")
                return False

        # Update portfolio
        self.portfolio[ticker]["shares"] -= shares

        # Remove stock if no shares left
        if self.portfolio[ticker]["shares"] == 0:
            del self.portfolio[ticker]

        # Update cash
        self.cash += shares * price
        print(f"Sold {shares} shares of {ticker} at ${price:.2f}")
        return True

    def get_stock_price(self, ticker):
        """Get current stock price using a free API"""
        try:
            # Using Alpha Vantage API (you would need to replace with your API key)
            # For demo purposes, we'll return a random price
            import random
            return round(random.uniform(50, 500), 2)

            # In a real application, you would use:
            # url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey=YOUR_API_KEY"
            # response = requests.get(url)
            # data = response.json()
            # return float(data["Global Quote"]["05. price"])
        except Exception as e:
            print(f"Error getting price: {e}")
            return None

    def display_portfolio(self):
        """Display the current portfolio"""
        print("\n===== Your Portfolio =====")
        print(f"Cash: ${self.cash:.2f}")
        print("---------------------------")

        total_value = self.cash

        for ticker, data in self.portfolio.items():
            shares = data["shares"]
            avg_price = data["avg_price"]
            current_price = self.get_stock_price(ticker)

            if current_price is None:
                print(f"{ticker}: {shares} shares, Avg Price: ${avg_price:.2f}, Current Price: Unknown")
                continue

            value = shares * current_price
            gain_loss = (current_price - avg_price) * shares
            gain_loss_percent = ((current_price / avg_price) - 1) * 100

            print(f"{ticker}: {shares} shares")
            print(f"  Avg Price: ${avg_price:.2f}, Current Price: ${current_price:.2f}")
            print(f"  Value: ${value:.2f}")
            print(f"  Gain/Loss: ${gain_loss:.2f} ({gain_loss_percent:.2f}%)")

            total_value += value

        print("---------------------------")
        print(f"Total Portfolio Value: ${total_value:.2f}")
        print("===========================\n")

    def save_portfolio(self, filename="portfolio.json"):
        """Save portfolio to a file"""
        data = {
            "cash": self.cash,
            "portfolio": self.portfolio,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Portfolio saved to {filename}")

    def load_portfolio(self, filename="portfolio.json"):
        """Load portfolio from a file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.cash = data["cash"]
                self.portfolio = data["portfolio"]
            print(f"Portfolio loaded from {filename}")
            return True
        except Exception as e:
            print(f"Error loading portfolio: {e}")
            return False


# Demo usage
if __name__ == "__main__":
    tracker = SimplePortfolioTracker()

    # Add some sample stocks
    tracker.add_stock("AAPL", 10, 150)
    tracker.add_stock("MSFT", 5, 280)
    tracker.add_stock("GOOGL", 2, 2800)

    # Display portfolio
    tracker.display_portfolio()

    # Sell some stock
    tracker.remove_stock("AAPL", 5, 160)

    # Display updated portfolio
    tracker.display_portfolio()

    # Save portfolio
    tracker.save_portfolio()

    print("Available commands:")
    print("  add <ticker> <shares> [price] - Add stock to portfolio")
    print("  sell <ticker> <shares> [price] - Sell stock from portfolio")
    print("  portfolio - Display current portfolio")
    print("  save - Save portfolio to file")
    print("  load - Load portfolio from file")
    print("  exit - Exit program")