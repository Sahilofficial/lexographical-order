# import library
from math import factorial


def lexicographical_permutations(str):
    # there are going to be n ! permutations where n = len(seq)
    for p in range(factorial(len(str))):
        print(''.join(str))

        i = len(str) - 1

        # find i such that str[i:] is the largest sequence with
        # elements in descending lexicographic order
        while i > 0 and str[i - 1] > str[i]:
            i -= 1

        # reverse str[i:]
        str[i:] = reversed(str[i:])

        if i > 0:

            q = i
            # find q such that str[q] is the smallest element
            # in str[p:] such that str[q] > str[i - 1]
            while str[i - 1] > str[q]:
                q += 1

            # swap str[i - 1] and str[q]
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp


s = 'abcdefghij'
s = list(s)
s.sort()
lexicographical_permutations(s)