# AIM: To implement & simulate Distance Vector Routing algorithm.

class Rtr:
    def __init__(self, name):
        self.name = name
        self.nbrs = {}
        self.dv = {self: (0, self)}  # Distance to itself is zero, next hop is itself

    def add_nbr(self, nbr, cost):
        self.nbrs[nbr] = cost
        self.dv[nbr] = (cost, nbr)

    def update_dv(self):
        updated = False
        for nbr in self.nbrs:
            for dest, (dist, _) in nbr.dv.items():
                new_cost = self.nbrs[nbr] + dist
                if dest not in self.dv or self.dv[dest][0] > new_cost:
                    self.dv[dest] = (new_cost, nbr)
                    updated = True
        return updated

    def __str__(self):
        table = [f"{dest.name:<10}{dist:<10}{('-' if dest == next_hop else next_hop.name):<10}"
                 for dest, (dist, next_hop) in self.dv.items()]
        return f"Routing Table of {self.name}:\n{'Destination':<10}{'Distance':<10}{'Next Hop':<10}\n" + "\n".join(table) + "\n"

def create_rtrs(n, adj_matrix):
    rtrs = [Rtr(str(i + 1)) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != 99 and i != j:
                rtrs[i].add_nbr(rtrs[j], adj_matrix[i][j])
    return rtrs

n = int(input("Enter number of nodes: "))
adj_matrix = [list(map(int, input().split())) for _ in range(n)]
rtrs = create_rtrs(n, adj_matrix)

for i in range(5):
    print(f"Iteration {i+1}\n")
    updates = any(rtr.update_dv() for rtr in rtrs)
    for r in rtrs: print(r)
    if not updates: break

print("Final Distance Vectors:\n")
for r in rtrs: print(r)

'''
_____________________________________________________
output:
Enter the number of nodes: 5
Enter the adjacency matrix (use 99 for no direct connection):
0 5 2 3 99
5 0 4 99 3
2 4 0 99 4
3 99 99 0 99
99 3 4 99 0

Iteration 1

Routing Table of 1:
Destination    Distance  Next Hop  
1              0         -         
2              5         -         
3              2         -         
4              3         -         
5              6         3         

Routing Table of 2:
Destination    Distance  Next Hop  
2              0         -         
1              5         -         
3              4         -         
5              3         -         
4              8         1         

Routing Table of 3:
Destination    Distance  Next Hop  
3              0         -         
1              2         -         
2              4         -         
5              4         -         
4              5         1         

Routing Table of 4:
Destination    Distance  Next Hop  
4              0         -         
1              3         -         
2              8         1         
3              5         1         
5              9         1         

Routing Table of 5:
Destination    Distance  Next Hop  
5              0         -         
2              3         -         
3              4         -         
1              6         3         
4              9         3         

Iteration 2

Routing Table of 1:
Destination    Distance  Next Hop  
1              0         -         
2              5         -         
3              2         -         
4              3         -         
5              6         3         

Routing Table of 2:
Destination    Distance  Next Hop  
2              0         -         
1              5         -         
3              4         -         
5              3         -         
4              8         1         

Routing Table of 3:
Destination    Distance  Next Hop  
3              0         -         
1              2         -         
2              4         -         
5              4         -         
4              5         1         

Routing Table of 4:
Destination    Distance  Next Hop  
4              0         -         
1              3         -         
2              8         1         
3              5         1         
5              9         1         

Routing Table of 5:
Destination    Distance  Next Hop  
5              0         -         
2              3         -         
3              4         -         
1              6         3         
4              9         3         

Final Distance Vectors:

Routing Table of 1:
Destination    Distance  Next Hop  
1              0         -         
2              5         -         
3              2         -         
4              3         -         
5              6         3         

Routing Table of 2:
Destination    Distance  Next Hop  
2              0         -         
1              5         -         
3              4         -         
5              3         -         
4              8         1         

Routing Table of 3:
Destination    Distance  Next Hop  
3              0         -         
1              2         -         
2              4         -         
5              4         -         
4              5         1         

Routing Table of 4:
Destination    Distance  Next Hop  
4              0         -         
1              3         -         
2              8         1         
3              5         1         
5              9         1         

Routing Table of 5:
Destination    Distance  Next Hop  
5              0         -         
2              3         -         
3              4         -         
1              6         3         
4              9         3         
'''
