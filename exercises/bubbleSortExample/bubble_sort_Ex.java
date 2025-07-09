public class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {

            for (int j = 0; j < n - i - 1; j++) {

                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
    
        public static void main(String[] args) {
        int[] numeros = {5, 3, 4, 1};

        System.out.println("Antes da ordenação:");
        printArray(numeros);

        bubbleSort(numeros);

        System.out.println("Depois da ordenação:");
        printArray(numeros);
    }
}