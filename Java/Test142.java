// import java.sql.*;

// public class Test142 {
//     public static void main(String[] args) {
//         String username = "admin";
//         String sql = "SELECT * FROM users WHERE username = '" + username + "'";
//         // 未使用PreparedStatement
//     }
// }

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Test142 {
    public static void main(String[] args) {
        String username = "admin";

        // 正确写法：使用 ? 占位符（防SQL注入）
        String sql = "SELECT * FROM users WHERE username = ?";

        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;

        try {
            conn = DriverManager.getConnection("url", "user", "pass");
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, username);
            rs = pstmt.executeQuery();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // 关闭资源 必须写！
            try {
                if (rs != null)
                    rs.close();
                if (pstmt != null)
                    pstmt.close();
                if (conn != null)
                    conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}