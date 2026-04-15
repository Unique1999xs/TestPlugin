public class Test138 {
    private static final int TARGET_NUMBER = 3;

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        boolean found = false;

        // 👇 只保留这个【多余的双重循环】BUG
        // 其他所有问题全部优化完成
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] == TARGET_NUMBER) {
                    found = true;
                    break; 
                }
            }
        }

        System.out.println(found);
    }
}