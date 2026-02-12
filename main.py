from pyscript import display, document

def account_verify(e):
    document.getElementById('output').innerHTML = '' 
    
    username = document.getElementById('input1').value
    password = document.getElementById('input2').value
    username_length = len(username)
    password_length = len(password)

    if username_length < 7 and password_length < 10: 
        display('Invalid: Username and password are too short.', target='output')
    elif username_length < 7: 
        display('Username is too short. Retry again.', target='output')
    elif password_length < 10: 
        display('Password is too short. Retry again.', target='output')
    elif password.isalpha(): 
        display('Your password must include with least one number.', target='output')
    elif password.isdigit():
        display('Your password must include with least one letter.', target='output')
    else: 
        display(f'Welcome to the Hub, {username}!', target='output')
