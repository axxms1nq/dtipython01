# 4. have parameter , have return
'''
def func_name(param,param,param.....) :
    คำสั่ง 
    คำสั่ง
    ........
    return ข้อมูลที่ต้องการส่งกลับ
'''
def sum_number(n1, n2, n3) :
    total = n1 + n2 + n3
    return total

def welcome(name) :
    massage = 'Hello' + name
    return massage

print(sum_number(1, 2, 3,))

# print(welcome('สมชาย')) ไม่ควรเขียนแบบนี้

print(sum_number(10, 20, 30,))

data1, data2 = welcome('สมชาย')
print(data1)
print(data2)