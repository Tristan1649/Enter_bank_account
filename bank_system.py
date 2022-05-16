

country_codes = [
'500', 
'501',
'502', 
'505', 
'507',
'550',
'551',
'552',
'553',
'554',
'555',
'556',
'557',
'559',
'755',
'999',
'771',
'772',
'773',
'774',
'775',
'776',
'777',
'778',
'779',
'220',
'227',
]

name_list = {
      'Asan': {
            'phone' : '+996500123456',
            'name' : 'Asan',
            'cash' : 10000,
            'password' : '12345'
            },
      'Ulan2002' : {
            'phone' : '+996500123456',
            'name' : 'Usan',
            'cash' : 10000,
            'password' : '12345'
            },
      }   

user = None
while True:
    if user is not None:
        print(f'"Welcome {user}!"')

    main_menu = input('Press 1 for registration:\nPress 2 for Authorization:\nPress 3 for transaction:\nPress 4 for more information:\nPress 5 quit profile:\nPress 6 quit system:')
    if main_menu == '1':
        login = input('Create Log in: ')
        name = input('Enter name: ')
        password = input('Create password longer then 8 characters: ')
        password_confirm = input('Confirm password: ')

        while password != password_confirm or len(password) < 8:
                password = input('Create password longer then 8 characters: ')
                password_confirm = input('Confirm password: ')
        print('"Password applied"')


        phone = input('Enter phone number: ')
        while len(phone) != 13 or not phone.startswith('+996') or not phone.strip('+').isdigit() or not phone[4:7] in country_codes:
                print('"mobile applied"')
                break
        else:
            print('"Incorrect mobile"')


        cash = int(input('Enter amount to recieve:'))
        if cash <= 10000:
            print(f'"You recieved {cash}."')
        
        else:
            print('"Account not apply more then 10 000. Enter correct amount!"')

        name_list.update({
            login: {
                'name': name, 
                'password': password, 
                'phone': phone, 
                'cash': cash
                }
            })
        user = login

    elif main_menu == '2':
        if user is not None:
            print('"Already authorized"')
        else:
            login = input('Log in: ')
            password = input('Enter password : ')
            boot = False
            
            if login in name_list and name_list[login]['password'] == password:                          
                boot = True
            if boot:
                print('"Succecefull authorization"')
                user = login

    elif main_menu == '3':
        if user is not None:
            login_p = input("Enter reciever's account")
            cash_tr = int(input('Amount'))
            if login in name_list and name_list[user]['cash'] >= cash_tr:
                name_list[user]['cash'] -= cash_tr
                name_list[login_p]['cash'] += cash_tr
                print(f'"{cash_tr} succesfully transfered"')

            else:
                print('Incorrect datas')
        else:
            print('Enter profile')
            break 

    elif main_menu == '4':
        print(name_list)
        
    elif main_menu == '5':
        print('Profile are leaved')
        user = None

    elif main_menu == '6':
        print('System are leaved')
        break
    else:
        print('No command. Try again')
