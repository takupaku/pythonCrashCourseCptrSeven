sandwich_orders=['Hero', 'hoagie','submarine']
finished_sandwiches=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print("Your "+sandwich+" sandwich has been made.")
    finished_sandwiches.append(sandwich)

print("The following sandwiches have been made.")
for sand in finished_sandwiches:
    print(sand)