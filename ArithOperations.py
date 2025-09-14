# Input:Amount in USD and the exchange rate
usd_amount=float(input("Enter amount in US Dollars:"))
exchange_rate=85.62
# Conversion
inr_amount=usd_amount*exchange_rate 
# output
print(f"{usd_amount}USD is equivalent to {inr_amount:.2f}INR.")