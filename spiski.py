citys = {
    'city': 'moscow',
    'temper': 20,

}
citys['date'] = '27.05.2019'
citys["temper"] -=5
print(citys)
print(citys['city'])
print(citys.get('country'))
print(citys.get('country','Россия'))
print(len(citys))
