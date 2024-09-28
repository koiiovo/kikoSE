import random
import operator

# 四则运算的操作符映射
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def user_input_calculation():
    """用户手动输入计算"""
    print("手动输入计算：")
    try:
        num1 = float(input("请输入第一个数字："))
        op = input("请选择操作符 (+, -, *, /): ")
        num2 = float(input("请输入第二个数字："))

        if op in operations:
            result = operations[op](num1, num2)
            print(f"结果：{num1} {op} {num2} = {result}")
        else:
            print("无效的操作符，请重新输入")
    except ZeroDivisionError:
        print("错误：除数不能为0！")
    except ValueError:
        print("错误：输入的不是数字！")

def generate_random_problem():
    """随机生成四则运算题目"""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(list(operations.keys()))

    print(f"随机题目： {num1} {op} {num2}")
    user_answer = input("请输入你的答案： ")

    try:
        correct_answer = operations[op](num1, num2)
        if float(user_answer) == round(correct_answer, 2):
            print("回答正确！")
        else:
            print(f"回答错误，正确答案是： {correct_answer}")
    except ZeroDivisionError:
        print("错误：除数不能为0！")
    except ValueError:
        print("错误：输入的不是有效答案！")

def main():
    """主函数，选择模式"""
    while True:
        print("\n1. 手动输入运算\n2. 随机生成题目\n3. 退出")
        choice = input("请选择选项 (1, 2, 3): ")

        if choice == "1":
            user_input_calculation()
        elif choice == "2":
            generate_random_problem()
        elif choice == "3":
            print("程序已退出")
            break
        else:
            print("无效的选择，请重新输入")

if __name__ == "__main__":
    main()
