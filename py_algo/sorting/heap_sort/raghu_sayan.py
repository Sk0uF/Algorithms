"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/sorting/heap-sort/practice-problems/algorithm/raghu-vs-sayan/

Raghu and Sayan both like to eat (a lot) but since they are also looking after their health, they can only eat a limited
amount of calories per day. So when Kuldeep invites them to a party, both Raghu and Sayan decide to play a game. The
game is simple, both Raghu and Sayan will eat the dishes served at the party till they are full, and the one who eats
maximum number of distinct dishes is the winner. However, both of them can only eat a dishes if they can finish it
completely i.e. if Raghu can eat only 50 kCal in a day and has already eaten dishes worth 40 kCal, then he can't eat a
dish with calorie value greater than 10 kCal. Given that all the dishes served at the party are infinite in number,
(Kuldeep doesn't want any of his friends to miss on any dish) represented by their calorie value(in kCal) and the amount
of kCal Raghu and Sayan can eat in a day, your job is to find out who'll win, in case of a tie print “Tie” (quotes for
clarity).

Input - Output:
First line contains number of test cases T.
Each test case contains two lines.
First line contains three integers A, B and N where A and B are
the maximum amount of kCal Raghu and Sayan can eat per day and N is
the number of dishes served at the party.
Next line contains N integers where ith integer is the amount of kCal ith dish has.
For each test case print "Raghu Won" (quotes for clarity) if Raghu wins else if print "Sayan Won"
(quotes for clarity) if Sayan wins else print "Tie" (quotes for clarity) if both eat equal number of dishes.

Sample input:
3
15 20 3
10 5 4
3 10 2
4 7
10 8 3
4 5 5

Sample Output:
Sayan Won
Sayan Won
Raghu Won
"""

"""
Sort the calories of the served dishes, start subtracting them from the total calories of each person and count 1 for
each dish they can eat. Always eat the smaller dish in calories to get the maximum dishes they can eat.

Final complexity: O(N)
"""

inp_len = int(input())

for _ in range(inp_len):
    a, b, n = map(int, input().rstrip().split())
    calories = list(map(int, input().rstrip().split()))

    calories = sorted(calories)

    count_a = 0
    count_b = 0
    for i in range(n):
        if a >= calories[i]:
            a -= calories[i]
            count_a += 1
        if b >= calories[i]:
            b -= calories[i]
            count_b += 1

    if count_a > count_b:
        print("Raghu Won")
    elif count_a < count_b:
        print("Sayan Won")
    else:
        print("Tie")
