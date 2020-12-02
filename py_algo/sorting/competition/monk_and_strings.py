
inp_len = int(input())
first_char = input()
characters = [first_char]
print("0")

for i in range(1, inp_len):
    new_char = input()
    count = 0
    for j in range(len(characters)-1, -1, -1):
        if new_char > characters[j]:
            count += 1

    print(count)
    characters.append(new_char)