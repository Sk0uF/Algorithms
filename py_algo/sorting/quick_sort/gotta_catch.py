"""
Codemonk link: https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/practice-problems/algorithm/gotta-catch-em-all/

Little Arihant has always wanted to be the best Pokemon trainer in this world. And he thinks he has achieved his goal,
so he wants to quickly go and meet Professor Oak and verify this fact. But like all Pokemon trainers, he has a weird
habit too. He catches Pokemons which can go through evolution to become a better one. After roaming in the Pokemonworld
for days, he has finally managed to catch k such Pokemons. The way he can make a Pokemon go through evolution is NOT by
making them fight battles, but by using an evolution stone. Since he has k Pokemons, he naturally needs k evolution
stones for every one of them, as well. Now it takes little Arihant one complete day, to use the evolution stone on one
Pokemon. And for each Pokemon, he knows how many days will they take to evolute after the evolution stone has been used
on them. He will go to meet Professor Oak, the very next day, once all his Pokemons have gone through evolution. He can
select the order of applying evolution stones as he likes, so he wants to do it in such a way that he gets to meet
Professor Oak as soon as possible!

Input - Output:
The input has two lines. The first line will contain an integer k
which denotes the number of Pokemons.
Then, a line with k integers follows, where the i-th integer denotes the
number of days it takes for the i-th Pokemon to evolve.
You need to print the earliest day when little Arihant can go meet Professor Oak.

Sample input:
2
3 1

Sample Output:
5
"""

"""
Sort the days of each pokemon's evolution. We will begin from the most days. The key notice here is that we can use the
stone to a pokemon while we are at the evolution period of another. We consider a queue, being the most days of
evolution. The next pokemon will have the same days or less. If it has the same days we add 1 day and the queue remains
as is. If it has less days we just used 1 day from the queue and we decrease it by 1. We follow the same procedure till
the end.
"""

inp_len = int(input())
array = list(map(int, input().rstrip().split()))

array = sorted(array, reverse=True)

days = 2 + array[0]
queue = array[0]

for i in range(1, inp_len):
    if array[i] < queue:
        queue -= 1
    else:
        days += 1

print(days)
