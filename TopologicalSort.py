from yogi import read, tokens
from typing import List
import heapq as hpq


def topoSort(adj: List[List[int]]) -> None:
	inDeg: List[int] = [0 for _ in range(len(adj))]
	topo: List[int] = list()
	cuap: List[int] = list() 

	for u in range(len(adj)):
		for x in adj[u]: inDeg[x] += 1
	for u in range(len(adj)):
		if inDeg[u] == 0: hpq.heappush(cuap, u)

	while cuap:
		s = hpq.heappop(cuap)
		topo.append(s)
		for u in adj[s]:
			inDeg[u] -= 1
			if inDeg[u] == 0: 
				hpq.heappush(cuap, u) 

	for i in range(len(topo)-1): print(topo[i], end=" ")
	print(topo[len(topo)-1])


	


def main() -> None:
	for n in tokens(int):
		m = read(int)
		adj: List[List[int]] =  [list() for _ in range(n)]

		for _ in range(m):
			x, y = read(int), read(int)
			adj[x].append(y)

		topoSort(adj)
	

if __name__ == "__main__":
	main()
