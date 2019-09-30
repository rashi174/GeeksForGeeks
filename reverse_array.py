"""
Given a string S as input. You have to reverse the given string.

Input: First line of input contains a single integer T which denotes the number of test cases. T test cases follows, first line of each test case contains a string S.

Output: Corresponding to each test case, print the string S in reverse order.

Constraints:
1 <= T <= 100
3 <= length(S) <= 1000

Example:
Input:
3
Geeks
GeeksforGeeks
GeeksQuiz

Output:
skeeG
skeeGrofskeeG
ziuQskeeG

** For More Input/Output Examples Use 'Expected Output' option **
Contributor: Harsh Agarwal
Author: harsh.agarwal0
"""



for _ in range(int(input())):
    s=input()
    print(s[::-1])