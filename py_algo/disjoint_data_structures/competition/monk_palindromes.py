"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-palindromes-52299611/

Monk loves maths and is always curious to learn new things. Recently, he learned about palindromes. Now, he decided to
give his students a problem which uses maths and the concept of palindromes. So, he wants the students to find how many
different numbers they can create according to the following conditions. He will give the students an integer N which
will denote the total number of digits in the final number. Also he will provide them with Q conditions where these
conditions will be of form A B where the number formed by concatenating the digits from the Ath position to Bth position
is a palindrome. You can learn more about palindromes here. Note- Numbers with leading zeros are also to be considered.

Input - Output:
First line consists of the integer N denoting the number of digits in final number.
Next line consists of the integer Q denoting the number of conditions.
Next Q lines will be of the form A B which denotes that the number formed by
concatenating the digits from the  position to  position of the final number is a palindrome.
Print the number of different numbers the students can create by following the conditions.
Since the answer can be very large, print it modulo 10^9 + 7.

Sample input:
5
2
2 4
3 5

Sample Output:
1000
"""

"""
To translate the problem to a disjoint set problem we have to note that if we have a palindrome from 0th position to
nth, then 0-n, 1-n-1, 2-n-2, etc must have the same value. That basically means that if the range of the sequence is N
and i have 10^N possible combinations, if we have a palindrome from 0 to N then we have 10^(N-N//2) combinations. We
basically need to find all such groups. For example, if we have 1-5 to be a palindrome then 1 and 5 belong to one set
and 2-4 to another. We can continue the same process to find the total number of groups. After doing so we can easily 
calculate the answer.

Final complexity: O(Q*N*INVERSE_ACKERMAN) 
"""


def find_root(array, value):
    if array[value] != value:
        array[value] = find_root(array, array[value])
    return array[value]


n = int(input())
q = int(input())
disjoint = [i for i in range(n)]
sizes = [1] * n
for _ in range(q):
    a, b = map(int, input().split())
    ind = b
    for i in range(a-1, (b+a)//2):
        val_a = i
        ind -= 1
        val_b = ind

        root_a = find_root(disjoint, val_a)
        root_b = find_root(disjoint, val_b)

        if root_a != root_b:
            if sizes[root_a] < sizes[root_b]:
                disjoint[root_a] = root_b
                sizes[root_b] += sizes[root_a]
            else:
                disjoint[root_b] = root_a
                sizes[root_a] += sizes[root_b]

groups = {}
for i in range(n):
    temp = find_root(disjoint, i)
    if temp in groups:
        continue
    else:
        groups[temp] = 1

ans = 1
temp_mod = 1000000007
for i in range(1, len(groups)+1):
    ans = ((ans % temp_mod) * (10 % temp_mod)) % temp_mod

print(ans)
