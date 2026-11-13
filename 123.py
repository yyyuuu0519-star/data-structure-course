def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("階層無法計算負數")
    # 終止條件 (Base Case)
    if n == 0 or n == 1:
        return 1
    # 遞迴呼叫 (Recursive Case)
    return n * factorial_recursive(n - 1)

# 測試
num = int(input("請輸入一個整數："))
print(f"{num}! = {factorial_recursive(num)}")
