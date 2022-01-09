# 要求二:Python 字典與列表、JavaScript 物件與陣列 
# 完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
# 提醒:請勿更動題目中任何已經寫好的程式。

def avg(data):
# 請用你的程式補完這個函式的區塊
    total = 0 
    for i in range(data["count"]):
        total += data["employees"][i]['salary']
    ans = total / data["count"]
    print(ans)
    return


avg({
    "count":3, 
    "employees":[
        {
        "name":"John",
        "salary":30000 },
        {
        "name":"Bob",
        "salary":60000 },
        {
        "name":"Jenny",
        "salary":50000 }
    ]
}) 

# 呼叫 avg 函式