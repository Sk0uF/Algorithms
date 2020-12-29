"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-search-2-cff3fa01/

Monk and his friend Micro are on a quest to find the answer of Life, Universe and Everything. In order to complete it
they need to answer Q queries on an array A having N integers. The queries can be of following two types:
0 x: Find the number of numbers in A which are not less than x.
1 x: Find the number of numbers in A which are greater than x.
Help them complete the quest and be back in time for the next Code Monk Challenge.

Input - Output:
First line consists of a single integer denoting N.
Second line consists of N space separated integers denoting the array A.
Third line consists of a single integer denoting Q.
Each of the following Q lines consists of a query of one of the given two types.
For each query print the required answer in new line.

Sample input:
4
1 2 3 4
3
0 5
1 3
0 3

Sample Output:
0
1
2
"""

"""
Find the lower and upper bound of the array. The lower bound is the index of the first element that is equal or bigger 
than x. The upper bound is the index of the first element that is greater than x. After finding those indices the answer
is simply n - lower_bound or n - upper_bound. The names lower and upper bound are not well defined in my opinion. By 
changing the if statements both can be considered "upper" or "lower" bounds.

O(NlogN) for the sorting and O(2*QlogN) for the binary search
for each query.

Final complexity: O(NlogN + 2QlogN)
"""


def lower_bound(lower, upper, a, num):
    while lower < upper:
        mid = (lower+upper) // 2
        if a[mid] >= num:
            upper = mid
        else:
            lower = mid + 1
    return lower  # Can return upper as well.


def upper_bound(lower, upper, a, num):
    while lower < upper:
        mid = (lower + upper) // 2
        if a[mid] <= num:
            lower = mid + 1
        else:
            upper = mid
    return lower  # Can return upper as well.


n = int(input())
a = list(map(int, input().rstrip().split()))
q = int(input())

a = sorted(a)
for _ in range(q):
    query, num = map(int, input().rstrip().split())

    if query == 0:
        if num > a[-1]:
            print(0)
            continue
        elif num <= a[0]:
            print(n)
            continue
        print(n - lower_bound(0, n - 1, a, num))
    else:
        if num >= a[-1]:
            print(0)
            continue
        elif num < a[0]:
            print(n)
            continue
        print(n - upper_bound(0, n - 1, a, num))
