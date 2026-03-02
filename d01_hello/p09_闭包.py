def create_counter():
    """创建一个计数器闭包"""
    count = 0  # 这是闭包要"记住"的变量
    
    def counter():
        nonlocal count  # 声明使用外部变量（Python 3+ 需要）
        count += 1
        return count
    
    return counter  # 返回内部函数，而不是调用它

# 使用闭包
counter1 = create_counter()
counter2 = create_counter()

print("计数器1:")
print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

print("\n计数器2（独立的计数器）:")
print(counter2())  # 1
print(counter2())  # 2

print("\n再次使用计数器1:")
print(counter1())  # 4 - 保持了之前的状态！