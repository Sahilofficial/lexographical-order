# lexographical-order
The lexicographic or lexicographical order (also known as lexical order, dictionary order, alphabetical order or lexicographic(al) product) is a generalization of the way words are alphabetically ordered based on the alphabetical order of their component letters. This generalization consists primarily in defining a total order on the sequences (often called strings in computer science) of elements of a finite totally ordered set, often called an alphabet.
The lexicographical order is used not only in dictionaries, but also commonly for numbers and dates.
The functions from a well-ordered set X to a totally ordered set Y may be identified with sequences indexed by X of elements of Y. They can thus be ordered by the lexicographical order, and for two such functions f and g, the lexicographical order is thus determined by their values for the smallest x such that f(x) ≠ g(x).
If Y is also well-ordered and X is finite, then the resulting order is a well-order. As shown above, if X is infinite this is not the case.
# ALGORITHM
1- String as there will be n! permutations.

2- Every iteration prints the string and finds its next larger lexicographical permutation to be printed in the next iteration.

3- The next higher permutation is found as :-

4- Let the string is called str, find the smallest index i such that all elements in str[i…end] are in descending order.

5- If str[i…end] is the entire sequence, i.e. i == 0, then str is the highest permutation. So we simply reverse the entire string to get the smallest permutation which we consider as the next permutation.

6- If i > 0, then we reverse str[i…end].

7- Then we look for the smallest element in str[i…end] that is greater than str[i – 1] and swap its position with str[i – 1].

8-This is then the next permutation.
