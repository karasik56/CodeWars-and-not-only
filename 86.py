def taxi_price():
    base_tarif = 4
    distanse_tarif = 0.25
    min_distanse_paid = 0.14
    user_distanse = float(input())
    total_price = base_tarif + (user_distanse / min_distanse_paid * distanse_tarif)
    print(total_price)


taxi_price()