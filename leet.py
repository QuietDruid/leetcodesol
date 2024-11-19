import unittest

def minReorder(n: int, connections: list[list[int]]) -> int:
    edges_to_change = 0
    undirected = {}

    for x in connections:
        if x[0] not in undirected:
            undirected[x[0]] = [x[1]]
        else:
            undirected[x[0]].append(x[1])
        
        if x[1] not in undirected:
            undirected[x[1]] = [x[0]]
        else:
            undirected[x[1]].append(x[0])
     
    visited_node = [False for i in range(n)]
    # print(connections)
    # start at 0 and jump down
    # print(undirected)
    def dfs(node):
        visited_node[node] = True
        # print(undirected[node])
        for x in undirected[node]:
            if not visited_node[x]:
                
                temp = [x, node]
                # print(temp)
                if temp not in connections:
                    # print(temp)
                    nonlocal edges_to_change
                    edges_to_change = edges_to_change + 1
                dfs(x)
        return
    dfs(0)

    return edges_to_change

def longestPath(parent: list[int], s: str) -> int:
        '''
        In: parent arr and the string
        out: longest no pair

        starting at the root, def at -1, add it to the dfs queue

        while the dfs queue active
            look at the children, 
                if they share the same letter add it to the DFS queue
                else:  continue the dfs, count, check if thats the biggest
    
        '''

        directed = {0:[]}
        # N work
        for i in range(1, len(parent)):
            if parent[i] not in directed:
                directed[parent[i]] = [i]
            else:
                directed[parent[i]].append(i)
            
            if i not in directed:
                directed[i] = []
        
        # print(directed)
        visited = False * len(parent)
        longest = 0
        first = 1
        fakequeue = []
        fakequeue.append(0)

        def dfs(node, count):
            for x in directed[node]:
                if s[x] == s[node]:
                    fakequeue.append(x)
                else:
                    dfs(x, count + 1)
            nonlocal longest
            longest = max(longest, count)
            return

        while fakequeue:
            node = fakequeue.pop()
            dfs(node, first)
        
        return longest

def longestPathSolution(parent: list[int], s: str) -> int:
    childCount = [0] * len(parent)

    for i in range(1, len(parent)):
        childCount[parent[i]] += 1

    longestChain = [[0] * 2 for _ in range(len(parent))]
    # print(longestChain)
    longest = 1
    queue = []

    for i in range(len(parent)):
        if childCount[i] == 0 and i != 0:
            queue.append(i)
            longestChain[i][0] = 1
    
    while queue:
        node = queue.pop()
        curParent = parent[node]

        
        nodeLongest = longestChain[node][0]

        if s[node] != s[curParent]:
            if nodeLongest > longestChain[curParent][0]:
                longestChain[curParent][1] = longestChain[curParent][0]
                longestChain[curParent][0] = nodeLongest
            elif nodeLongest > longestChain[curParent][1]:
                longestChain[curParent][1] = nodeLongest
        
        longest = max(longest, longestChain[curParent][0] + longestChain[curParent][1])

        childCount[curParent] -= 1

        if childCount[curParent] == 0 and curParent != 0:
            longestChain[curParent][0] += 1
            queue.append(curParent)

    return longest

def lengthOfLongestSubstring( s: str) -> int:
        left, right = 0, 0
        charSeen = []
        longest = 1

        if len(s) == 0:
            return 0

        charSeen.append(s[0])
        
        for i in range(1, len(s)):
           
            if s[i] not in charSeen:
                right = i
                charSeen.append(s[i])
                longest = max(longest, len(charSeen))
            elif s[i] in charSeen:
                right = i
                temp_indx = charSeen.index(s[i])
                longest = max(longest, len(charSeen))
                # print(temp_indx)
                left += temp_indx + 1
                charSeen.append(s[i])
                charSeen = charSeen[temp_indx + 1:]
                # print(charSeen)
        # print(left, right)
        return longest

def numIslands(grid: list[list[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        islands = 0

        def bfs(i, j):
            queue = []
            queue.append((i, j))

            while queue:
                x, y = queue.pop(0)
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == "1":
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    # print(i, j)
                    visited[i][j] = True
                    bfs(i, j)
                    # print(visited)
                    islands += 1
        return islands
        print(visited)

class TestLeet(unittest.TestCase):
    def testPassing(self):
        self.assertEqual(1, 1)

    def testMinReorder1(self):
        self.assertEqual(minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]), 3)
    
    def testLongestPathAdj1(self):
        self.assertEqual(longestPathSolution([-1,0,0,1,1,3,3], "leetcode"), 4)

    def testLongestPathAdj2(self):
        self.assertEqual(longestPathSolution([-1,0,0,1,1,2], "abacbe"), 3)

    def testLongestPathAdj3(self):
        self.assertEqual(longestPathSolution([-1,0,0,0], "aabc"), 3)

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    # print(minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
    # print(longestPath([-1,0,0,1,1,2], "abacbe"))
    # print(longestPathSolution([-1,0,0,0], "aabc"))
    # print(lengthOfLongestSubstring("abcabcbb"))
    # print(lengthOfLongestSubstring("bbbbbbbbbbbb"))
    # print(lengthOfLongestSubstring("pwwkew"))
    print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]))