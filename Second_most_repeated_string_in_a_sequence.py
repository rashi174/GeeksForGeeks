#https://practice.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence/0
'''
Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.

Note: No two strings are the second most repeated, there will be always a single string.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting number of strings in a sequence and the second line contains N space separated strings.

Output:
For each test case, in a new line print the second most repeated string.

Constraints:
1<=T<=100
3<=N<=103
1<=|String length|<=100

Example:
Input:
2
6
aaa bbb ccc bbb aaa  aaa
6
geeks for geeks for geeks aaa

Output:
bbb
for

** For More Input/Output Examples Use 'Expected Output' option **
'''
#here just sort the list by taking key as count function
for _ in range(int(input())):
    n=int(input())
    li=list(input().split())[:n]
    print(sorted(set(li),key=li.count)[-2])