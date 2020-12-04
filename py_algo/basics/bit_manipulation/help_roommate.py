"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/a-new-experiment/

Initially you are given the number 0. After each day the number doubles itself. At any day, you can add the number 1 any
number of times during the day. You are given a number N and you need to tell the minimum number of times you have to
add 1 to get N at any point of time.

Input - Output:
First line contains the number of test cases.
The next lines contain the number N for each
test case.
For every test case print the required output.

Sample input:
4
4
8
7
5

Sample Output:
1
1
3
2
"""

"""
The problem is equivalent to finding the number of set bits in the binary representation. Why is that? The binary 
representation answers to this problem exactly. By dividing by 2 we find how many times the number 2 fits in 23 (we cut
the number in half, for example 23) and we also find if there is any remainder. The remainder can only be 0 or 1 in this
case. If we keep doing that for every quotient and keep the remainders, then we have a number consisting of 0 and 1.
So, if we reverse the procedure and we begin from 0, all we have to do is double and add 1 or just double the number.
This means, that we can begin from 0 at each step we can multiply by 2 and add 1 or just multiply by 2 until we reach
the desired result. The order that shows us what to do begins from bottom to top. If we see an 1, we double and add 1.
If we see a 0, we just double. (Try to always find the logic of this statement). Now take the number 23 for example.
The binary representation is 10111. We start at 0. To start going we double at 0 and add 1 and then we double at 2. Α 1
follows, so we just double at 4 and add 1 to get to 5. Then, we double at 10 and add 1 to get to 11 and finally we
double at 22 and add 1 to reach 23. In each step there is no reason to make more than one addition of 1. For example,
when awe are at 1, we don't need to add another 1 in the step because we will reach 2, which will be the result after
doubling 1. When we are at 2, we can't add anything cause if we did, we would not reach the number 23 by doubling, so we
would need many more additions. When we are at 4, if we don't add 1 we will need more additions in the end and if we add
it more than 1 times then we can't reach the number 23. Same goes for the next. Lets see the binary version. We are at 0
and we dobule at 0 and then we need the first 1 to start rolling, so we are at 1. Now we double at 10 and then we double
at 100. We ad 1 to get to 101, we double at 1010, we add 1 to get to 1011, we double at 10110 and then we add the last 1
to get to 10111 = 23. So, we "see" the bits from bottom to top (left to right) and we find the logic.

23 2|   Finally, as we know, if we have the binary number 10111 then this is equal to 1*2^4 + 1*2^2 + 1*2^1 + 1*2^0
11 1|   We did not think of it this way though. The thoughts are equal though, why? The number based on our approach 
5  1|   would be: (((((0*2 + 1) * 2) * 2 + 1) * 2 + 1) * 2 + 1) = (((1*2*2 + 1) * 2 + 1) * 2 + 1) = 
2  1|   = (2*2*2 + 2 + 1) * 2 + 1 = 2*2*2*2 +2*2 + 2 + 1 = 2^4 + 2^2 + 2^1 + 1*2^0
1  0|   
0  1|
----|

O(N) for the "while" statement. The input lines constraint is insignificant.

Final complexity: O(N)
"""

inp_len = int(input())

for i in range(inp_len):
    num = int(input())
    count = 0

    while num:
        # Count the number of 1's using bit manipulation
        # num - 1 changes the LSB and the bits right to it.
        # Each time we make num & (num - 1) we remove the LSB.
        num = num & (num - 1)
        count += 1
    print(count)
