'''

Think of it as a stranger implementation of quick sort. We will first sort the array of the boys. Then, we are going to
use as pivot its first element. The pivot will be used for the girls array. As we are doing in quick sort, we will place
elements left and right from the pivot. Based on the n elements placed left, we can be sure that the first n elements
from boys have found their match because the boys array is sorted. We don't care anymore for the left array, the only
one that matters is the right array and for the boys array we need to find out what happens for the n+1 element till its
end. The same patter will repeat, this time using as pivot the first element from boys (but now boys = boys[n:end] we
once again call are strange quick sort. If at any step the left array is empty, that means that we can't find a match.
If at some point the length of the left array is bigger than the length of the boys array, are goal is achieved and all
boys can find a match. NlogN to sort boys and (NlogN/2)? (also len() is O(1) how?). If N > M we know from the beginning
that our case will be a "NO".
The other way would be to sort both arrays NlogN + NlogN and loop through all elements of boys. Each time we compare
with the first element from girls and if boys[i] > girls[0] we remove the element from girls and we continue, otherwise
there is no match. If we loop through all elements then there is a match. So that is a bit slower, NlogN + NlogN + N.

'''

def quicky_sort(array, boys):
    pivot = boys[0]
    left = []
    right = []
    for i in range(len(array)):
        if array[i] < pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    temp_len = len(left)
    if temp_len == 0:
        return False

    if len(boys) <= temp_len:
        return True

    return quicky_sort(right, boys[temp_len:])


inp_len = int(input())
for _ in range(inp_len):

    n, m = map(int, input().rstrip().split())
    boys = list(map(int, input().rstrip().split()))
    girls = list(map(int, input().rstrip().split()))

    if m < n:
        print("NO")
        continue

    boys = sorted(boys)
    doable = quicky_sort(girls, boys)

    if doable:
        print("YES")
    else:
        print("NO")
