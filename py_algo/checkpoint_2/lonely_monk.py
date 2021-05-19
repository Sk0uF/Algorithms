"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/lonely-monk-code-monk-ebca6e4a/

Being alone in the new world, Monk was little afraid and wanted to make some friends. So he decided to go the famous
dance club of that world, i.e "DS Club" and met a very beautiful array A of N integers, but for some reasons she was
very sad. Being asked by Monk, she told him that she wants to find out the total number of sub arrays in it, having
their sum even. In order to impress her, Monk wants to solve this problem for her.

Input - Output:
First line of input consists of integer N.
Next line will consists of N integers.
Print the total number of sub arrays of this array with even sum.

Sample input:
5
2 5 4 4 4

Sample Output:
7
"""

"""
The implementation of this problem is very easy but the thought is quite more hard. We can solve the problem in linear 
time. We just have to think that if we subtract or add 2 even numbers we get an even number and the same goes for adding
or subtracting 2 odd numbers, we once again get an even number. We are going to keep the cumulative sum and each time
we end up in an even or odd number we are going to add +1 the amount of even of odd sums up to that point. Before we do
that, if we end to an even number we add the amount of even numbers up to that point and we do the same if we end up to
an odd number.

Final complexity: O(N)
"""

n = int(input())
array = list(map(int, input().split()))
current = 0
ans = 0
odd = 0
even = 1
for i in range(n):
    current += array[i]

    temp = current % 2
    if temp == 0:
        ans += even
        even += 1
    else:
        ans += odd
        odd += 1

print(ans)
