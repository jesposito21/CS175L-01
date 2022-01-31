#CS175L 01
#Jenna Esposito
#Stocks
com_rate=float(input('What was the commission rate? '))
owned_shares=int(input('How many shares did you purchase?'))
purch_price=float(input('What was the purchase price? '))
selling_price=float(input('What was the selling price? '))
stock_price=owned_shares*purch_price
print('Amount paid for stock: $',stock_price)
commission_purch=stock_price*com_rate
print('Commission paid on the purchase: $',commission_purch)
sold_stock=owned_shares*selling_price
print('Amount the stock sold for: $',sold_stock)
commission_paid=sold_stock*com_rate
print('Commission paid on the sale: $',commission_paid)
total_commission=commission_purch+commission_paid
print('Total commission paid: $', total_commission)
profit_loss=(sold_stock-stock_price)-total_commission
print('Profit (or loss if negative): $',profit_loss)

