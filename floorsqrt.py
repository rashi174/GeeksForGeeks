"""

Given an integer x. The task is to find the square root of x. If x is not a perfect square, then return floor(√x).

Input Format:
First line of input contains number of testcases T. For each testcase, the only line contains the number x.

Output Format:
For each testcase, print square root of given integer.

User Task:
The task is to complete the function floorSqrt() which should return the square root of given number x.

Constraints:
1 ≤ T ≤ 1000
1 ≤ x ≤ 107

Example:
Input:
2
5
4

Output:
2
2

Explanation:
Testcase 1: Since, 5 is not perfect square, so floor of square_root of 5 is 2.
Testcase 2: Since, 4 is a perfect square, so its square root is 2.
 
"""

{
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(floorSqrt(x))
            
            T-=1
if __name__ == "__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def floorSqrt(x): 
    #Your code here
    res=math.sqrt(x)
    return math.floor(res)