import java.util.LinkedList;
import java.util.Queue;

public class OrangeRottingSolver {

    public int timeToRot(int[][] grade) {

        int m = grade.length;
        int n = grade[0].length;

        Queue<int[]> line = new LinkedList<>();
        int freshOranges = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grade[i][j] == 2) {
                    line.offer(new int[]{i,j});
                } else if (grade[i][j] == 1) {
                    freshOranges++;
                }
            }
        }

        if (freshOranges == 0) return 0;

        int time = 0;
        int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}};

        while (!line.isEmpty()) {
            int size = line.size();

            for (int i = 0; i < size; i++) {
                int[] position = line.poll();
                int x = position[0];
                int y = position[1];

                for (int[] dir : directions) {
                    int newX = x + dir[0];
                    int newY = y + dir[1];

                    if (newX >= 0 && newX < m && newY >= 0 && newY < n && grade[newX][newY] == 1) {
                        grade[newX][newY] = 2;
                        line.offer(new int[]{newX, newY});
                        freshOranges--;
                    }
                }
            }

            time++;
        }
        return freshOranges == 0 ? time -1 : -1;
    }
}