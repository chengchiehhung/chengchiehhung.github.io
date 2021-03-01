 #要求一: 函式與流程控制
def calculate(min, max):
# 請用你的程式補完這個函式的區塊
    total = 0
    
    for i in range(min, max+1):
        total += i
    
    print(total)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後在 console 印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後在 console 印出 30

#要求二：Python 字典與列表、JavaScript 物件與陣列
def avg(data):
# 請用你的程式補完這個函式的區塊
    count = data['count']
    salary_sum = 0

    for employee in data['employees']:
        salary_sum += employee['salary']
    
    print(salary_sum/count) #印出員工的平均薪資

avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
}) # 呼叫 avg 函式

#要求三：演算法
def bubble_sort(nums): #自定義一個排序函式
    n = len(nums)

    for i in range(n-1):
        flag = 0

        for j in range(n-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                flag = 1
        
        if flag == 0:
            break
    
    return nums

def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    nums = bubble_sort(nums) #先將list排序
    Max = nums[-1] * nums[-2] #將最大的2數相乘
    Min = nums[0] * nums[1] #考慮有可能會有2個負數相乘，而產生一個正數可能會大於Max
    
    if Max > Min: #把2個極端值做比較，即可得到相乘的最大值
        print(Max) #印出相乘得到的最大值
    else:
        print(Min) #印出相乘得到的最大值
    

maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值

#要求四 ( 請閱讀英文 )：演算法
def twoSum(nums, target):
    # your code here
    for num in nums:
        
        if num >= target: #如果數字本身就大於target，可直接跳過。
            continue
        
        complement = target-num #找出數字補數

        if complement in nums: #若當下數字的補數也存在list中，即為答案。
            return [nums.index(num), nums.index(complement)] #回傳2數的indices

        


result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


#要求五 ( Optional )：演算法
def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊

    count = 0 #計算連續幾個0
    temp = 0 #存放當前最大的連續0數字

    for num in nums:
        if num == 0:
            count += 1
        else: #若當前數字不為0則重新計算長度
            count = 0
        
        if count > temp: #確認累積長度有沒有大於上次存放的最大長度，若有，則替換
            temp = count
        
    print(temp) #將最大連續0的長度印出


maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
