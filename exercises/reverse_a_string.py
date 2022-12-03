#str[start:stop:step]

string = 'Daniel Iyiola'
reversed_string = string[::-1]

print(reversed_string)

a = [[96], [69]]

print(''.join(list(map(str, a))))

employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

for item in employee_list:
    print(item['id'])
