''' https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python '''

def divisors(integer):
    lst = []
    for i in range(integer-1, 1, -1):
        if integer % i == 0:
            lst.append(i)
    if len(lst) == 0:
        return f'{integer} is prime'
    return sorted(lst)




print(divisors(13))