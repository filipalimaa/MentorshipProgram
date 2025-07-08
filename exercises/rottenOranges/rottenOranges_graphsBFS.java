import java.util.*;

public class rottenOranges {

    static class position {
        int line, column;

        position(int l,  int c) {
            this.line = l;
            this.column = c;
        }
    }

    public static void rotten(int[][] matrix) {
        int lines = matrix.length;
        int columns = matrix[0].length;

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        Queue<position> q = new LinkedList<>();

        for ( int i = 0; i < lines; i++ ) {
            for ( int j = 0; j < columns; j++ ) {
                if ( matrix[i][j] == 2 ) {
                    q.add(new position(i,j));
                }
            }
        }

        while ( !q.isEmpty() ) {
            position p = q.poll();
            for ( int i = 0; i < 4; i++ ) {
                int newLine = p.line + dx[i];
                int newColumn = p.column + dy[i];

                if (newLine >= 0 && newLine < lines && newColumn >= 0 && newColumn < columns &&
                matrix[newLine][newColumn] == 1 ) {
                    matrix[newLine][newColumn] = 2;
                    q.add(new position(newLine,newColumn));
                }
            }
        }
    }
}