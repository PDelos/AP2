from yogi import read, tokens
from typing import List, Tuple

def bfs(x: int, adj: List[List[int]], color: List[int]) -> bool:
	n = len(adj)
	q: List[int] = list()

	color[x]=1
	q.append(x)
	while q:
		s = q.pop(0)
		for u in adj[s]:
			if color[u] == -1: 
				color[u] = 1-color[s]
				q.append(u)
			elif color[s] == color[u]: 
				return False
	return True



def main() -> None:
	for n in tokens(int):
		m = read(int)
		adj: List[List[int]] = [list() for _ in range(n)]
		color: List[int] = [-1 for _ in range(n)]

		for _ in range(m):
			x, y = read(int), read(int)
			adj[x].append(y)
			adj[y].append(x)

		sol = "yes"
		for node in range(n):
			if color[node] == -1 and not bfs(node, adj, color): 
					sol = "no"
		print(sol)

if __name__ == "__main__":
	main()
