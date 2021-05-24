"""
Codemonk link: https://www.hackerearth.com/problem/algorithm/little-monk-and-library-80fc56d8/?utm_source=header&utm_medium=search&utm_campaign=he-search

Little Monk as usual has not prepared for his exams. So, to ensure that he does not fail in any course, he goes to the
library and picks up N books for his N courses that he has to give exams for. The number of books being too large, he
puts them on different tables and goes to a particular table whenever he wants to read that particular book. After he is
done with studying, he has to put all the books back in their place. He finds that there are exactly N empty spaces in
the book shelf where he can put his N books. Imagine shelves and tables where books are kept, as locations on the
x-coordinate axis. Now Little Monk wants to minimize the time he takes to put books back in shelves. He takes T units of
time to put a book back in a shelf, where T denotes the distance between the book and the shelf it was put in. Once
Little Monk puts a book into a shelf, he takes 0 unit time to reach the next book he wants to put into a shelf. Since he
is dumb, and in a hurry, help him calculate the minimum time required to put all the books in shelves. Note: Once a book
has been into a shelf, you can't put another book in the same shelf. Also, initially Monk can start from any book.

Input - Output:
The first line contains a pair of integers: an integer N, which denotes the number of books and empty shelves.
Next line contains N space separated integers denoting co-ordinates of the tables where books are placed.
Next line contains N space separated integers denoting co-ordinates of shelves.
Print minimal time it will take Little Monk to put all books back in shelves.

Sample input:
3
2 1 3
4 3 2

Sample Output:
3
"""

"""
Very easy problem. Think about it.

Final complexity: O(N)
"""

n = int(input())
books = list(map(int, input().split()))
shelves = list(map(int, input().split()))
books = sorted(books)
shelves = sorted(shelves)

time = 0
for i in range(n):
    time += abs(books[i]-shelves[i])

print(time)
