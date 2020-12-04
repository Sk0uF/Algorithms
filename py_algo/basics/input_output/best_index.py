"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/best-index-1-45a2f8ff/

You are given an array of elements. Now you need to choose the best index of this array. An index of the array is called
best if the special sum of this index is maximum across the special sum of all the other indices. To calculate the
special sum for any index i, you pick the first element, A[i] and add it to your sum. Now you pick the next two elements
i.e. A[i+1] and A[i+2] and add both of them to your sum. Now you will pick the next  elements and this continues till
the index for which it is possible to pick the elements.

Input - Output:
First line contains the length of the array.
The next line contains the values of the array.
The output contains the best sum.

Sample input:
6
-3 2 3 -4 3 1

Sample Output:
3
"""

"""
The general idea, using as an example the sample input, is the following: For the first index (index 0), we have
1 + 3 + 1, so, for the next index we have 3 + 1 + 2, meaning we need to subtract the value of the previous index (1) and 
add the value of the next index (2). The process continues until we arrive at index 3. Now the sum is 2, thus we need to
subtract the value of the previous index (we have subtracted all the previous ones in each previous step) and subtract
some values from the position we were before we reach outside the length of the array, until the end of the array. This
process continues, step by step, the partial sum of each index finishes closer to the end of the array. When it reaches
it, the next index falls outside the array and thus we need to make those extra subtractions.

Solution using additions and subtractions in every step 

O(N) for the "while" statement plus O(N) for the "for".
We also have an added complexity each time we subtract values when
we reach an index outside the array, but i am not sure how to find it.

Final complexity: O(2*N) => O(N)
"""

inpLen = int(input())
a = list(map(int, input().rstrip().split()))

initialSteps = 2
initialPos = 1

# Initially, find for the first element of the array
# the position that it will land and the steps needed
# to land there.
while initialPos <= inpLen:
    initialPos += initialSteps
    initialSteps += 1

initialPos -= initialSteps-1
initialSteps -= 2

# This is our initial sum.
# From now on, we either need to subtract or to add some values.
initSum = sum(a[:initialPos])
sm = initSum

for i in range(1, inpLen):
    # First of all, for each next index, subtract the previous one.
    # If we haven't landed outside the array, it means we have landed one index further than the previous one.
    initSum -= a[i-1]
    if initialPos < inpLen:
        initSum += a[initialPos]
        initialPos += 1
    else:
        # If we land outside the array, it means that we have to subtract some more values.
        # It basically means that for the step we used the position was outside the array.
        # So we subtract the values from the position minus the step.
        initSum -= sum(a[initialPos-(initialSteps-1):inpLen])
        initialPos -= (initialSteps - 1)
        initialSteps -= 1

    # The minus or plus in the position and the step might seem confusing at first
    # This is just the way i wrote the code, with the initial pos starting from 1 and not from 0
    # The array though starts from 0
    if sm < initSum:
        sm = initSum
print(sm)


"""
Solution using partial sums

O(N) for the "while" statement plus O(N) to create the partial sum array 
plus O(N) for the "for".

Final complexity: O(3*N) = O(N)
"""

inpLen = int(input())
a = list(map(int, input().rstrip().split()))

initialSteps = 2
initialPos = 1

# Partial sum array
# Each index contains the sum of all the previous ones and itself
# After having that, by subtracting specific indices we can directly find the needed sum
# That way, we avoid subtracting and adding in each step like we did before
while initialPos <= inpLen:
    initialPos += initialSteps
    initialSteps += 1

initialPos -= initialSteps-1
initialSteps -= 2

partSum = []
sum = 0

for s in a:
    sum += s
    partSum.append(sum)


initSum = partSum[initialPos-1]
sm = initSum

for i in range(1, inpLen):
    if initialPos < inpLen:
        initSum = partSum[initialPos] - partSum[i-1]
        initialPos += 1
    else:
        initSum = partSum[initialPos-initialSteps] - partSum[i-1]
        initialPos -= (initialSteps - 1)
        initialSteps -= 1

    if sm < initSum:
        sm = initSum

print(sm)
