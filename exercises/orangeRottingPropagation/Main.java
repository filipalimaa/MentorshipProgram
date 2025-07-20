package orangeRottingPropagation;
import java.util.*;

public class Main {

    public static void main(String[] args) {

        OrangeInputs inputReader = new OrangeInputs();
        int[][] matrix = inputReader.readInput();

        OrangeRottingSolver solver = new OrangeRottingSolver();
        int time = solver.timeToRot(matrix);

        System.out.println("Time it takes for all the oranges to rot:" + time);

    }
}