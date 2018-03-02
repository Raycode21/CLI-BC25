choose_action = input('''
    Choose action - Enter 1 or 2
        1 - Log In
        2 - Sign Up
    ''')

if choose_action == 1:
    print('username: ')

    user_name = str(input())

    print('Password: ')
    user_password = input ()

    login (user_name, user_password)

else:
    print('signup')



def login(user_name, user_password):
    print('login in')
    if user_name == "dc" and user_password == 'password':
        return True