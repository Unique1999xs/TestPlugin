// public class Test132 { 	
// 	public static void main(String[] args) { 		
// 		System.out.println("test"); 	
// 	} 
// }

/**
 * 133
 */
// public class Test132 {
//     public static void main(String[] args) {
//         int a = 10
//         System.out.println(a);
//     }
// }

/**
 * 134
 */
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Test132 {
    private static final Logger logger = LoggerFactory.getLogger(Test132.class);
    private static final int DEFAULT_USER_AGE = 20;

    public static void main(String[] args) {
        int userAge = DEFAULT_USER_AGE;
        logger.info("用户年龄: {}", userAge);}
}