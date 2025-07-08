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
        int linhas = matrix.length;
        int colunas = matrix[0].length;

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        Queue<position> q = new LinkedList<>();

        for ( int i = 0; i < linhas; i++ ) {
            for ( int j = 0; j < colunas; j++ ) {
                if ( matrix[i][j] == 2 ) {
                    q.add(new position(i,j));
                }
            }
        }
    }
}