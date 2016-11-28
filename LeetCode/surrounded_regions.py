from sys import stdout as out
from collections import deque

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # print 'entered solve'
        # out.flush()
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        # print visited
        # out.flush()
        for row in range(len(board)):
            for col in range(len(board[0])):
                # print 'checking postition: ' + str((row, col))
                # print 'visited[position]: ' + str(visited[row][col])
                # out.flush()
                if visited[row][col]:
                    # print 'position has already been visited'
                    # out.flush()
                    continue
                if board[row][col] == 'O':
                    # print 'found O'
                    # out.flush()
                    region = self.BFS(board, visited, (row, col))
                    if region:
                        for point in region:
                            board[point[0]][point[1]] = 'X'

                # print 'visited[row][col] = ' + str(visited[row][col])
                visited[row][col] = True
                # print visited
                # out.flush()
                        
                    
    def BFS(self, board, visited, point):
        # print 'running bfs from point ' + str(point)
        # out.flush()
        region = set()
        q = deque()
        q.append(point)
        
        while len(q):
            curr = q.popleft()
            # print "checking position " + str(curr)
            # out.flush()

            if curr in region:
                # print "current point to check is in the region"
                # out.flush()
                continue
            
            surrounded = True
            if curr[0] - 1 >= 0:
                if board[curr[0] - 1][curr[1]] == 'O':
                    q.append((curr[0] - 1, curr[1]))
            else:
                surrounded = False
            if curr[0] + 1 < len(board):
                if board[curr[0] + 1][curr[1]] == 'O':
                    q.append((point[0] + 1, point[1]))
            else:
                surrounded = False
            if curr[1] - 1 >= 0:
                if board[curr[0]][curr[1] - 1] == 'O': 
                    q.append((curr[0], curr[1] - 1))
            else:
                surrounded = False
            if curr[1] + 1 < len(board[0]):
                if board[curr[0]][curr[1] + 1] == 'O':
                    q.append((curr[0], curr[1] + 1))
            else:
                surrounded = False
            
            if not surrounded:
                return None
                
            region.add(curr)
            visited[curr[0]][curr[1]] = True
        
        return region