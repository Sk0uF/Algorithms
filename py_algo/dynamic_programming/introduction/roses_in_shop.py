"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/roses-for-valentine-4a795f72/

There are n roses in a shop. Each rose is assigned an ID. These roses are arranged in order 1, 2, ..., n. Each rose has
a smell factor denoted as smell[i] (1 <= i <= n). You want to buy roses from this shop under the condition that you can
buy roses in a segment. In other words, you can purchase roses from l to r (1 <= l <= r <= n). You can remove at most
rose from this segment of roses. Thus, the final length of roses is n-1 or n. Your task is to calculate the maximum
possible length of the strictly-increasing contiguous sub array of the smell factors of these roses. A contiguous sub
array a with indices from l to r is a[l, ..., r] = a[l], a[l+1], ..., a[r]. The sub array a[l, ..., r] is strictly
increasing if a[l] < a[l+1] < ... < a[r].

Input - Output:
The first line contains a single integer  denoting the number of roses that are available in the shop.
The second line contains n space-separated integers smell[1], smell[2], ..., smell[n].
Print one integer denoting the maximum possible length of the strictly-increasing contiguous sub array of the
smell factor after removing at most one element.

Sample input:
5
1 2 5 3 4

Sample Output:
4
"""

"""
We are going to consider every point as a removing point. Then the answer can be given if we calculate the prefix and 
suffix arrays containing the largest increasing sequence up to an index and starting from that index. The answer then
will simply be ans = max(ans, pre[i-1] + suff[i+1]), iterating through the whole array.

Final complexity: O(N)
"""

# Dp
n = int(input())
smell = list(map(int, input().split()))
pre = [1] * n
suff = [1] * n
ans = 1

for i in range(1, n):
    if smell[i] > smell[i-1]:
        pre[i] = pre[i-1] + 1
        ans = max(ans, pre[i])

for i in range(n-2, -1, -1):
    if smell[i+1] > smell[i]:
        suff[i] = suff[i+1] + 1
        ans = max(ans, suff[i])

for i in range(1, n-1):
    if smell[i-1] < smell[i+1]:
        ans = max(ans, pre[i-1]+suff[i+1])

print(ans)

"""
Another solution can be given without dp in linear dp but it's more complex and time consuming to understand. We iterate
through the array. If we find a bigger element then it's pointless to remove it. The only case would be to remove the 
previous element (e.g 1 3 5 7 9 2 10 if are at 10 we could remove 2 and achieve a bigger sequence), otherwise we just
add + 1. We only remove the previous element if we had previously made a reset, meaning that from an increasing sequence
we just found smaller number. Now, if we are at a reset point we can either remove the previous element or not based on 
the value of the i-2 element. We make sure to calculate the starting and ending indices of our movement to properly
calculate the largest sequences.

Final complexity: O(N)
"""

# Non Dp
n = int(input())
smell = list(map(int, input().split()))
score = [0] * n
score[0] = 1
start = 0
end = 0
found = False

# Initialization
if smell[1] > smell[0]:
    score[1] = 2
    end = 1
else:
    score[1] = 1
    found = True


for i in range(2, n):
    # If we find a bigger element we have to check if we can remove
    # the previous. It would be pointless to do so if we didn't just
    # move the start and end indices and the previous value isn't 1.
    if smell[i] > smell[i-1]:
        if not found:
            score[i] = score[i-1] + 1
            end += 1
        else:
            # If we can remove the element because then the previous
            # will be bigger then we find the new value based on the
            # indices and then we move them.
            if smell[i] > smell[i-2]:
                score[i] = end - start + 2
                start = i-1
                end = i
            # In other case we just move the indices and add 1 to the
            # previous value.
            else:
                start = i-1
                end = i
                score[i] = score[i-1] + 1
            found = False
    # If we find a smaller element we have to reset.
    else:
        # If we can't remove the element because then the previous
        # will still be bigger then we have a value of 1.
        # When we have multiple such elements in a row we have to move the
        # start and end counters to the current index.
        if smell[i-2] >= smell[i]:
            score[i] = 1
            if found:
                start = i
                end = i
            found = True
        # If we can remove the element then we find the value
        # and once again move the start and end counters to the current index.
        else:
            score[i] = end - start + 1
            found = False
            start = i
            end = i

print(max(score))
