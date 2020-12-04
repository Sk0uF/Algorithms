"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/mystery-30/

Find the logic of the problem based on the sample input!

Input - Output:
A series of numbers.
Find the logic of the output.

Sample input:
0
1
5
12
22
1424

Sample Output:
0
1
2
2
3
4
"""

"""
The logic is simple. Print the number of the set bits of each number. Lets suppose that the current number is num. 
num - 1 reverses the bits from the least significant bit to the end, so num & (num - 1) each times removes the lsb.
Thus, all we need to do is count the times until we reach 0. If num = 10100 then num - 1 = 10011 and num & (num - 1) =
10000. The count is 1. We do the same thing one more time, the count becomes 2 and we reach 0.

The input length is significant. O(N) for the first "for" statement. 
The while statement in insignificant.

Final complexity: O(N)
"""

from sys import stdin, stdout

temp_inputs = {}

for num in stdin:
    inp = int(num)
    if inp in temp_inputs:
        count = temp_inputs[num]
    else:
        count = 0
        while inp:
            inp = inp & (inp - 1)
            count += 1

        temp_inputs[num] = count

    stdout.write(str(count) + '\n')
