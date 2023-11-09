def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "除数不能为零"
    return x / y

while True:
    print("选择运算:")
    print("1. 相加")
    print("2. 相减")
    print("3. 相乘")
    print("4. 相除")
    print("5. end")

    choice = input("请输入选项 (1/2/3/4/5):")

    if choice == '5':
        print("程序已退出.")
        break
