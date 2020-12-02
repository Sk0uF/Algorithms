"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/question-2-38-cf73c1b4/

You are given a, b and c. You need to convert a to b. You can perform following operations:
1) Multiply a by c.
2) Decrease a by 2.
3) Decrease a by 1.
You can perform this operation in any order and any number of times. You need to find and print the minimum number of
steps to convert a to b.

Input - Output:
First line contains the number of test cases.
The next lines contain the integers a, b, c.
Print the number of minimum steps.

Sample input:
2
3 10 2
11 6 2

Sample Output:
3
3
"""

"""
--------------------------------------------
Need better understanding of the solution.
--------------------------------------------
This problem is tricky. First, we observe that if a >= b, we can only make subtractions. To find how many times we have
to subtract 2 and how many 1, we simply do (a-b) // 2 + (a-b) % 2. The div operation gives us the times we can subtract
2 from the difference of a-b to reach 0 (to cover the difference) and the mod operation gives us the remainder if any, 
meaning that we have to subtract 1. The mod2 will give us 0 or 1, so, we will either make one 1 subtraction or zero.
What if  a < b? Now, we have two cases. If c perfectly divides b, then all we have to do is reach b//c and then multiply
by c. If the above case doesn't hold, then try to reach a little further than our current b, at (b//c + 1) * c. We do +1
and not -1 because we can only subtract from a number. Now, once again, we count how many (t-b) // 2 + (t-b) % 2 and our
new b will be t = (b//c + 1) * c. In the second and third cases we use recursion for b = b//c and b = t respectively.

Final complexity: Undetermined
"""


def operation(a, b, c):
    if a >= b:
        # First case, we don't need recursion
        print("First if count + " + str((a-b) // 2 + (a-b) % 2))
        return (a-b) // 2 + (a-b) % 2

    if b % c == 0:
        # Second case, we need to call the function
        # with b = b//c
        print("Second if, b = " + str(b//c) + " count + 1 ")
        return 1 + operation(a, b//c, c)

    else:
        # Third case, we need to call the the function
        # with b = t and count the steps to reach b from t
        t = (b//c+1) * c
        print("Third if, t = " + str(t) + " count + " + str((t-b) // 2 + (t-b) % 2))
        return (t-b) // 2 + (t-b) % 2 + operation(a, t, c)


inp_len = int(input())

for _ in range(inp_len):
    a, b, c = map(int, input().rstrip().split())
    print(operation(a, b, c))
