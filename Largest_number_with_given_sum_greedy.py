'''
#https://practice.geeksforgeeks.org/problems/largest-number-with-given-sum-1587115620/1/?track=ppc-greedy&batchId=221
Largest number with given sum
A boy lost the password of his super locker. He remembers the number of digits N as well as the sum S of all the digits of his password. He know that his password is the largest number of N digits that can be possible with given sum S. As he is busy doing his homework, help him retrieving his password.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains two space separated integers N and S, where N is the number of digits in password and S is the sum of all the digits of the password.

Output:
Corresponding to each test case, in a new line, print the largest integer if possible , else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 104
0 <= S <= 106

Example:
Input:
3
5 12
3 29
3 26

Output:
93000
-1
998

Explanation :
Testcase 1: Sum of elements is 12. Largest possible 5 digit number is 93000.
Testcase 2: There is no such three digit number whose sum is 29.

'''

def largestnum(n,s):
    largest=int('9'*n)
    smallest=int('1'+'0'*(n-1))
    li= []
    for i in range(largest,smallest,-1):
        x=0
        i=str(i)
        for j in i:
            x+=int(j)
        if x==s:
            li.append(i)
    if not li:
        return -1      
    else:
        return max(li)
    
