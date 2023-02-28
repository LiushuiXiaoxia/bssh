import json


class TestUser:
    age = 1


u1 = TestUser()
print(f'u1.age = {u1.age}')
u1.age = 22
print(f'u1.age = {u1.age}')

u2 = TestUser()
print(f'u2.age = {u2.age}')
u2.age = 33
print(f'u2.age = {u2.age}')

print(f'u1.age = {u1.age}')
print(f'u2.age = {u2.age}')

print(f'age = {TestUser.age}')

print('---')

TestUser.age = 100
print(f'u1.age = {u1.age}')
print(f'u2.age = {u2.age}')
print(f'age = {TestUser.age}')

a = [
    {
        'user': 'name'
    }
]

with open('a.json', 'w') as f:
    f.write(json.dumps(a, indent=4))
