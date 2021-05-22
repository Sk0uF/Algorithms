# https://www.hackerearth.com/problem/algorithm/little-monk-and-library-80fc56d8/?utm_source=header&utm_medium=search&utm_campaign=he-search
n = int(input())
books = list(map(int, input().split()))
shelves = list(map(int, input().split()))
books = sorted(books)
shelves = sorted(shelves)

time = 0
for i in range(n):
    time += abs(books[i]-shelves[i])

print(time)