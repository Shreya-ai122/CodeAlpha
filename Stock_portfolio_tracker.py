import os

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}
total_value = 0

print("📈 Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = quantity
        except ValueError:
            print("❌ Please enter a valid number.")
    else:
        print("⚠ Stock not found. Please try again.")

# Display summary
print("\n🧾 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Save to file with error handling
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    try:
        with open("portfolio_summary.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
            file.write(f"\nTotal Investment Value: ${total_value}")
        print("✅ Saved to 'portfolio_summary.txt'")
    except Exception as e:
        print("❌ Could not save the file. Error:", e)

