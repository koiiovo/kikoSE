import tkinter as tk
from tkinter import messagebox
import random
import operator

# 四则运算操作符
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# 计算手动输入的运算
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation_var.get()

        if op in operations:
            result = operations[op](num1, num2)
            label_result.config(text=f"结果: {num1} {op} {num2} = {result}", fg="green")
        else:
            messagebox.showerror("错误", "无效的操作符")
    except ZeroDivisionError:
        messagebox.showerror("错误", "除数不能为0！")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字！")

# 生成随机的四则运算题目
def generate_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(list(operations.keys()))

    label_random_problem.config(text=f"题目: {num1} {op} {num2}")

    def check_answer():
        try:
            user_answer = float(entry_answer.get())
            correct_answer = operations[op](num1, num2)
            if round(user_answer, 2) == round(correct_answer, 2):
                messagebox.showinfo("正确", "回答正确！")
            else:
                messagebox.showinfo("错误", f"回答错误，正确答案是：{correct_answer}")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的答案！")

    button_check.config(command=check_answer)

# 创建主窗口
root = tk.Tk()
root.title("四则运算器")
root.geometry("400x600")  # 设置窗口大小
root.configure(bg="#f0f0f0")  # 背景颜色

# 设置统一的字体
font_title = ("Microsoft YaHei", 16, "bold")
font_text = ("Microsoft YaHei", 12)
font_result = ("Microsoft YaHei", 14, "bold")

# 手动输入计算区域
frame_manual = tk.Frame(root, bg="#f0f0f0")
frame_manual.pack(pady=20)

label_manual = tk.Label(frame_manual, text="手动输入运算", font=font_title, bg="#f0f0f0")
label_manual.grid(row=0, column=0, columnspan=2, pady=10)

label_num1 = tk.Label(frame_manual, text="第一个数字:", font=font_text, bg="#f0f0f0")
label_num1.grid(row=1, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(frame_manual, font=font_text)
entry_num1.grid(row=1, column=1, padx=10, pady=5)

label_num2 = tk.Label(frame_manual, text="第二个数字:", font=font_text, bg="#f0f0f0")
label_num2.grid(row=2, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(frame_manual, font=font_text)
entry_num2.grid(row=2, column=1, padx=10, pady=5)

operation_var = tk.StringVar(value="+")
operation_menu = tk.OptionMenu(frame_manual, operation_var, "+", "-", "*", "/")
operation_menu.config(font=font_text, width=5)
operation_menu.grid(row=3, column=0, columnspan=2, pady=5)

button_calculate = tk.Button(frame_manual, text="计算", font=font_text, bg="#4CAF50", fg="white", command=calculate)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

label_result = tk.Label(frame_manual, text="结果:", font=font_result, bg="#f0f0f0", fg="black")
label_result.grid(row=5, column=0, columnspan=2, pady=10)

# 随机生成题目区域
frame_random = tk.Frame(root, bg="#f0f0f0")
frame_random.pack(pady=20)

label_random = tk.Label(frame_random, text="随机生成题目", font=font_title, bg="#f0f0f0")
label_random.grid(row=0, column=0, columnspan=2, pady=10)

label_random_problem = tk.Label(frame_random, text="题目: ", font=font_text, bg="#f0f0f0")
label_random_problem.grid(row=1, column=0, columnspan=2)

button_generate = tk.Button(frame_random, text="生成题目", font=font_text, bg="#2196F3", fg="white", command=generate_problem)
button_generate.grid(row=2, column=0, columnspan=2, pady=10)

label_answer = tk.Label(frame_random, text="你的答案:", font=font_text, bg="#f0f0f0")
label_answer.grid(row=3, column=0, padx=10, pady=5)
entry_answer = tk.Entry(frame_random, font=font_text)
entry_answer.grid(row=3, column=1, padx=10, pady=5)

button_check = tk.Button(frame_random, text="检查答案", font=font_text, bg="#FF5722", fg="white")
button_check.grid(row=4, column=0, columnspan=2, pady=10)

# 启动主循环
root.mainloop()
