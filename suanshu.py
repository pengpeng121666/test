# 定义一个函数来获取用户输入并返回两个数字
def get_numbers():
    try:
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        return num1, num2
    except ValueError:
        print("输入无效，请输入数字。")
        return get_numbers()  # 递归调用以重新获取输入

# 定义一个函数来进行算术运算
def perform_operations(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    
    # 检查除数是否为零以避免除零错误
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print(f"{num1} / {num2} 是未定义的（除数不能为零）")

# 主程序
if __name__ == "__main__":
    num1, num2 = get_numbers()
    perform_operations(num1, num2)