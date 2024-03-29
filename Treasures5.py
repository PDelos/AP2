from yogi import read
from typing import List
from dataclasses import dataclass

dx: List[int] = [1, 0, -1, 0]
dy: List[int] = [0, -1, 0, 1]

@dataclass
class Point:
	x: float
	y: float

def isValid(x: int, y:int, mapa: List[List[chr]], visited: List[List[bool]]) -> bool:
	n, m = len(mapa), len(mapa[0])
	if x >= n or x < 0: return False
	if y >= m or y < 0: return False
	if mapa[x][y] == "X": return False
	if visited[x][y]: return False
	return True

def bfs(mapa: List[List[chr]]) -> List[int]:
	n, m = len(mapa), len(mapa[0])
	visited: List[List[bool]] = [[False for _ in range(m)] for _ in range(n)]
	dist: List[List[int]] = [[n*m for _ in range(m)] for _ in range(n)]
	q: List[Point] = list()
	r, c = read(int)-1, read(int)-1

	sol: List[int] = list() 
	visited[r][c] = True
	dist[r][c] = 0
	q.append(Point(r,c))
	while q:
		s = q.pop(0)
		if mapa[s.x][s.y] == 't': sol.append(dist[s.x][s.y])
		for i in range(4):
			newX, newY = s.x+dx[i], s.y+dy[i]
			if isValid(newX, newY, mapa, visited):
				visited[newX][newY] = True
				dist[newX][newY] = dist[s.x][s.y]+1
				q.append(Point(newX, newY))
	return sol

def main() -> None:
	n, m = read(int), read(int)
	mapa: List[str] =  [read(str) for _ in range(n)]

	sol = bfs(mapa)
	if len(sol) <= 1: print('we cannot reach two or more treasures')
	else: print('second maximum distance:', sol[-2])


if __name__ == "__main__":
	main()
