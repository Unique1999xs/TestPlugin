public class Test136 {
    // 定义常量替代魔法数字，提升可读性和可维护性
    private static final int ARRAY_ELEMENT_ONE = 1;
    private static final int ARRAY_ELEMENT_TWO = 2;
    private static final int ARRAY_ELEMENT_THREE = 3;
    // 同时用常量定义数组长度和合法索引，避免越界
    private static final int VALID_INDEX_THREE = 3;

    public static void main(String[] args) {
        // 用常量初始化数组，消除魔法数字
        int[] arr = {ARRAY_ELEMENT_ONE, ARRAY_ELEMENT_TWO, ARRAY_ELEMENT_THREE};
        // 数组越界
        System.out.println(arr[VALID_INDEX_THREE]);
    }
}