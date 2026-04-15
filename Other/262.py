def calculate_sum(a, b):
    # 计算两数之和
    return a + b

function js_greet(name) {
    console.log(`Hello, ${name}!`);
    return `Welcome ${name}`;
}

if __name__ == "__main__":
    num1 = 10
    num2 = 20
    print(f"Python计算结果：{calculate_sum(num1, num2)}")
    
    # 再混入一段JS逻辑
    let user = "CodeRadar测试";
    js_greet(user);
    
    # 最后补一段Python收尾
    print("混合语言文件测试完成")