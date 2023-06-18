from yogi import read, tokens
from heapq import heappush, heappop
from typing import List, Tuple, Dict
# S'HA DE FER SERVIR CODON PER AC
dx: List[int] = [-1, 1, 0, 0]
dy: List[int] = [0, 0, -1, 1]

def h(src: Tuple[int, int], dst: Tuple[int, int]) -> int:
    """Heuristic to estimate dist from src to dst"""
    return abs(src[0] - dst[0]) + abs(src[1] - dst[1])

def valid(p: Tuple[int, int], block: List[Tuple[int, int]]) -> bool:
    """Check if there is a blockade"""
    return True if p not in block else False

def Astar_search(s: Tuple[int, int], t: Tuple[int, int], block: List[Tuple[int, int]]) -> int:
    f: Dict[Tuple[int, int], int] = dict()  # prediction u -> t
    g: Dict[Tuple[int, int], int] = dict()  # actual distance from s -> u

    pred: Dict[Tuple[int, int], Tuple[int, int]] = dict()  # parent
    pq: List[Tuple[int, Tuple[int, int]]] = list()  # priority queue

    g[s] = 0
    f[s] = h(s, t)
    heappush(pq, (f[s], s))

    while pq:
        u: Tuple[int, int] = heappop(pq)[1]
        if u == t:
            return g[u]
        for i in range(4):
            v:  Tuple[int, int] = (u[0] + dx[i], u[1] + dy[i])
            if not valid(v, block):
                continue
            gv = g[u] + 1
            if v not in g or gv < g[v]:
                if v in f:
                    prev = (f[v], v)
                    if prev in pq:
                        pq.remove(prev)

                g[v] = gv
                f[v] = gv + h(v, t)
                pred[v] = u
                heappush(pq, (f[v], v))  # new value
    return -1


def main() -> None:
    start: Tuple[int, int] = (read(int), read(int))
    end: Tuple[int, int] = (read(int), read(int))
    block: List[Tuple[int, int]] = [(x, read(int)) for x in tokens(int)]

    print(Astar_search(start, end, block))


if __name__ == "__main__":
    main()
