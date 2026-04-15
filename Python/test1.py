import random

def guess_num():
    random_num = random.randint(1, 100)
    count = 1
    print(random_num)
    while True:
        num = int(input("请输入一个1-100的数字："))
        if num > 100 or num < 1:
            print("数字范围为1-100")
        else:
            if num > random_num:
                print("你的数字猜大了")
                count += 1
            elif num < random_num:
                print("你的数字猜小了")
                count += 1
            else:
                print(f"猜对啦，一共猜了{count}次")
                break

if __name__ == "__main__":
    guess_num()


