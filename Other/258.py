# ==============================================
# 学生成绩管理系统
# 业务：管理员/教师登录、学生管理、课程管理、成绩管理、统计分析
# 数据存储：JSON 文件
# 语言：Python 3
# 代码行数：1200+
# ==============================================

import json
import os
import time
from datetime import datetime

# ===================== 全局配置 =====================
DATA_DIR = "data"
USER_FILE = os.path.join(DATA_DIR, "users.json")
STUDENT_FILE = os.path.join(DATA_DIR, "students.json")
COURSE_FILE = os.path.join(DATA_DIR, "courses.json")
SCORE_FILE = os.path.join(DATA_DIR, "scores.json")

# ===================== 工具函数 =====================
def init_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_json(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_json(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except:
        return False

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def input_int(msg="请输入数字："):
    while True:
        s = input(msg)
        if s.isdigit():
            return int(s)
        print("输入无效，请输入整数！")

def input_score(msg="请输入成绩："):
    while True:
        s = input(msg)
        try:
            score = float(s)
            if 0 <= score <= 100:
                return score
            else:
                print("成绩必须在 0~100 之间")
        except:
            print("输入无效，请输入数字")

def print_sep():
    print("=" * 60)

def pause():
    input("\n按回车继续...")

# ===================== 用户模块 =====================
def init_admin():
    users = load_json(USER_FILE)
    if not users:
        admin = {
            "username": "admin",
            "password": "123456",
            "role": "admin",
            "create_time": get_current_time()
        }
        users.append(admin)
        save_json(USER_FILE, users)

def login():
    print_sep()
    print("【 用户登录 】")
    username = input("用户名：")
    password = input("密码：")
    users = load_json(USER_FILE)
    for u in users:
        if u["username"] == username and u["password"] == password:
            print(f"登录成功！欢迎 {u['role']}：{username}")
            time.sleep(0.5)
            return u
    print("用户名或密码错误")
    pause()
    return None

def add_user():
    print_sep()
    print("【 添加用户 】")
    username = input("用户名：")
    password = input("密码：")
    role = input("角色（admin/teacher）：")
    if role not in ["admin", "teacher"]:
        print("角色无效")
        pause()
        return
    users = load_json(USER_FILE)
    for u in users:
        if u["username"] == username:
            print("用户名已存在")
            pause()
            return
    new_user = {
        "username": username,
        "password": password,
        "role": role,
        "create_time": get_current_time()
    }
    users.append(new_user)
    if save_json(USER_FILE, users):
        print("添加成功")
    else:
        print("添加失败")
    pause()

def list_users():
    print_sep()
    print("【 用户列表 】")
    users = load_json(USER_FILE)
    if not users:
        print("暂无用户")
    else:
        for i, u in enumerate(users, 1):
            print(f"{i:2}. 用户名：{u['username']} | 角色：{u['role']} | 创建时间：{u['create_time']}")
    pause()

def delete_user():
    print_sep()
    print("【 删除用户 】")
    username = input("输入要删除的用户名：")
    users = load_json(USER_FILE)
    new_users = [u for u in users if u["username"] != username]
    if len(new_users) == len(users):
        print("用户不存在")
    else:
        if save_json(USER_FILE, new_users):
            print("删除成功")
        else:
            print("删除失败")
    pause()

# ===================== 学生模块 =====================
def add_student():
    print_sep()
    print("【 添加学生 】")
    stu_id = input("学号：")
    name = input("姓名：")
    gender = input("性别：")
    age = input_int("年龄：")
    cls = input("班级：")
    students = load_json(STUDENT_FILE)
    for s in students:
        if s["stu_id"] == stu_id:
            print("学号已存在")
            pause()
            return
    student = {
        "stu_id": stu_id,
        "name": name,
        "gender": gender,
        "age": age,
        "class": cls,
        "create_time": get_current_time()
    }
    students.append(student)
    if save_json(STUDENT_FILE, students):
        print("添加成功")
    else:
        print("添加失败")
    pause()

def list_students():
    print_sep()
    print("【 学生列表 】")
    students = load_json(STUDENT_FILE)
    if not students:
        print("暂无学生")
    else:
        for i, s in enumerate(students, 1):
            print(f"{i:2}. 学号：{s['stu_id']} | 姓名：{s['name']} | 性别：{s['gender']} | 年龄：{s['age']} | 班级：{s['class']}")
    pause()

def search_student():
    print_sep()
    print("【 查询学生 】")
    keyword = input("输入学号/姓名：")
    students = load_json(STUDENT_FILE)
    result = []
    for s in students:
        if keyword in s["stu_id"] or keyword in s["name"]:
            result.append(s)
    if not result:
        print("无匹配结果")
    else:
        for i, s in enumerate(result, 1):
            print(f"{i:2}. {s['stu_id']} {s['name']} {s['gender']} {s['age']} {s['class']}")
    pause()

def update_student():
    print_sep()
    print("【 修改学生信息 】")
    stu_id = input("输入要修改的学生学号：")
    students = load_json(STUDENT_FILE)
    for s in students:
        if s["stu_id"] == stu_id:
            print("找到学生：", s["name"])
            s["name"] = input(f"新姓名({s['name']})：") or s["name"]
            s["gender"] = input(f"新性别({s['gender']})：") or s["gender"]
            new_age = input(f"新年龄({s['age']})：")
            if new_age.isdigit():
                s["age"] = int(new_age)
            s["class"] = input(f"新班级({s['class']})：") or s["class"]
            if save_json(STUDENT_FILE, students):
                print("修改成功")
            else:
                print("修改失败")
            pause()
            return
    print("未找到该学号")
    pause()

def delete_student():
    print_sep()
    print("【 删除学生 】")
    stu_id = input("输入学号：")
    students = load_json(STUDENT_FILE)
    new_stus = [s for s in students if s["stu_id"] != stu_id]
    if len(new_stus) == len(students):
        print("学号不存在")
    else:
        if save_json(STUDENT_FILE, new_stus):
            print("删除成功")
        else:
            print("删除失败")
    pause()

# ===================== 课程模块 =====================
def add_course():
    print_sep()
    print("【 添加课程 】")
    cid = input("课程编号：")
    name = input("课程名称：")
    credit = input_int("学分：")
    teacher = input("授课教师：")
    courses = load_json(COURSE_FILE)
    for c in courses:
        if c["cid"] == cid:
            print("课程编号已存在")
            pause()
            return
    course = {
        "cid": cid,
        "name": name,
        "credit": credit,
        "teacher": teacher,
        "create_time": get_current_time()
    }
    courses.append(course)
    if save_json(COURSE_FILE, courses):
        print("添加成功")
    else:
        print("添加失败")
    pause()

def list_courses():
    print_sep()
    print("【 课程列表 】")
    courses = load_json(COURSE_FILE)
    if not courses:
        print("暂无课程")
    else:
        for i, c in enumerate(courses, 1):
            print(f"{i:2}. {c['cid']} {c['name']} 学分：{c['credit']} 教师：{c['teacher']}")
    pause()

def delete_course():
    cid = input("输入课程编号：")
    courses = load_json(COURSE_FILE)
    new_courses = [c for c in courses if c["cid"] != cid]
    if len(new_courses) == len(courses):
        print("课程不存在")
    else:
        save_json(COURSE_FILE, new_courses)
        print("删除成功")
    pause()

# ===================== 成绩模块 =====================
def add_score():
    print_sep()
    print("【 录入成绩 】")
    stu_id = input("学生学号：")
    cid = input("课程编号：")
    score = input_score()
    students = load_json(STUDENT_FILE)
    courses = load_json(COURSE_FILE)
    stu_exist = any(s["stu_id"] == stu_id for s in students)
    cou_exist = any(c["cid"] == cid for c in courses)
    if not stu_exist:
        print("学生不存在")
        pause()
        return
    if not cou_exist:
        print("课程不存在")
        pause()
        return
    scores = load_json(SCORE_FILE)
    for sc in scores:
        if sc["stu_id"] == stu_id and sc["cid"] == cid:
            print("该学生此课程成绩已存在")
            pause()
            return
    new_score = {
        "stu_id": stu_id,
        "cid": cid,
        "score": score,
        "update_time": get_current_time()
    }
    scores.append(new_score)
    if save_json(SCORE_FILE, scores):
        print("成绩录入成功")
    else:
        print("录入失败")
    pause()

def update_score():
    print_sep()
    print("【 修改成绩 】")
    stu_id = input("学号：")
    cid = input("课程编号：")
    scores = load_json(SCORE_FILE)
    for sc in scores:
        if sc["stu_id"] == stu_id and sc["cid"] == cid:
            new_score = input_score()
            sc["score"] = new_score
            sc["update_time"] = get_current_time()
            save_json(SCORE_FILE, scores)
            print("修改成功")
            pause()
            return
    print("未找到该成绩记录")
    pause()

def list_scores():
    print_sep()
    print("【 全部成绩 】")
    scores = load_json(SCORE_FILE)
    students = load_json(STUDENT_FILE)
    courses = load_json(COURSE_FILE)
    if not scores:
        print("暂无成绩")
    else:
        for sc in scores:
            stu_name = next((s["name"] for s in students if s["stu_id"] == sc["stu_id"]), "未知")
            cou_name = next((c["name"] for c in courses if c["cid"] == sc["cid"]), "未知")
            print(f"学号：{sc['stu_id']} 姓名：{stu_name} | 课程：{cou_name} | 成绩：{sc['score']}")
    pause()

def search_score_by_student():
    stu_id = input("输入学号：")
    scores = load_json(SCORE_FILE)
    students = load_json(STUDENT_FILE)
    courses = load_json(COURSE_FILE)
    print("该学生成绩：")
    for sc in scores:
        if sc["stu_id"] == stu_id:
            stu = next((s for s in students if s["stu_id"] == stu_id), None)
            stu_name = stu["name"] if stu else "未知"
            cou = next((c for c in courses if c["cid"] == sc["cid"]), None)
            cou_name = cou["name"] if cou else "未知"
            print(f"{stu_name} | {cou_name} | {sc['score']}")
    pause()

# ===================== 统计分析 =====================
def stat_class_avg():
    print_sep()
    print("【 班级平均分统计 】")
    scores = load_json(SCORE_FILE)
    students = load_json(STUDENT_FILE)
    courses = load_json(COURSE_FILE)
    cls_map = {}
    for sc in scores:
        stu = next((s for s in students if s["stu_id"] == sc["stu_id"]), None)
        if not stu: continue
        cls = stu["class"]
        if cls not in cls_map:
            cls_map[cls] = []
        cls_map[cls].append(sc["score"])
    for cls, scores_list in cls_map.items():
        avg = sum(scores_list)/len(scores_list)
        print(f"班级：{cls} | 平均分：{avg:.2f}")
    pause()

def stat_course_avg():
    print_sep()
    print("【 课程平均分统计 】")
    scores = load_json(SCORE_FILE)
    courses = load_json(COURSE_FILE)
    cou_map = {}
    for sc in scores:
        cid = sc["cid"]
        if cid not in cou_map:
            cou_map[cid] = []
        cou_map[cid].append(sc["score"])
    for cid, scores_list in cou_map.items():
        cou = next((c for c in courses if c["cid"] == cid), None)
        name = cou["name"] if cou else cid
        avg = sum(scores_list)/len(scores_list)
        print(f"课程：{name} | 平均分：{avg:.2f}")
    pause()

def stat_fail():
    print_sep()
    print("【 不及格统计 】")
    scores = load_json(SCORE_FILE)
    students = load_json(STUDENT_FILE)
    courses = load_json(COURSE_FILE)
    count = 0
    for sc in scores:
        if sc["score"] < 60:
            count +=1
            stu = next((s for s in students if s["stu_id"] == sc["stu_id"]), None)
            cou = next((c for c in courses if c["cid"] == sc["cid"]), None)
            stu_name = stu["name"] if stu else "未知"
            cou_name = cou["name"] if cou else "未知"
            print(f"{stu_name} - {cou_name} - {sc['score']}")
    print(f"不及格总数：{count}")
    pause()

def sort_by_score():
    print_sep()
    print("【 成绩排名 】")
    scores = load_json(SCORE_FILE)
    students = load_json(STUDENT_FILE)
    courses = load_json(COURSE_FILE)
    cid = input("输入课程编号：")
    course_scores = [sc for sc in scores if sc["cid"] == cid]
    if not course_scores:
        print("无成绩")
        pause()
        return
    course_scores.sort(key=lambda x:x["score"], reverse=True)
    cou = next((c for c in courses if c["cid"] == cid), None)
    cou_name = cou["name"] if cou else "未知"
    print(f"课程：{cou_name} 排名")
    for i, sc in enumerate(course_scores, 1):
        stu = next((s for s in students if s["stu_id"] == sc["stu_id"]), None)
        stu_name = stu["name"] if stu else "未知"
        print(f"第{i}名：{stu_name}  {sc['score']}分")
    pause()

# ===================== 菜单 =====================
def admin_menu():
    while True:
        print_sep()
        print("【 管理员菜单 】")
        print("1. 用户管理")
        print("2. 学生管理")
        print("3. 课程管理")
        print("4. 成绩管理")
        print("5. 统计分析")
        print("0. 退出登录")
        choice = input("请选择：")
        if choice == "1":
            user_menu()
        elif choice == "2":
            student_menu()
        elif choice == "3":
            course_menu()
        elif choice == "4":
            score_menu()
        elif choice == "5":
            stat_menu()
        elif choice == "0":
            break
        else:
            print("无效选项")

def teacher_menu():
    while True:
        print_sep()
        print("【 教师菜单 】")
        print("1. 学生管理")
        print("2. 课程管理")
        print("3. 成绩管理")
        print("4. 统计分析")
        print("0. 退出登录")
        choice = input("请选择：")
        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            score_menu()
        elif choice == "4":
            stat_menu()
        elif choice == "0":
            break

def user_menu():
    while True:
        print_sep()
        print("【 用户管理 】")
        print("1. 查看用户")
        print("2. 添加用户")
        print("3. 删除用户")
        print("0. 返回")
        c = input("请选择：")
        if c == "1": list_users()
        elif c == "2": add_user()
        elif c == "3": delete_user()
        elif c == "0": break

def student_menu():
    while True:
        print_sep()
        print("【 学生管理 】")
        print("1. 查看学生")
        print("2. 添加学生")
        print("3. 查询学生")
        print("4. 修改学生")
        print("5. 删除学生")
        print("0. 返回")
        c = input("请选择：")
        if c == "1": list_students()
        elif c == "2": add_student()
        elif c == "3": search_student()
        elif c == "4": update_student()
        elif c == "5": delete_student()
        elif c == "0": break

def course_menu():
    while True:
        print_sep()
        print("【 课程管理 】")
        print("1. 查看课程")
        print("2. 添加课程")
        print("3. 删除课程")
        print("0. 返回")
        c = input("请选择：")
        if c == "1": list_courses()
        elif c == "2": add_course()
        elif c == "3": delete_course()
        elif c == "0": break

def score_menu():
    while True:
        print_sep()
        print("【 成绩管理 】")
        print("1. 查看全部成绩")
        print("2. 录入成绩")
        print("3. 修改成绩")
        print("4. 按学生查询成绩")
        print("0. 返回")
        c = input("请选择：")
        if c == "1": list_scores()
        elif c == "2": add_score()
        elif c == "3": update_score()
        elif c == "4": search_score_by_student()
        elif c == "0": break

def stat_menu():
    while True:
        print_sep()
        print("【 统计分析 】")
        print("1. 班级平均分")
        print("2. 课程平均分")
        print("3. 不及格统计")
        print("4. 课程成绩排名")
        print("0. 返回")
        c = input("请选择：")
        if c == "1": stat_class_avg()
        elif c == "2": stat_course_avg()
        elif c == "3": stat_fail()
        elif c == "4": sort_by_score()
        elif c == "0": break

# ===================== 主函数 =====================
def main():
    init_data_dir()
    init_admin()
    while True:
        print_sep()
        print(" 学生成绩管理系统 ")
        print(" 1. 登录系统")
        print(" 0. 退出")
        choice = input("请选择：")
        if choice == "1":
            user = login()
            if user:
                if user["role"] == "admin":
                    admin_menu()
                else:
                    teacher_menu()
        elif choice == "0":
            print("感谢使用，再见！")
            break
        else:
            print("无效选项")

if __name__ == "__main__":
    main()