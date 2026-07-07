class Solution {
    public int orangesRotting(int[][] grid) {
        //setup queue
        //setup freshcount

        //iterate find all rotting oranges and add their index to queue
        //count fresh oranges

        //while queue is not empty, get size, iterate
        //we check neighbors (check bounds)
        //if fresh orange we rot it, add it to the queue and reduce freshcount

        //finally we return -1 if freshcount > 0 or the minutes.
        Queue<int[]> queue = new LinkedList<>();
        int freshcount = 0; 

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) freshcount++;
                if (grid[i][j] == 2) queue.add(new int[]{i, j});
            }
        }

        int minutes = 0;
        int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}}; //directions

        while (!queue.isEmpty() && freshcount > 0) { //bfs per level

            int size = queue.size();

            for (int i = 0; i < size; i++) {

                int[] orange = queue.poll();//get rotted orange

                for (int[] d : dirs) { //for every direction

                    int nr = orange[0] + d[0];
                    int nc = orange[1] + d[1];

                    if (nr >= 0 && nr < grid.length && nc >= 0 && nc < grid[0].length
                            && grid[nr][nc] == 1) {

                        grid[nr][nc] = 2; //rot orange
                        freshcount--; //decrese count
                        queue.add(new int[]{nr, nc}); //add to queue
                    }
                }
            }
            minutes++;//increase minute for next while loop iteration
        }

        return freshcount == 0 ? minutes : -1; //if fresh is 0 return minutes if not -1
    }
}