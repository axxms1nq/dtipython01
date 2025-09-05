# break , continue
# break ใช้สําหรับหยุดการทํางานของ loop
# continue ใช้สําหรับข้ามการทํางานของ loop
for i in range(5) :
    if i == 3 :
        break
    print(i, 'Hi...')

print('+++++++++++++++++++')

for i in range(5) :
    if i == 3 :
        continue
    print(i, 'Hey...')

print('Bye bye...')