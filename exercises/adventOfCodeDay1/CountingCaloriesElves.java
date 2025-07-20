import java.util.*;

public class CountingCaloriesElves {

    public static void main(String[] args) {
        String[] input = {
                "1000", "2000", "3000", "",
                "4000", "",
                "5000", "6000", "",
                "7000", "8000", "9000", "",
                "10000"
        };

        int maxCalories = 0;
        int currentTotal = 0;

        for (String line : input) {
            if (line.isEmpty()) {
                if (currentTotal > maxCalories) {
                    maxCalories = currentTotal;
                }
                currentTotal = 0;
            } else {
                currentTotal += Integer.parseInt(line);
            }
        }

        if (currentTotal > maxCalories) {
            maxCalories = currentTotal;
        }

        System.out.println("The Elf who carries the most calories has them: " + maxCalories);
    }
}