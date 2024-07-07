from collections import defaultdict

n = int(input()) 
adj = defaultdict(list)

k = int(input())

def addEdge(u, v):
    adj[u].append(v)
    adj[v].append(u)

def Vertex(u):
    print(*adj[u])

while k != 0:
    each = list(map(int, input().split()))

    if each[0] == 1:
        addEdge(each[1], each[2])
    else:
        Vertex(each[1])

    k -= 1
