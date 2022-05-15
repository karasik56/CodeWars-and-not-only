'''https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python'''


def high(x):
    lst = list(x.split())
    alphabet = [chr(i) for i in range(97, 123)]
    score_point_fullset = [i for i in range(1, len(alphabet)+1)]
    full_dict = dict(zip(alphabet, score_point_fullset))
    score_point = 0
    dict_word_score = {}
    for i in lst:
        for k in i:
            score_point += full_dict.get(k)
        dict_word_score[i] = score_point
        score_point = 0
    max_val = max(dict_word_score.values())
    for key, value in dict_word_score.items():
        if max_val == value:
            return key
    print(dict_word_score)


print(high('man i need a taxi up to ubud'))



