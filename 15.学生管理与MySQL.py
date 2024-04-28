import os
import json
import pymysql

datas = {
    'students': [
        {"id": 101, "name": 12, "age": 18, "sex": "男"},
    ]
}
file_name = "小的学生系统(少但完整).txt"
inf = """
输入数字1，添加学生信息
输入数字2，查看所有学生信息
输入数字3，统计学生平均年纪
输入数字4，统计学生性别比例
输入数字5，退出系统
"""  # 用户界面


def show_user_interface():
    print(f"欢迎来到学生管理系统".center(30, "$"))
    print(inf)


def select_check(tip, scope):
    """
    对用户输入的选项进行校验！
    :param tip: 提示用户的信息。
    :param scope: 用户合法输入的范围。
    :return:
    """
    option = int(input(tip))
    if option in scope:
        return True, option
    else:
        print("输入内容不合法！请重新输入！")
        return False, None


def quit_process():
    print("感谢使用！欢迎下次再来！")
    exit()


def view_all_students():
    if isexist_student():
        for st in datas["students"]:
            print(st)
    print("所有学生信息显示完毕！")


def isexist_student(student_id=0):
    """
    如果不传参，则判断的是是否有学生。
    如果传入参数，就是判断指定的学生是否存在。
    :param student_id:
    :return:
    """
    if student_id == 0:
        if len(datas["students"]) == 0:
            print("该学生管理系统中还未有学生。")
            return False
        else:
            return True
    else:
        for stu in datas["students"]:
            if stu["id"] == student_id:
                return True
        print(f"未找到id为{student_id}的学生！")
        return False


def input_three_items():
    while 1:
        tem_na = input("输入名字,长度为2或者3：")
        if len(tem_na) > 3 or len(tem_na) < 2:
            print("名字不合法！")
        else:
            break
    while 1:
        tem_se = input("输入性别，男或者女：")
        if tem_se != '男' and tem_se != '女':
            print("性别不合法！")
        else:
            break
    while 1:
        tem_ag = int(input("输入年龄，15-25之间："))
        if tem_ag >= 25 or tem_ag <= 15:
            print("年龄不合法！")
        else:
            break
    return tem_na, tem_ag, tem_se


def show_isadd_interface():
    print("是否要继续添加？")
    print("1.继续！")
    print("2.返回主菜单！")


def add_student():
    while 1:
        base_information = input_three_items()
        if isexist_student():
            new_student = {"id": 1 + datas["students"][-1]["id"], "name": base_information[0],
                           "age": base_information[1],
                           "sex": base_information[2]}

        else:
            new_student = {"id": 101, "name": base_information[0],
                           "age": base_information[1],
                           "sex": base_information[2]}
        # noinspection PyTypeChecke
        datas['students'].append(dict(new_student))
        for st in datas["students"]:
            print(st)
        print("添加成功！")
        save_sql()
        show_isadd_interface()
        while 1:
            option = select_check("请选择", [1, 2])
            if option[0]:
                if option[1] == 1:
                    break
                else:
                    return
            else:
                pass


def get_average_age():
    if isexist_student():
        sum_age = 0
        for stu in datas["students"]:
            sum_age += stu["age"]
        print(f"学生的平均年龄为{sum_age / len(datas['students'])}")


def get_sex_ratio():
    if isexist_student():
        man_count = 0
        for stu in datas["students"]:
            if stu["sex"] == "男":
                man_count += 1
        print(f"男生占比为{(man_count / len(datas['students'])) * 100}%")


# def load_datas():
#     global datas
#     if os.path.exists(file_name):
#         with open(file_name, "r") as f:
#             datas = json.load(f)
#     else:
#         pass


def load_sql():
    global datas

    con = pymysql.connect(port=3306, user='root', password='123456')
    cur = con.cursor()
    cur.execute('show databases like "sm"')
    if cur.fetchall():
        cur.execute('use sm')
        datas = {
            'students': []
        }
        cur.execute('select * from students')
        naked_data = cur.fetchall()
        for data in naked_data:
            tem_dic = {'id': data[0],
                       'name': data[1],
                       "age": data[2],
                       "sex": data[3]}
            datas['students'].append(tem_dic)

    else:
        sqls = [
            'create database sm charset=utf8;',
            'use sm',
            'create table students (id int not null primary key,name varchar(225) not null,age int ,sex varchar(225))'
        ]
        cur.execute(sqls[0])
        cur.execute(sqls[1])
        cur.execute(sqls[2])

    con.commit()
    cur.close()
    con.close()


# def save_datas():
#     global datas
#     with open(file_name, "w") as f:
#         json.dump(datas, f)


def save_sql():
    global datas
    naked_data = []
    for stu in datas['students']:
        tem_tuple = (stu['id'], stu['name'], stu['age'], stu['sex'])
        naked_data.append(tem_tuple)
    naked_data = tuple(naked_data)
    con = pymysql.connect(port=3306, user='root', password='123456', database='sm')
    cur = con.cursor()
    cur.execute('delete from students')
    cur.executemany('insert into students values (%s,%s,%s,%s)', naked_data)

    con.commit()
    cur.close()
    con.close()


def main():
    load_sql()
    while 1:
        show_user_interface()
        ret_option = select_check("尊敬的用户请选择你的操作:", [i for i in range(1, 6)])
        if ret_option[0]:
            if ret_option[1] == 1:
                add_student()
            elif ret_option[1] == 2:
                view_all_students()
            elif ret_option[1] == 3:
                get_average_age()
            elif ret_option[1] == 4:
                get_sex_ratio()
            elif ret_option[1] == 5:
                quit_process()

        else:
            pass


main()
