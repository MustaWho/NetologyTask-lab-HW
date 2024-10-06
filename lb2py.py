all_price = []
products = []
process = True
shops = []


while process:
    shop = input("Введите магазин или введите 'стоп' : ")
    if shop.lower() == "стоп":
        process = False
    else:
        shops.append(shop)

print('Магазины', shops)
process = True

while process:
    product = input("Введите продукт или введите 'стоп' : ")
    if product.lower() == "стоп":
        process = False
    else:
        products.append(product)

print('Продукты:', products)

for n in range(len(products)):
    print(f'Продукт: {products[n]}')
    shoplist = [products[n]]
    for i in range(len(shops)):
        print(f'Введите стоимость в магазине {shops[i]}')
        prise = int(input('Цена: '))
        shoplist.append((shops[i], prise))
    all_price.append(shoplist)

print(all_price)
print(all_price[0])
print(all_price[0][1])
print(all_price[0][1][0])

low_shop = []

for x, i in enumerate(all_price):
    print(x, i)
    only_shop = i[1:]
    sum_one_shop = 0
    for y in only_shop:
        print(y[1])
        sum_one_shop += y[1]
    low_shop.append([shops[x], sum_one_shop])

print()
print(low_shop)
low_shop.sort(key=lambda x: x[1])
low_shop_one = low_shop[0]
print(f'Самый выгодный магазин для покупки: {low_shop_one[0]} - {low_shop_one[1]}руб')
