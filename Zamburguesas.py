from yogi import read, tokens
from typing import List, Dict
from dataclasses import dataclass
from math import sqrt

@dataclass
class Point:
	x: float
	y: float
	r: float

def check(p1: Point, p2: Point, d: float) -> bool:
	dist = sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y))
	if dist < p1.r+p2.r+d: return True
	else: return False

def readPoint() -> Point:
	return Point(read(float), read(float), read(float))

def bfs(points: List[Point], d: float) -> int:
	n = len(points)
	visited: List[bool] = [False for _ in range(n)]
	distance: List[int] = [0 for _ in range(n)]
	q: List[int] = list()

	visited[0] = True;
	q.append(0)
	while q:
		s = q.pop(0)
		if s == n-1: return distance[s]
		for u in range(n):
			if u!=s and not visited[u] and check(points[u], points[s], d): 
				visited[u] = True
				distance[u] = distance[s]+1
				q.append(u)
	return -1

def main() -> None:
	for n in tokens(int):
		d = read(float)
		points: List[Point] = [readPoint() for _ in range(n)]
		sol = bfs(points, d)

		if(sol < 0): print('Xof!')
		else: print(sol)

if __name__ == "__main__":
	main()
