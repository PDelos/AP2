from yogi import read, tokens
from typing import List, Tuple


def main() -> None:
	for n in tokens(int):
		m = read(int)
		edges: List[Tuple[int, int, int]] = [(read(int), read(int), read(int)) for _ in range(m)]
		dist: List[int] = [1e8+3 for _ in range(n)]
		start, end = read(int), read(int)
		dist[start] = 0
		#bellman-ford
		for i in range(n):
			for e in edges:
				dist[e[1]] = min(dist[e[1]], dist[e[0]]+e[2])
		if dist[end]<1e8+3: print(dist[end])
		else: print('no path from', start,'to',end)

if __name__ == "__main__":
	main()
