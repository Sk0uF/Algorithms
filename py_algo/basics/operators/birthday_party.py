"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems/algorithm/birthday-party-12/

Mr. X' s birthday is in next month. This time he is planning to invite N of his friends. He wants to distribute some
chocolates to all of his friends after party. He went to a shop to buy a packet of chocolates. At chocolate shop, each
packet is having different number of chocolates. He wants to buy such a packet which contains number of chocolates,
which can be distributed equally among all of his friends. Help Mr. X to buy such a packet.

Input - Output:
First line contains the number of test cases.
Each test case contains two integers, the first being the number of friends
and the second the number of chocolates in a packet.
The output is straight forward!

Sample input:
2
5 14
3 21

Sample Output:
No
Yes
"""

"""
We just need a simple modulo operation between the number of chocolates and the number of friends, to see if we can
equally give them to everyone.

O(N) for the "for" and O(20) for the input "for", because 1 <= input <= 20.

Final complexity: O(N)
"""

inp_len = int(input())

for k in range(inp_len):
    friends_num, chocolate_num = map(int, input().rstrip().split())

    if chocolate_num % friends_num == 0:
        print("Yes")
    else:
        print("No")
