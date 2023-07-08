# Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
price = 0
for key in stock:
    price = price + stock.get(key) * prices.get(key)
print(price)
