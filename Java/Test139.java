// public class Test139 {
//     public static int add1(int a, int b) {
//         int sum = a + b;
//         return sum;
//     }

//     public static int add2(int x, int y) {
//         int sum = x + y;
//         return sum;
//     }

//     public static void main(String[] args) {
//         System.out.println(add1(1, 2));
//         System.out.println(add2(3, 4));
//     }
// }

public class Test139 {
    // 定义常量替代魔法数字，统一业务语义
    private static final int PARAM_A = 1;
    private static final int PARAM_B = 2;
    private static final int PARAM_X = 3;
    private static final int PARAM_Y = 4;

    // 仅保留一个add方法，消除重复代码
    public static int add(int a, int b) {
        // 处理整数溢出：Java 8+ 用Math.addExact，溢出直接抛出ArithmeticException
        return Math.addExact(a, b);
    }

    public static void main(String[] args) {
        // 用日志框架替代System.out，符合生产规范（示例用SLF4J，实际项目按需引入）
        // org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(Test139.class);
        // logger.info("add1结果: {}", add(PARAM_A, PARAM_B));
        // logger.info("add2结果: {}", add(PARAM_X, PARAM_Y));

        // 若暂不引入日志框架，可保留打印，但建议仅用于测试
        System.out.println(add(PARAM_A, PARAM_B));
        System.out.println(add(PARAM_X, PARAM_Y));
    }
}