def get_summ(one, two, delimiter = ' & '):
    return(one + delimiter + two)

c = get_summ('learn', 'python').capitalize()  
print(c)  

def format_price (price):
    price = int(price)
    return('цена ' + str(price) + ' руб')

p = format_price(56.24)
print(p)

