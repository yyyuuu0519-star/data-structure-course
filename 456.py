def calculate_n(n):
    if n < 0:
        return None  # 小於 0 沒有值
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_n(n - 1) + calculate_n(n - 2)

# 取得使用者輸入並測試
try:
    user_input = int(input("請輸入整數 n: "))
    if user_input < 0:
        print("小於 0 沒有值")
    else:
        sequence = [calculate_n(index) for index in range(user_input + 1)]
        print(" ".join(map(str, sequence)))
except ValueError:
    print("請輸入有效的整數")