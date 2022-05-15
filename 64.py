def sales(new_price):
    percent = 60
    for price in new_price:
        old_price = round((price * 100)/(100 - percent), 2)
        sum_of_sale = round(old_price - price, 2)
        print(f'Исходная цена {old_price}, Сумма скидки {sum_of_sale}, Новая цена {price} ')


new_price = [4.95, 9.95, 14.95, 19.95, 24.95]
sales(new_price)
