# 要求三:演算法
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
# 提醒:請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊 
    maxProuctAns = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            maxProuctAns.append(nums[i]*nums[j])
    print(max(maxProuctAns))
    return

maxProduct([5, 20, 2, 6]) # 得到 120 
maxProduct([10, -20, 0, 3]) # 得到 30 
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0 
maxProduct([-1, -2, 0]) # 得到 2