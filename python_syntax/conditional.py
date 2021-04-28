user_id = input('id?')
user_pwd = input('password?')

# if user_pwd == '1234':
#     print('Hello master')
#     print('hi')
# else:
#     print('Who are you?')

# if user_id == 'jang':
#     if user_pwd == '1234':
#         print('Hello master')
#     else:
#         print('Who are you?')
# else:
#     print('Who are you?')

if user_id == 'jang' and user_pwd == '1234':
    print('Hello master')
elif user_id == 'sang' and user_pwd == '1234':
    print('Hello sang')
else:
    print('Who are you?')
