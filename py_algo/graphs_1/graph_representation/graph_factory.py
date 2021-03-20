# Handshaking lemma
n = int(input())
degrees = list(map(int, input().split()))
total = sum(degrees)
if total == 2*(n - 1):  # Because tree has n-1 edges where n are the vertices. So based on
    print("Yes")        # on the handshaking lemma we have the 2*EDGES = 2*(n-1).
else:
    print("No")
