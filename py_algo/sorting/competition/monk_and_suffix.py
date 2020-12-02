
inp = input().rstrip().split()
inp_string = inp[0]
position = int(inp[1])

suffices = []

prev = ""
for i in range(len(inp_string) - 1, -1, -1):
    temp_string = inp_string[i]
    prev = temp_string + prev
    suffices.append(prev)

suffices = sorted(suffices)
print(suffices[position-1])