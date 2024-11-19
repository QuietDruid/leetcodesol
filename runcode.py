from collections import *
import unittest 
our_list = []
our_dict = {}
our_set = set()
our_tuple = tuple()


class temp:
    def __init__(self):
        self.our_list = []
        self.our_dict = {}
        self.our_set = set()
        self.our_tuple = tuple()

class node:
    def __init__(self, value, depth):
        self.value = value
        self.into = []
        self.out = []
        self.depth = depth
    
    def add_into(self, node):
        self.into.append(node)
    
    def add_out(self, node):
        self.out.append(node)
    
    def __str__(self):
        return str(self.value) + " " + str(self.into) + " " + str(self.out)
    

def dfs():
    pass

def bfs_gate():
    grid =  [[2147483647,-1,0,2147483647], [2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

    ROW, COLS = len(grid), len(grid[0])
    visited = set()
    queue = deque()

    for i in range(ROW):
        for j in range(COLS):
            if grid[i][j] == 0:
                queue.append((i, j))
                visited.add((i, j))
    dist = 0
    while queue:
        for i in range(len(queue)):
            x, y = queue.popleft() # looking at the current node
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # looking up down left right
                nx, ny = x + dx, y + dy # calculating the next node
                if 0 <= nx < ROW and 0 <= ny < COLS and (nx, ny) not in visited and grid[nx][ny] != -1: # checking if next node is valid and not a wall
                    grid[nx][ny] = dist + 1
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        dist += 1

    print(grid)

def longestIncreasingPath():
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    ROW, COLS = len(matrix), len(matrix[0])
    visited = [[0 for _ in range(COLS)] for _ in range(ROW)]
    max_len = 0

    def dfs(matrix, i, j, visited):
        if visited[i][j] != 0:
            return visited[i][j]
        visited[i][j] = 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = i + dx, j + dy
            if 0 <= nx < ROW and 0 <= ny < COLS and matrix[nx][ny] > matrix[i][j]:
                visited[i][j] = max(visited[i][j], dfs(matrix, nx, ny, visited) + 1)
        return visited[i][j]

    for i in range(ROW):
        for j in range(COLS):
            max_len = max(max_len, dfs(matrix, i, j, visited))
    print(max_len)

def findPair(banks: list[int], target:int) -> list[int]:
    visited = {} # value is the key and the index is the valueofdict 
    for i in range(len(banks)):
        if target - banks[i] in visited:
            return [visited[target - banks[i]], i]
        visited[banks[i]] = i

def make_bricks(small, big, goal):
    fives_needed = goal // 5
    # print(fives_needed)
    if fives_needed >= big:
        goal = goal - (big * 5)
    elif fives_needed < big:
        goal =- (fives_needed * 5)
    # print(goal)
    if goal > small:
       
        return False

    return True

class testingTest(unittest.TestCase):

    def testdoesItPass(self):
        self.assertEqual(1, 1)
    
    def testdoesItFail(self):
        self.assertNotEqual(1, 2)

    def testMakeBrick(self):
        # self.assertEqual(make_bricks(3, 1, 8), True)
        self.assertEqual(make_bricks(3, 1, 9), False)
        """ self.assertEqual(make_bricks(3, 2, 10), True)
        self.assertEqual(make_bricks(3, 2, 8), True)
        self.assertEqual(make_bricks(3, 2, 9), False)
        self.assertEqual(make_bricks(6, 1, 11), True)
        self.assertEqual(make_bricks(6, 0, 11), False)
        self.assertEqual(make_bricks(1, 4, 11), True)
        self.assertEqual(make_bricks(0, 3, 10), True)
        self.assertEqual(make_bricks(1, 4, 12), False)
        self.assertEqual(make_bricks(3, 1, 7), True)
        self.assertEqual(make_bricks(1, 1, 7), False)
        self.assertEqual(make_bricks(2, 1, 7), True)
        self.assertEqual(make_bricks(7, 1, 11), True)
        self.assertEqual(make_bricks(7, 1, 8), True)
        self.assertEqual(make_bricks(7, 1, 13), False)
        self.assertEqual(make_bricks(43, 1, 46), True)
        self.assertEqual(make_bricks(40, 1, 46), False)
        self.assertEqual(make_bricks(40, 2, 47), True)
        self.assertEqual(make_bricks(40, 2, 50), True)
        self.assertEqual(make_bricks(40, 2, 52), False)
        self.assertEqual(make_bricks(22, 2, 33), False)
        self.assertEqual(make_bricks(0, 2, 10), True)
        self.assertEqual(make_bricks(1000000, 1000, 1000100), True)
        self.assertEqual(make_bricks(2, 1000000, 100003), False)
        self.assertEqual(make_bricks(20, 0, 19), True)
        self.assertEqual(make_bricks(20, 0, 21), False)
        self.assertEqual(make_bricks(20, 4, 51), False)
        self.assertEqual(make_bricks(20, 4, 39), True) """



if __name__ == '__main__':

    #bfs_gate()

    #longestIncreasingPath()

    
    unittest.main(verbosity=2)

