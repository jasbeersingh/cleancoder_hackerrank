def solution(n):
    '''
    details here: https://stackoverflow.com/questions/46106209/python-stairstep-dp-solution-understanding
    '''
    ways = [[0 for i in range(n + 1)] for j in range(n + 1)]
    ways[0][0] = 1  # base case

    for max_height in range(1, n + 1):
        for bricks_left in range(0, n + 1):
            ways[max_height][bricks_left] = ways[max_height - 1][bricks_left]
            if bricks_left >= max_height:
                ways[max_height][bricks_left] += ways[max_height - 1][bricks_left - max_height]

    return ways[n][n] - 1