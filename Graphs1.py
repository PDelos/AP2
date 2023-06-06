from yogi import read
from typing import List


def dfs(s: int, adj: List[List[int]], visited: List[int]) -> None:
	if visited[s]: return
	visited[s] = True
	for u in adj[s]: dfs(u, adj, visited)

def main() -> None:
	n, m = read(int), read(int)
	adj: List[List[int]] = [[] for _ in range(n)]
	visited: List[bool] = [False for _ in range(n)]
	for _ in range(m):
		x, y = read(int), read(int)
		adj[x].append(y)

	start, end = read(int), read(int)
	dfs(start, adj, visited)
	if visited[end]: print('yes') 
	else: print('no')

if __name__ == "__main__":
	main()
