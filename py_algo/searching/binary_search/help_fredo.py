from math import log10

n = int(input())
array = [int(element) for element in input().strip().split()]

log_value = 0

for element in array:
    log_value += log10(element)

print(int(10 ** (log_value/n)) + 1)

# Let our number be x, then x^n > a1*a2*...*an
# logx^n > log(a1*a2*...*an)
# 10^logx > 10^log(a1*a2*...*an)/n
# x > 10^(log(a1) + log(a2) + ... + log(an))/n
# Better to compute additions with log rather than
# big multiplication and then log. That's a good usage
# of log. Ofc we can use log2 or w/e log we want.
# Answer is int(10^(log(a1) + log(a2) + ... + log(an))/n) + 1

# l = 1
# for element in array:
#     l *= element**(1.0/n)
#
# print(int(l) + 1)