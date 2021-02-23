"""
Codemonk link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/pairs-having-similar-element-eed098aa/

Given an array A, having N integers A1, A2, ..., AN. Two elements of the array Ai and Aj are called similar if Ai = Aj+1
or Aj = Ai+1. Also, the similarity follows transitivity. If Ai and Aj are similar and Aj and Ak are similar, then Ai and
Ak are also similar. You need to find number of pairs of indices (i, j)  such that i<j and Ai is similar to Aj.

Input - Output:
The first line contains a single integer N denoting the number of elements in the array.
The second line contains N space separated integers where the ith elements indicates Ai.
Output the number of pairs of indices (i, j) such that i<j and Ai is similar to Aj in a single line.

Sample input:
8
1 3 5 7 8 2 5 7

Sample Output:
6
"""

"""
First of all, we need to understand that because of the Ai = Aj + 1 or Aj = Ai + 1 property, we can sort the array and
still have the exact same number of similar elements. Now, the transitivity property can be translated to taking all the
possible pairs of 2, out of a continues segment of similar elements. For example, if we have the array 1 2 3 5 5 7 7 8,
the first segment of similar elements is the segment 1 2 3, because indexes (1, 2) and (2, 3) are similar. This means 
that the indexes (1, 3) are also similar, so we need to take the binomial coefficient 3!/(2!(3-2)!) = 3!/(2!*1!) = 
= 3 * 2 * 1 / (1 * 2 * 1) = 3 * 2 / 2 = 3 = n * (n - 1) / 2 in the general case. We can also simply take directly the
first equation. Now, we need to account for the elements that are equal to each other. If there is a certain amount 
of equal elements and one of these element is similar to an element in some index, then all the other elements are
similar to this new element in that index and to each other. In our example, 5 and 5 are equal but none of these is
similar to some other element. 7 and 7 are equal and the last 7 is similar to 8, so the first 7 is similar to 8 and the
7's are similar with each other. The same formula holds, we need to take the binomial coefficient 3!/(2!(3-2)!). 

O(N) for the "for" statement.
Python uses Timsort which has O(NlogN) complexity. 

Final complexity: O(2*N + NlogN) => O(N)
"""

N = int(input())
A = list(map(int, input().rstrip().split()))
A = sorted(A)
count = 0
eq = 1
similar = False

for i in range(1, N):
    if A[i-1] + 1 == A[i]:
        # Increase the segment of similar elements.
        # We need to know if there is at least 1 pair of indices that is similar.
        # If the elements are equal, we just need to increase the segment but
        # we don't have a similar boolean variable, to avoid the case of 2 equal
        # elements, not being similar to another element.
        eq += 1
        similar = True
    elif A[i-1] == A[i]:
        eq += 1
    else:
        # Only if we had found similar elements, calculate all the other similar
        # elements that are created due to the properties of the problem.
        # Now the segment starts from the beginning.
        if similar:
            count += eq * (eq - 1)//2
            similar = False
        eq = 1

# This accounts in case of ending with similar elements.
if similar:
    count += eq * (eq - 1) // 2

print(count)
