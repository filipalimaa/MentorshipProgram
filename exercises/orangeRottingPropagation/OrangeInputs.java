package orangeRottingPropagation;
import java.util.Scanner;

public class OrangeInputs {

    public int[][] readInput() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Number of rows in the matrix: ");
        int lines = scanner.nextInt();

        System.out.print("Number of columns in the matrix: ");
        int columns = scanner.nextInt();

        int[][] matrix = new int[lines][columns];

        System.out.println("Insert the values of the matrix (0 = empty, 1 = fresf, 2 = rotten):");

        for (int i = 0; i < lines; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print("Value for [" + i + "][" + j + "]: ");
                matrix[i][j] = scanner.nextInt();
            }
        }
        return matrix;
    }
}