"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-sorting-algorithm-3aa7826d/

Monk recently taught Fredo about sorting. Now, he wants to check whether he understood the concept or not. So, he gave
him the following algorithm and asked to implement it. Assumptions: We consider the rightmost digit of each number to be
at index 1, second last at index 2 and so on till the leftmost digit of the number. Meaning of ith chunk: This chunk
consists of digits from position 5*i to 1 + 5*(i-1) in the given number. If there is no digit at some position in the
number, take the digit to be 0. Initially, i is 1. Construct the ith chunk, for all of the integers in the array. Let's
call the value of this chunk to be the weight of respective integer in the array. If weight of all the integers of the
array is 0, then STOP. Sort the array according to the weights of integers. If two integers have same weight, then the
one which appeared earlier should be positioned earlier after the sorting is done. The array changes to this sorted
array. Increment i by 1 and repeat from STEP 1.

Input - Output:
The first line of the input contains N denoting the number of elements in the array to be sorted.
The next line contains N single space separated integers denoting the array elements.
You need to print the new array in each step of the algorithm.

Sample input:
3
213456789 167890 123456789

Sample Output:
213456789 123456789 167890
167890 123456789 213456789
"""

"""
Sort the numbers based on their value modulo by 100000 which basically is what 5*i to 5*(i-1) means. At each step,
divide the number by 100000. When the maximum value from the array becomes 0 we stop the process.

We sort N numbers for a maximum of 18/5 = 3.6 times.

Final complexity: O(3.6*NlogN)
"""

inp_len = int(input())
array = list(map(int, input().rstrip().split()))
max_elem = max(array)
mul = 1
step = 10**5

while max_elem:
    array = sorted(array, key=lambda x: (x//mul) % step)
    print(' '.join(map(str, array)))
    mul *= step
    max_elem //= step
