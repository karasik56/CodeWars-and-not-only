'''https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python'''


def alphabet_position(text):
    lst = []
    alphabet = [chr(i) for i in range(97, 123)]
    position_point = [i for i in range(1, len(alphabet)+1)]
    full_dict = dict(zip(alphabet, position_point))
    for i in text.lower():
        if i.isalpha():
            lst.append(full_dict.get(i))
    result = ' '.join(map(str, lst))
    return result




print(alphabet_position("The sunset sets at twelve o'clock."))
