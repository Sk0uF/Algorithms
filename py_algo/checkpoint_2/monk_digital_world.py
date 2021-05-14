# https://www.hackerearth.com/problem/algorithm/monk-and-digital-world-code-monk-5cd78708/
n = int(input())
first = input()
second = input()
occ_first = {}
occ_second = {}
for character in first:
    if character in occ_first:
        occ_first[character] += 1
    else:
        occ_first[character] = 1

for character in second:
    if character in occ_second:
        occ_second[character] += 1
    else:
        occ_second[character] = 1

ans = "YES"
for character in occ_first:
    if character not in occ_second:
        ans = "NO"
        break
    else:
        if occ_first[character] != occ_second[character]:
            ans = "NO"
            break

print(ans)