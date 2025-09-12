# โปรแกรมซึ่งรับชื่อ และปีเกิดของผู้ใช้โปรแกรมทางแป้นพิมพ์ โดยหากอายุมีค่าตั้งแต่ 55 พ.ศ ปีขึ้นไป 
# ให้แสดงข้อความว่า "คุณแก่แล้ว..." หากไม่ถึงให้แสดงข้อความ "คุณยังไม่แก่..." ทางหน้าจอ

from datetime import datetime

def show_menu():
    print('-------------------------------')
    print(' Program check Age')
    print('-------------------------------')

def input_data():
    name = input('ป้อนชื่อของคุณ ==>> ')
    birth_year = int(input('ป้อนปีเกิดของคุณ ==>> '))
    return name, birth_year

def show_result(name, birth_year):
    current_year = (datetime.now().year + 543 ) 
    age = current_year - birth_year
    print('-------------------------------')
    print('คุณ {} เกิดปี {} มีอายุ {} ปี'.format(name, birth_year, age))

def check_age(name, birth_year):
    current_year = (datetime.now().year + 543 ) 
    age = current_year - birth_year
    print('-------------------------------')
    if age >= 55 : 
        print('คุณ {} มีอายุ {} ปี คุณแก่แล้ว...'.format(name, age))
    else : 
        print('คุณ {} มีอายุ {} ปี คุณยังไม่แก่...'.format(name, age))

show_menu()
user_name, user_birth_year = input_data()
check_age(user_name, user_birth_year)