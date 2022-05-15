def amount_of_pages(summary):
    string = ''
    count = 1
    while len(string) != summary:
        string = string + str(count)
        count += 1
    return count-1



print(amount_of_pages(25))