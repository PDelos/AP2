from yogi import read
from typing import List, Dict


def dfs(s: int, adj: List[List[int]], visited: List[int]) -> None:
	if visited[s]: return
	visited[s] = True
	for u in adj[s]: dfs(u, adj, visited)

def main() -> None:
	n = read(int)
	adj: List[List[int]] = [[] for _ in range(n)]
	visited: List[bool] = [False for _ in range(n)]
	dic: Dict[str, int] = dict()
	for i in range(n):
		dic[read(str)] = i


	m = read(int)
	for _ in range(m):
		x, y = read(str), read(str)
		adj[dic[x]].append(dic[y])
		adj[dic[y]].append(dic[x])

	start, end = read(str), read(str)
	dfs(dic[start], adj, visited)
	if visited[dic[end]]: print('yes') 
	else: print('no')

if __name__ == "__main__":
	main()
