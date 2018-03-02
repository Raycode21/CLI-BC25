import getpass


current_user = None
user_level = 1


def main():
    choose_action = home_page ()
    if choose_action == 1:
        '''Log in user'''
        user_name = input()
        print(user_name)
        user_password = getpass.getpass()

        if login(user_name, user_password):
            current_user = user_name

            
            
            '''Logged in user'''
            chosenOption = input('''
                Welcome {}
 
                Select Action

                    1 - Post Comment
                    2 - View Comments
                    3 - Logout
            
            '''.format(current_user))
            

        else:
            print('Error!! Username or Password is wrong')        
        
    else:
        '''Signup user'''
        print('Create New Account')
        user_name = input('''
            What is your username? ''')

        user_password = getpass.getpass('''
        What about your password?

        ''')

def login(user_name, user_password):
    if user_name == "dc" and user_password == 'password':
        return True

def logout():
    current_user = None

def home_page():
    if not current_user:
        choose_action = input('''
        Choose action - Enter 1 or 2
            1 - Log In
            2 - Sign Up
        ''')
    
    return choose_action













if __name__ == "__main__":
    main()