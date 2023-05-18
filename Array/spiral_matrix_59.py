'''
59.

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

Example 1:

    Input: n = 3

    Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
    
    Input: n = 1

    Output: [[1]]

1 <= n <= 20

'''


'''
My solution:

start from (0, 0) and go right --> 
    if matrix[i][j] == 0 --> make num --> make a move by current direction
    else --> go along the direction now --> make num
'''

class Solution1(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        current_direction = 'right'
        for num in range(1, n * n + 1):
            if matrix[i][j] == 0:
                matrix[i][j] = num
                current_direction, i, j = move(current_direction, i, j, n, matrix)
            else:
                current_direction, i, j = move(current_direction, i, j, n, matrix)
                matrix[i][j] = num
                current_direction, i, j = move(current_direction, i, j, n, matrix)
        return matrix

def move(current_direction, i, j, n, matrix):
    direction = {'right': 'down', 'down': 'left', 'left': 'up', 'up': 'right'}
    if current_direction == 'right':
        if j < n - 1 and matrix[i][j + 1]==0:
            j += 1
        else:
            current_direction = direction[current_direction]
    if current_direction == 'down':
        if i < n - 1 and matrix[i + 1][j]==0:
                i += 1
        else:
            current_direction = direction[current_direction]
    if current_direction == 'left':
        if j > 0 and matrix[i][j - 1]==0:
            j -= 1
        else:
            current_direction = direction[current_direction]
    if current_direction == 'up':
        if i > 0 and matrix[i - 1][j]==0:
            i -= 1
        else:
            current_direction = direction[current_direction]

    return current_direction, i, j

'''
Make the codes more efficient
'''

class Solution2(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # r, d, l, u
        direction_idx = 0
        i, j = 0, 0

        for num in range(1, n * n + 1):
            matrix[i][j] = num

            next_i = i + directions[direction_idx][0]
            next_j = j + directions[direction_idx][1]

            if (
                next_i < 0
                or next_i >= n
                or next_j < 0
                or next_j >= n
                or matrix[next_i][next_j] != 0
            ):
                direction_idx = (direction_idx + 1) % 4

            i += directions[direction_idx][0]
            j += directions[direction_idx][1]

        return matrix