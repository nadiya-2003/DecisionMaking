
X = float(input())
Y = float(input())
cost_price_per_banana = X / 12
total_selling_price = Y * 12
profit_or_loss = total_selling_price - X
if profit_or_loss > 0:
    print(f"Profit : Rs.{profit_or_loss:.2f}")
elif profit_or_loss < 0:
    print(f"Loss : Rs.{abs(profit_or_loss):.2f}")
else:
    print("No Profit No Loss")
