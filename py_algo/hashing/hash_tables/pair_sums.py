"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/pair-sums/

You have been given an integer array A and a number K. Now, you need to find out whether any two different elements of
the array A sum to the number K. Two elements are considered to be different if they lie at different positions in the
array. If there exists such a pair of numbers, print "YES" (without quotes), else print "NO" without quotes.

Input - Output:
The first line consists of two integers N,
denoting the size of array A and K.
The next line consists of N space separated integers denoting the elements of the array A.

Sample input:
5 9
1 2 3 4 5

Sample Output:
YES
"""

"""
By using the build in python's hash table (dictionary) we insert all the integers from the initial array into the table
as keys and their values is the number of occurrences. Then, we loop through the array and subtract each value from
the integer we want to reach. That way we get the number that if we add in the initial value we will reach the desired
integer. If that number exists in the hash table then we have a solution. We also have to consider the case in which the
integer can be reach by the addition of the same values (for example the solution for 8 could be 4+4). That's why we
store all the occurrences for each key in the hash table. Think of it!

O(N) to create the hash table and then
O(N) to loop through it.

Final complexity: O(2*N) => O(N)
"""

n, k = map(int, input().split())
array = list(map(int, input().split()))
hash_table = {}

for element in array:
    if element in hash_table:
        hash_table[element] += 1
    else:
        hash_table[element] = 1

ans = "NO"
for element in array:
    number = k - element
    if number <= 0:
        continue

    if number in hash_table:
        if number == element:
            if hash_table[number] > 1:
                ans = "YES"
            else:
                continue
        else:
            ans = "YES"
            break

print(ans)
