'''
Nearest multiple of 10 
Given a positive number N. The task is to round N to nearest multiple of 10. Number can be so big and can contains 1000 of digits.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a positive number N.

Output:
For each test case, print the nearest multiple of 10 in new line.

Constraints:
1 <= T <= 100
1 <= |Number length| <= 1000

Example:
Input:
2
15
29
Output:
10
30
'''


for i in range(int(input())):
    number=int(input())
    x=10-number%10
    if x>=5:
        print(number+x-10)
    else:
        print(number+x)
