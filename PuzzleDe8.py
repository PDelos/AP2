from yogi import read, tokens
from heapq import heappush, heappop
from typing import Dict, List, Tuple, Any, Set


def heuristic(s: str) -> int:
	heuristic_score = 0
	for tile in s:
		tile_idx = s.index(tile)
		goal_idx = "123456780".index(tile)
		tile_i, tile_j = tile_idx // 3, tile_idx % 3
		goal_i, goal_j = goal_idx // 3, goal_idx % 3
		heuristic_score += abs(tile_j-goal_j)+abs(tile_i-goal_i)
	return heuristic_score

def swap_indices(s: str, i: int, j: int) -> str:
    s_lst = list(s)
    s_lst[i], s_lst[j] = s_lst[j], s_lst[i]
    return ''.join(s_lst)

def solve(s: str) -> bool:
    inv_count = sum(s[i] > s[j] and s[i] != "0" and s[j] != "0" for i in range(9) for j in range(i + 1, 9))
    return (inv_count % 2 == 0)


def Astar_search(s:str) -> int:
	f: Dict[str, int] = dict()  # prediction u -> t
	g: Dict[str, int] = dict()  # actual distance from s -> u

	pred: Dict[str,str] = dict()  # parent
	pq: List[Tuple[int, str]] = list()  # priority queue

	g[s] = 0
	f[s] = heuristic(s)
	heappush(pq, (f[s], s))


	moves: Dict[int, List[int]] = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8], 6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}

	while pq:
		u: str = heappop(pq)[1]
		i: int = u.index("0")
		if u == "123456780": 
			return g[u]
		for move in moves[i]:
			v: str = swap_indices(u, i, move)
			gv = g[u] + 1
			if v not in g or gv < g[v]:
				if v in f and (f[v], v) in pq:
					pq.remove((f[v], v))

				g[v] = gv
				f[v] = gv + heuristic(v)
				pred[v] = u
				heappush(pq, (f[v], v))  # new value
	return -1


def main() -> None:
	s: str = "".join([str(read(int)) for _ in range(9)])
	if solve(s): print(Astar_search(s))
	else: print(None)
        
	
if __name__ == "__main__":
    main()
