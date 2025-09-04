#Operator ตัวดำเนินการ คือ เครื่องหมาย
# 1. Asithemetic Opt. เครื่องหมายคำนวณ
# + - * / **(exponent) %(mod) //(floor)
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # หารปกติ
print(10 % 3)  # หารเอาเศษ
print(10 // 3) # หารเอาส่วน
print(10 ** 3)
print('+++++++++++++++++')
# 2. Comparison Opt. เครื่องหมายเปรียบเทียบ ผลลัพธ์ที่มีคือ True หรือ False
# == , != , > , < , >= , <=
print(10 >= 25)  # False
print(999 > 555) # False
print('Rayong' >= 'Ranong')
print('+++++++++++++++++')
# 3. Logical Opt. เครื่องหมายตรรกะ
# not , and , or
# ข้อมูลที่จะใช้กับเครื่องหมายมีแค่ True/False และผลลัพธ์ True/False (boolean)
print(not True)
print(not False)
print('+++++++++++++++++')
print(True and True)    #True
print(True and False)   #False
print(False and True)   #False
print(False and False)  #False
print('+++++++++++++++++')
print(True or True)     #True
print(True or False)    #True
print(False or True)    #True
print(False or False)   #False