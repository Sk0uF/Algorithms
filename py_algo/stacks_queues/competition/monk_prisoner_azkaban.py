"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-prisoner-of-azkaban-0f96c4a2/

Monk's wizard friend Harry Potter is excited to see his Dad fight Dementors and rescue him and his Godfather Sirius
Black. Meanwhile their friend Hermoine is stuck on some silly arrays problem. Harry does not have time for all this, so
he asked Monk to solve that problem for Hermoine, so that they can go. The problem is given an array A having N integers
for each i (1<=i<=N), find x+y, where x is the largest number less than i such that  A[x] > A[i] and y is the smallest
number greater than i such that A[y] > A[i]. If there is no x < i such that A[x] > A[i] then x is -1. The same holds for
y.

Input - Output:
First line consists of a single integer denoting N.
Second line consists of N space separated integers denoting the array A.
Print N space separated integers, denoting x+y.

Sample input:
5
5 4 1 3 2

Sample Output:
-2 0 6 1 3
"""

"""
We can think of the problem as 2 separate problems, one for finding x and one for finding y. To find x, we are going to
loop though the array and for each element find the closest element to its left that is bigger than our current element.
We can find this solution in linear time and more particular in O(2*N). To explain the logic, lets see an example.

5 4 1 3 2 10

1) Number 5 is the first element and doesn't have any number bigger than itself on its left. Ans = -1.
2) We compare 4 with the previous element, in that case 5, it's smaller than 5, so the Ans = 1 (index).
3) We compare 1 with the previous element, in that case 4, it's smaller than 4, so the Ans = 2 (index).
4) We compare 3 with the previous element, in that case 1, it's not smaller than 1. Now we go back to the number that
   was bigger than 1. That is the number 4, 3 is smaller than 4, so the Ans = 2 (index.
5) We compare 2 with the previous element, in that case 3, it's smaller than 3, so the Ans = 4 (index).
6) We compare 10 with the previous element, in that case 2, it's not smaller than 2. Now we go back to the number that 
   was bigger than 2. That is the number 3, now we go back to number that was bigger than 3, that's 4, now to the number
   that was bigger than 4, that was 5.

Notice than at the 6th step we skipped number 1, because if 10 > 3 then the is no way that it will be less than an
element that was less than 3. If we had an 7th step with the number 11, then we would directly know that there is no
element bigger than 11. At each step, we compare with the previous element and sometimes go back some steps, with the
maximum number of steps to be equal with the length of the array.

If we repeat the process backwards and find the right elements that are bigger than our current element and closest to 
it then we can find y as well.

We can implement this technique with more than 1 ways. See the comments in the code for this particular implementation.

Final complexity: O(2*N + 2*N) => O(N)
"""

n = int(input())
array = list(map(int, input().rstrip().split()))

# Stack that hold the previous biggest numbers for each index.
# The left array holds the answer for each index.
stack = []
left = []

for i in range(0, n):
    while stack:
        k = stack[-1]

        # While the stack has elements, check the current element
        # with the previous. If its smaller then we found the answer.
        # If not, then we keep popping from the stack until and if we
        # find a bigger element.
        if array[i] < array[k]:
            left.append(k+1)
            stack.append(i)
            break
        else:
            stack.pop()

    # If the stack is empty then that means
    # that the is no bigger element for this
    # particular index. Just append the current
    # index for the next check.
    if not stack:
        left.append(-1)
        stack.append(i)

# Repeat the same process backwards.
right = []
stack = []

for i in range(n-1, -1, -1):
    while stack:
        k = stack[-1]
        if array[i] < array[k]:
            right.append(k+1)
            stack.append(i)
            break
        else:
            stack.pop()

    if not stack:
        right.append(-1)
        stack.append(i)

final = []
for i in range(len(left)):
    final.append(left[i] + right[len(right)-1-i])

print(*final)
