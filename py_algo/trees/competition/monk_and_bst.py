"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/monk-and-bst-b29fdb91/

The problem is extremely bad written thought it's very nice. We are given a complete BST with some extra properties.
The tree has L levels and 2^L - 1 nodes. The sum of all nodes must be the smallest integer that is bigger than S. Each
left sub-tree contains nodes with values equal or less than the parent. Each right sub-tree contains nodes with values
greater than the parent. If a node has a level i then the sub-tree rooted at that node should have exactly 2^(L-i)
number of distinct values. Note that it is the number of distinct values in the sub-tree and not the number of nodes in
the sub-tree. If a is the smallest value and b the biggest then all the in between values must appear at least one time.
We have 2 types of questions. Type 0: Find the closest node to the root whose value is equal to val and print the path
to that node from the root. If root has value equal to val print "root". Else print "l" or "r" for every child visited.
Consider that the tree is unique. The values in the queries will always exist in the tree.

Input - Output:
First line consists of two integers L and S as described in the question.
Second line consists of Q, denoting the number of queries.
Each of the following Q lines consists of two integers.
The first integer denoting the type of query and second denoting either val or k as described in the queries.
For each query, print the required answer in a separate line.

Sample input:
3 16
5
0 3
0 4
1 4
1 7
0 5

Sample Output:
root
r
2
5
rr
"""

"""
The problem is tricky. We solve it by finding some cool repeating patters which will always be encountered for the tree
to be unique (this need proof). The patterns we need to find to solve the problem are the following:

1) All the nodes of the tree will occur twice, except from the biggest value which will occur once. If the lowest value
is x and the height is l then the tree must have 2^(l-1) distinct values, from x to x+(2^(l-1) - 1) with x+(2^(l-1) - 1)
being the biggest value. Thus, we have 2*x + 2*(x+1) + ... + x+(2^(l-1) - 1) > S, or
x*(2^l - 1) + 2*((2^(l-1) - 2)*(2^(l-1) - 2 + 1)/2) + (2^(l-1) - 1) > S =>
=> x > [S - (2*((2^(l-1) - 2)*(2^(l-1) - 2 + 1)/2) + (2^(l-1) - 1))]/((2^l - 1))
=> x = int([S - (2*((2^(l-1) - 2)*(2^(l-1) - 2 + 1)/2) + (2^(l-1) - 1))]/((2^l - 1))) + 1

2) At each level, going from index to another index, there is a different of 2^(height-1) with height being 1 at the
base of the tree.

3) From each parent we can go the left or the right child with a difference of 2^(height-3) with height being 1 at the
base of the tree. If height-3 is negative then the left child has the same value as the parent and the right +1.

We use 1, 2 and 3 to calculate all the left children beginning from the bottom left and the root. Then, to solve queries
of type 1 we find the height of the given index (by counting how many divisions by 2 we can make until reaching the
root) and then we directly know the value because we know the left child and the difference between the children. This
is nearly constant, O(1). Then, to solve queries of type 0 we make a classic BST search because we know the root and 
we know the the value of all the children based on 3. This takes O(HEIGHT) = O(logN) in our case.

Final complexity: O(Q*(N+logN))
"""

l, s = map(int, input().split())

# Find the amount of nodes and the nodes
# that are on the last level.
nodes = 2 ** l - 1
base_nodes = 2 ** (l-1)
x = int((s - (2 * ((base_nodes-2) * (base_nodes-2+1)/2) + base_nodes-1))/nodes) + 1

# Find all the left children and the root. This
# array will help us calculate query of type 1.
left_children = [x, x]
for i in range(2, l):
    left_children.append(left_children[i-1]+2**(abs(i+1-3)))

q = int(input())
for _ in range(q):
    query, val = map(int, input().split())
    if query == 1:
        temp_val = val
        height = 0

        # Calculate the height.
        while temp_val:
            temp_val //= 2
            height += 1
        initial_index = 2**(height-1)
        height = l - height + 1
        ans = left_children[height-1] + (val-initial_index) * (2**(height-1))
        print(ans)
    else:
        root = left_children[-1]
        if val == root:
            print("root")
        else:
            path = ""
            height = l

            # BST search.
            while True:
                if val > root:
                    path += "r"
                    if height - 3 >= 0:
                        root = root+2**(height-3)
                    else:
                        root = root + 1
                elif val < root:
                    path += "l"
                    if height - 3 >= 0:
                        root = root-2**(height-3)
                    else:
                        root = root
                else:
                    print(path)
                    break
                height -= 1
