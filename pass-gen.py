import os ,sys,random,time,string

digits = list(string.digits)
alphabeth = list(string.ascii_letters)
special_characters = list("!@#$%^&*")
digits_and_alphabeth = list(digits + alphabeth)
digits_and_spcial_characters = list(digits + special_characters)
alphabeth_and_special = list(alphabeth + special_characters)
everything = list (digits + alphabeth + special_characters)
definitions = []
count = []
passwords = []
passwords_path_folder = []

def generate(length_of_password,d,a,s):
    password = []
    if d == True and a == False and s == False:
        for i in range(length_of_password):
            password.append(random.choice(digits))
    elif a == True and d == False and s == False:
        for i in range(length_of_password):
            password.append(random.choice(alphabeth))
    elif s == True and a == False and d == False:
        for i in range(length_of_password):
            password.append(random.choice(special_characters))
    elif a == True and d == True and s == False:
        for i in range(length_of_password):
            password.append(random.choice(digits_and_alphabeth))
    elif a == True and d == False and s == True:
        for i in range(length_of_password):
            password.append(random.choice(alphabeth_and_special))
    elif a == False and d == True and s == True:
        for i in range(length_of_password):
            password.append(random.choice(digits_and_spcial_characters))
    elif a == True and d == True and s == True:
        for i in range(length_of_password):
            password.append(random.choice(everything))
    elif a == False and d == False and s == False:
        clear_console()
        print("Can't generate password without any characters.\n")
        time.sleep(3)
        boot_pw_gen()
    passwords.append("".join(password))

def clear_console():
    for i in range(500):
        print("\n")

def verify_len(x):
    clear_console()
    print("Password length is :",x)
    verify_len_ans = input("Are you sure you want generate password with this lenght (y/n): ")
    if verify_len_ans == "y" or verify_len_ans == "Y":
        return True
    elif verify_len_ans == "n" or verify_len_ans == "N":
        return False
    else:
        verify_len(x)

def len_ask():
    clear_console()
    len_ans = input("How long password do you want? :")
    if len_ans == "":
        len_ask()
    elif len_ans.isnumeric() == True:
        if int(len_ans) <= 0:
            len_ask()
        elif int(len_ans) > 0:
            if int(len_ans) > 500:
                if verify_len(int(len_ans)) == True:
                    definitions.append(int(len_ans))
                else:
                    len_ask()
            else:
                definitions.append(int(len_ans))
    else:
        len_ask()

def definition_ask_digs():
    clear_console()
    digs = input("Do you want numbers in your password (y/n): ")
    if digs == "y" or digs == "Y":
        definitions.append(True)
    elif digs == "n" or digs == "N":
        definitions.append(False)
    else:
        definition_ask_digs()

def definition_ask_alph():
    clear_console()
    alph = input("Do you want letters in your password (y/n): ")
    if alph == "y" or alph == "Y":
        definitions.append(True)
    elif alph == "n" or alph == "N":
        definitions.append(False)
    else:
        definition_ask_digs() 

def definition_ask_spec():
    clear_console()
    spec = input("Do you want special characters in your password (y/n): ")
    if spec == "y" or spec == "Y":
        definitions.append(True)
    elif spec == "n" or spec == "N":
        definitions.append(False)
    else:
        definition_ask_spec()

def count_ask():
    clear_console()
    count_of_password = input("How many passwords do you want? : ")
    if count_of_password.isnumeric() == True:
        if int(count_of_password) == 0:
            boot_pw_gen()
        elif int(count_of_password) > 0:
            count.append(int(count_of_password))
        else:
            count_ask()
    else:
        count_ask()

def reset_generator():
    clear_console()
    definitions.clear()
    count.clear()
    passwords.clear()

def check_exist(patch):
    final_name = []
    number_addon = [1]
    if os.path.exists(patch) == True:
        check_loop = True
        while check_loop is True:
            customized_patch = [patch[:len(patch)-4],str(number_addon[0]),patch[len(patch)-4:]]
            if os.path.exists("".join(customized_patch)) == True:
                number_addon.append(number_addon[0]+1)
                number_addon.pop(0)
            else:
                final_name.append("".join(customized_patch))
                check_loop = False
    else:
        final_name.append(patch)
    passwords_path_folder.clear()
    passwords_path_folder.append(final_name[0])
    return final_name

def write_to_file():
    #check_exist("./Passwords/passwords.txt")
    file_name = check_exist(passwords_path_folder[0] +"Passwords.txt")[0]
    with open(file_name, 'w') as file:
        line = [0]
        for row in passwords:
            line.append(line[0]+1)
            line.pop(0)
            file.write("Password number " + str(line[0]) + " : \n" + row + '\n\n')

def get_platform():
    platforms = {
        'linux'  : 'Linux',
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform  
    return platforms[sys.platform]

def passwords_folder():
    if get_platform() == "Windows":
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        if os.path.exists(desktop + "/Passwords"):
            pass
        else:
            os.mkdir(desktop + "/Passwords")
        passwords_path_folder.append(desktop + "/Passwords/")
    elif get_platform() == "Linux":
        if os.path.exists("/home/Passwords"):
            pass
        else:
            os.mkdir("/home/Passwords")
        passwords_path_folder.append("/home/Passwords/")
    else:
        print("You don't have supported OS for use this program if you want me to add your OS create request.")

def boot_pw_gen():
    reset_generator()
    passwords_folder()
    count_ask()
    len_ask()
    definition_ask_digs()
    definition_ask_alph()
    definition_ask_spec()
    for i in range(count[0]):
        generate(definitions[0],definitions[1],definitions[2],definitions[3])
    write_to_file()
    clear_console()
    print("Your passwords has been generated you can find it in : \n" + passwords_path_folder[0]+"\n")

boot_pw_gen()

    
