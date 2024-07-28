bread=int(input("How many loaves of day old bread have you bought?"))
freshbrd=int(input("How many loaves of fresh bread have you bought?"))
pricefresh=freshbrd*3.49
priceold=bread*3.49*0.06
def day_old_bread():
    print("number of old day bread is", bread)
    print(f"your discount is" ,bread,"dollars")
    return()

def fresh_bread():
    print(f"number of fresh bread loaves is",freshbrd)
    print(f"price of fresh bread loaves is",pricefresh)
    return()

def total_price():
    print(f"total price is" , pricefresh+priceold)

day_old_bread()
fresh_bread()
total_price()