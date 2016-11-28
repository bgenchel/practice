# For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example 1:

# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

#         0
#         |
#         1
#        / \
#       2   3
# return [1]

# Example 2:

# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# return [3, 4]

# Show Hint 
# Note:

# (1) According to the definition of tree on Wikipedia: "a tree is an undirected
# graph in which any two vertices are connected by exactly one path. In other 
# words, any connected graph without simple cycles is a tree."

# (2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        edge_list = []
        for _ in range(n): edge_list.append([])
        for edge in edges:
            edge_list[edge[0]].append(edge[1])
            edge_list[edge[1]].append(edge[0])

        heights = [None]*n
        min_height = float('inf')
        for i in range(n):
            heights[i] = self.get_height(-1, i, edge_list)
            if heights[i] < min_height:
                min_height = heights[i]
        
        sol = []
        for i in range(n):
            if heights[i] == min_height:
                sol.append(i)
        
        return sol
        
    def get_height(self, source, curr, edge_list):
        if (len(edge_list[curr]) == 1) and (curr in edge_list[curr]):
            return 0
        
        max_height = -float('inf')
        for i in edge_list[curr]:
            if i == source:
                continue

            h = self.get_height(curr, i, edge_list)
            if h > max_height:
                max_height = h
         
        return max_height + 1

if __name__ == '__main__':
    s = Solution()
    edges = [[1, 0], [1, 2], [1, 3]]
    print s.findMinHeightTrees(4, edges)
