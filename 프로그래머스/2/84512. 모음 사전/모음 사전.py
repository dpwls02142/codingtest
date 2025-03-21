from itertools import product
def solution(word):
    dic = ["A", "E", "I", "O", "U"]
    words = []
    for i in range(1, 6):
        words += [''.join(w) for w in product(dic, repeat=i)]
    words.sort()
    return words.index(word) + 1