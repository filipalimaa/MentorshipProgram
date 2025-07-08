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

        System.out.println("Final result: ");
        for ( int i = 0; i < lines; i++ ) {
            for ( int j = 0; j < columns; j++ ) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of rows and columns of rotten:");
        int rows = sc.nextInt();
        System.out.println("Enter number of columns of rotten:");
        int columns = sc.nextInt();

        int[][] matrix = new int[rows][columns];

        System.out.println("Enter rotten matrix (0 = empty, 1 = good orange, 2 = rotten orange):");
        for ( int i = 0; i < rows; i++ ) {
            for ( int j = 0; j < columns; j++ ) {
                matrix[i][j] = sc.nextInt();
            }
        }

        rotten(matrix);
        sc.close();
    }
}