//https://leetcode.com/problems/rotting-oranges/description/

class Solution {
    public int orangesRotting(int[][] grid) {
        int mins = 0;

        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[i].length; j++){
                if(grid[i][j] == 1){
                    mins = Math.max(mins, bfs(grid, i, j, 0, new boolean[grid.length][grid[0].length]));
                    if(mins == Integer.MAX_VALUE){
                        return -1;
                    }
                }
            }
        }

        return mins;
    }

    public int bfs(int[][] grid, int i, int j, int count, boolean[][] visited) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[i].length || visited[i][j] || grid[i][j] == 0) {
            return Integer.MAX_VALUE;
        } else if (grid[i][j] == 2) {
            return count;
        }
        
        visited[i][j] = true;

        int minCount = Integer.MAX_VALUE;
        minCount = Math.min(minCount, bfs(grid, i + 1, j, count + 1, visited));
        minCount = Math.min(minCount, bfs(grid, i - 1, j, count + 1, visited));
        minCount = Math.min(minCount, bfs(grid, i, j + 1, count + 1, visited));
        minCount = Math.min(minCount, bfs(grid, i, j - 1, count + 1, visited));

        visited[i][j] = false;

        return minCount;
    }
}
