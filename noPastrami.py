sandwich_orders=['pastrami','Hero', 'hoagie','pastrami','submarine','pastrami']
finished_sandwich=[]
print('deli has run out of pastrami sandwich.')
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    sandwich=sandwich_orders.pop()
    finished_sandwich.append(sandwich)

print("So, the finished sandwiches are..")
for sand in finished_sandwich:
    print(sand)