def anagrams(word, words):
    lst = []
    for i in words:
        if sorted(i) == sorted(word):
            lst.append(i)
    return lst




print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))