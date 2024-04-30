"""
子供のやっていた「[賢くなる探偵パズル 図形 （かんたん）](https://ieben.gakken.jp/s_book/isbn9784053056573/)」
の迷路（初級4のやつ）1回目は普通に解けるが2回目（別の解き方で解いてみよう！）が全く解けないし答えみても書いてないので
そもそも別解ないんじゃねえの？と全探査してみた、結論、別解なんてない。
んんんん？？？？？別の解き方？とは？？



"""

def dfs(grid, row, col, visited, path):
    if grid[row][col] == 3 and len(path) == sum(1 for row in grid for cell in row if cell == 0)+1:
        path.append((row, col))
        return [path]
    
    if grid[row][col] == 1 or grid[row][col] == 3 or (row, col) in visited:
        return []
    
    visited.add((row, col))
    path.append((row, col))
    
    paths = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != 1:
            results = dfs(grid, new_row, new_col, visited, path[:])
            paths.extend(results)
    
    visited.remove((row, col))
    return paths
def find_path(grid):
    start_row, start_col = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                start_row, start_col = i, j
                break
        if start_row is not None:
            break

    results = dfs(grid, start_row, start_col, set(), [])

    if results:
        print(f"Found {len(results)} solutions:")
        for result in results:
            path_str = " ".join(f"{chr(65+col)}{row}" for row, col in result)
            print(path_str)
    else:
        print("No solution found.")

# グリッドの定義
grid = [
    [2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3]
]

find_path(grid)


