#!/bin/python3

class Solution:
    
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        edges_to_change = 0
        modified_list = [x.copy() for x in connections]

        visited_node = [False for i in range(n)]

        for x in modified_list:
            x.sort()
        modified_list.sort()

        # print(modified_list)
        # print(connections)

        for x in modified_list:
            if x[0] == 0:
                edges_to_change += self.dfs(x[1], modified_list, connections)
                temp = [x[1], x[0]]
                # print(temp)
                if temp not in connections:
                    # print(str(x[1]) + "->" + str(x[0]))
                    edges_to_change += 1
                    # print(edges_to_change)
        return edges_to_change

    def dfs(self, node, modified_list, connections) -> int:
        tempNum = 0
        for x in modified_list:
            if x[0] == node:
                tempNum += self.dfs(x[1], modified_list, connections)
                temp = [x[1], x[0]]
                # print(temp)
                if temp not in connections:
                    return 1 + tempNum
        return 0 + tempNum


testing = Solution()


print(testing.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
