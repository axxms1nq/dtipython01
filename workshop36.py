# โปรแกรมตรวจสอบรถว่าผ่านเกณฑ์ของการตรวจสอบค่าคาร์บอนไดซ์ออกไซน์หรือ 
# โดยหากค่าคาร์บอนไดซ์ออกไซน์มีค่าเกินกว่า 678.55 ให้แสดงข้อความว่า “ไม่ผ่าน”  หากน้อยกว่า 678.55 ให้แสดงข้อความ “ผ่าน” 
# โดยให้รับชื่อเจ้าของ ทะเบียนรถ และปริมาณก๊าซคาร์บอนไดซ์ออกไซน์ที่วัดได้ ทางแป้นพิมพี่

# Feature: ใช้ฟังก์ชันในการตรวจสอบรถว่าผ่านเกณฑ์หรือไม่
# - รับค่าชื่อเจ้าของ ทะเบียนรถ และปริมาณก๊าซคาร์บอนไดซ์ออกไซน์ที่วัดได้
# - ตรวจสอบค่าคาร์บอนไดซ์ออกไซน์ ก๊าซ
# - แสดงผลการตรวจสอบรถว่าผ่านเกณฑ์หรือไม่
# - แสดงชื่่อโปรแกรม

def show_program_name():
    print("-------------------------------")
    print("ตรวจสอบค่าคาร์บอนไดซ์ออกไซน์")
    print("-------------------------------")

def input_car_info():
    car_owner = input("กรุณาใส่ชื่อเจ้าของรถ: ")
    car_number = input("กรุณาใส่ทะเบียนรถ: ")
    car_carbon = float(input("กรุณาใส่ค่าคาร์บอนไดซ์ออกไซน์ที่วัดได้: "))
    return car_owner, car_number, car_carbon

def show_result(car_owner, car_number, car_carbon, result):
    print(f'คุณ {car_owner} ทะเบียนรถ {car_number} ค่าคาร์บอนไดซ์ออกไซน์ {car_carbon} ผลการตรวจสอบ {result}')
    print(f'ค่าคาร์บอนไดซ์ออกไซน์ {car_carbon} ผลการตรวจสอบ {result}')

def check_carbon(car_owner, car_number, car_carbon):
    if car_carbon > 678.55 :
        show_result(car_owner, car_number, car_carbon, "ไม่ผ่าน")
    else:
        show_result(car_owner, car_number, car_carbon, "ผ่าน")

show_program_name()
car_owner, car_number, car_carbon = input_car_info()
print("-------------------------------")
check_carbon(car_owner, car_number, car_carbon) 
print("-------------------------------") 