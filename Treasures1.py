from yogi import read
from typing import List

dx: List[int] = [1, 0, -1, 0]
dy: List[int] = [0, -1, 0, 1]


def isValid(x: int, y:int, mapa: List[List[chr]], visited: List[List[bool]]) -> bool:
	n, m = len(mapa), len(mapa[0])
	if x >= n or x < 0: return False
	if y >= m or y < 0: return False
	if mapa[x][y] == "X": return False
	if visited[x][y]: return False
	return True

def dfs(x: int, y:int, mapa: List[List[chr]], visited: List[List[bool]]) -> bool:
	if mapa[x][y] == "t": return True
	visited[x][y] = True
	for i in range(4):
		if isValid(x+dx[i], y+dy[i], mapa, visited):
			if dfs(x+dx[i], y+dy[i], mapa, visited):
				return True

	return False

def main() -> None:
	n, m = read(int), read(int)
	visited: List[List[bool]] = [[False for _ in range(m)] for _ in range(n)]
	mapa: List[str] =  [read(str) for _ in range(n)]
	r, c = read(int)-1, read(int)-1
	visited[r][c] = True
	if dfs(r, c, mapa, visited): print("yes")
	else: print("no")

if __name__ == "__main__":
	main()
