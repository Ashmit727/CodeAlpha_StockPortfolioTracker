# Stock Portfolio Tracker
# CodeAlpha Internship Project

stock_prices = {
    # Indian Companies
    "RELIANCE": 1500,
    "TCS": 3500,
    "INFY": 1800,
    "HDFCBANK": 1700,
    "ITC": 450,
    "WIPRO": 550,
    "SBIN": 850,
    "BHARTIARTL": 1800,
    "LT": 3800,
    "TATAMOTORS": 950,

    # Global Companies
    "AAPL": 180,
    "MSFT": 420,
    "GOOGL": 170,
    "AMZN": 220,
    "TSLA": 320,
    "META": 750,
    "NVDA": 145,
    "NFLX": 1250,
    "IBM": 290,
    "ORCL": 250
}

total_investment = 0
portfolio = []

print("=" * 60)
print("📈 STOCK PORTFOLIO TRACKER")
print("=" * 60)

print("\nAvailable Stocks:")
for stock in stock_prices:
    print(f"• {stock}")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").strip().upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        try:
            quantity = int(input("Enter quantity: "))

            investment = stock_prices[stock] * quantity
            total_investment += investment

            portfolio.append({
                "stock": stock,
                "price": stock_prices[stock],
                "quantity": quantity,
                "investment": investment
            })

            print(
                f"✅ {stock}: ₹{stock_prices[stock]} × "
                f"{quantity} = ₹{investment}"
            )

        except ValueError:
            print("❌ Please enter a valid number.")

    else:
        print("❌ Stock not available.")
        print("💡 Try: RELIANCE, TCS, INFY, AAPL, MSFT, TSLA")

print("\n" + "=" * 60)
print("📊 PORTFOLIO SUMMARY")
print("=" * 60)

if len(portfolio) == 0:
    print("No stocks added.")
else:
    for item in portfolio:
        print(
            f"{item['stock']} | "
            f"Price: ₹{item['price']} | "
            f"Qty: {item['quantity']} | "
            f"Value: ₹{item['investment']}"
        )

print("-" * 60)
print(f"💰 Total Investment Value: ₹{total_investment:,}")
print("=" * 60)

# Save summary to file
with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=" * 60 + "\n")

    for item in portfolio:
        file.write(
            f"{item['stock']} | "
            f"Price: ₹{item['price']} | "
            f"Qty: {item['quantity']} | "
            f"Value: ₹{item['investment']}\n"
        )

    file.write("-" * 60 + "\n")
    file.write(
        f"Total Investment Value: ₹{total_investment:,}\n"
    )

print("\n✅ Portfolio summary saved in 'portfolio_summary.txt'")
print("🎉 Thank you for using Stock Portfolio Tracker!")