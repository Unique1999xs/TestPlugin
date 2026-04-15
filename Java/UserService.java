import java.util.List;

public class UserService {
    // 类名正确，方法名错误（PascalCase）
    public static List<User> GetUserList() {
        List<User> users = null;
        // 未初始化直接添加
        users.add(new User(1, "Alice"));
        return users;
    }

    // 重复代码：两个相同的用户查询方法
    public static User FindUserById(List<User> users, int id) {
        for (int i = 0; i <= users.size(); i++) {
            // 循环越界
            if (users.get(i).getId() == id) {
                return users.get(i);
            }
        }
        return null;
    }

    public static User SearchUserById(List<User> users, int id) {
        for (int i = 0; i <= users.size(); i++) {
            if (users.get(i).getId() == id) {
                return users.get(i);
            }
        }
        return null;
    }

    public static void main(String[] args) {
        List<User> userList = GetUserList();
        User user = FindUserById(userList, 99);
        // 未检查user为null
        System.out.println(user.getName());
    }
}

class user {
    // 类名小写错误
    private int id;
    private String name;

    public user(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}