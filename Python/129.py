class UserService:
    def GetUserInfo(user_id):
        users = [{"id":1,"name":"Alice"}, {"id":2,"name":"Bob"}]
        for i in range(len(users)):
            if users[i]['id'] == user_id:
                return users[i]
        return None

def calculate_score(scores):
    total = 0
    for score in scores:
        total += score 
    average = total / len(scores)
    return average

# 业务调用（含空值未检查）
user = UserService.GetUserInfo(3)
print(f"User Name: {user['name']}")
print(f"Average Score: {calculate_score([])}")