from yogi import read, tokens
from typing import List, Tuple

def dfs1(s: int, adj: List[List[int]], visited: List[int], stack: List[int]) -> None:
	if visited[s]: return
	visited[s] = True
	for u in adj[s]: dfs1(u, adj, visited, stack)
	stack.append(s)

def dfs2(s: int, adj: List[List[int]], visited: List[int]) -> None:
	if visited[s]: return
	visited[s] = True
	for u in adj[s]: dfs2(u, adj, visited)

def transpose(adj: List[List[int]]) -> List[List[int]]:
    g: List[List[int]] = [list() for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in adj[i]: g[j].append(i)
    return g


def main() -> None:
	t = read(int)
	for i in range(t):
		n, m = read(int), read(int)
		adj: List[List[int]] = [list() for _ in range(n)]
		for _ in range(m):
			x, y = read(int), read(int)
			adj[x].append(y)

		visited: List[bool] = [False for _ in range(n)]
		stack: List[int] = list() 
		for node in range(n):
			if not visited[node]:
				dfs1(node, adj, visited, stack)

		
		numComp = 0
		visited: List[bool] = [False for _ in range(n)]
		adj = transpose(adj)
		while stack:
			node = stack.pop()
			if not visited[node]:
				dfs2(node, adj, visited)
				numComp+=1
		print("Graph #", i+1, " has ", numComp, " strongly connected component(s).", sep="")


if __name__ == "__main__":
	main()
