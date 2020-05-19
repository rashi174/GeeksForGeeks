#https://practice.geeksforgeeks.org/problems/check-set-bits/0
'''Given a number N. Write a program to check whether every bit in the binary representation of the given number is set or not.

Input:
First line of input contains a single integer T which denotes the number of test cases. T test cases follows. First line of each test case contains a single integer N which denotes the number to be checked.

Output:
For each test case, print "YES" without quotes if all bits of N are set otherwise print "NO".

Constraints:
1<=T<=1000
0<=N<=1000

Example:
Input:
3
7
14
4
Output:
YES
NO
NO

 

** For More Input/Output Examples Use 'Expected Output' option **
'''


for _ in range(int(input())):
    n=int(input())
    n=bin(n)[2:]
    if set(n)=={'1'}:
        print("YES")
    else:
        print("NO")