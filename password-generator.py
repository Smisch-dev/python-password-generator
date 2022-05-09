import os,random,time,string
passwords = []
wanted_chars = []
def animate_print(text,delay=0.05):
    custom_text = []
    for i in text:
        custom_text.append(i)
        time.sleep(delay)
        print("".join(custom_text),end="\r")
def animate_input(text,delay=0.05):
    custom_text = []
    for i in text:
        custom_text.append(i)
        time.sleep(delay)
        if len(text) != len(custom_text):
            print("".join(custom_text),end="\r")
        else:
            s = input(f"{text}")
            clear_console("console")
            return s
def clear_console(type="line"):
    if type == "line":
        print(100*" ",end="\r")
    elif type == "console":
        for i in range(100):
            print()
def ask_input(text,type="str"):
    while True:
        if type == "str":
            a = animate_input(text,0.01)
            return a
        elif type == "int":
            try:
                a = int(animate_input(text,0.01))
                return a 
            except: pass
def append_chars(text):
    for i in text:
        wanted_chars.append(i)
def generate(count,leng):
    for i in range(count):
        passwd = []
        for x in range(leng):
            passwd.append(random.choice(wanted_chars))
        passwords.append("".join(passwd))
        random.shuffle(wanted_chars)
    write_passwords_to_file()
def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1
    return path
def write_passwords_to_file():
    if not os.path.exists('Passwords'):
        os.makedirs('Passwords')
    with open(uniquify("./Passwords/passwords.txt"),'x') as f:
        line = 1
        for row in passwords:
            f.write(f"Password number {line} : \n{row}\n\n")
            line += 1      
def ask_for_definitions():
    global passwords_count
    passwords_count = ask_input(" How many passwords do you want (recomended maximum 100)? : ",type="int")
    while True:
        if passwords_count > 100:
            verify_count = ask_input(" Are you sure you want to generate more than 100 passwords (y/n)? : ",type="str")
            if verify_count.lower() in ["y","n"]:
                if verify_count.lower() == "n":
                    animate_print(" GoodBye thank you for using this password generator",0.02)
                    time.sleep(3)
                    quit()
                else: break
        else: break    
    global passwords_len
    passwords_len = ask_input(" How long passwords do you want (recommended maximum 30)? : ",type="int")
    while True:
        if passwords_len > 30:
            verify_len = ask_input(" Are you sure you want to generate longer passwords than 30 characters (y/n)? : ",type="str")
            if verify_len.lower() in ["y","n"]:
                if verify_len.lower() == "n":
                    animate_print(" GoodBye thank you for using this password generator",0.02)
                    time.sleep(3)
                    quit()
                else: break
        else: break    
    while True:
        want_small_alph = ask_input(" Do you want to have small Alphabet characters in your passwords (y/n)? : ",type="str")
        if want_small_alph.lower() == "y":
            append_chars(string.ascii_lowercase)
            break
        elif want_small_alph.lower() == "n":
            break
    while True:
        want_capital_alph = ask_input(" Do you want to have capital Alphabet characters in your passwords (y/n)? : ",type="str")
        if want_capital_alph.lower() == "y":
            append_chars(string.ascii_uppercase)
            break
        elif want_capital_alph.lower() == "n":
            break     
    while True:
        want_digits = ask_input(" Do you want digits in your passwords (y/n)? : ",type="str")
        if want_digits.lower() == "y":
            append_chars(string.digits)
            break
        elif want_digits.lower() == "n":
            break 
    while True:
        want_specials = ask_input(" Do you want special characters in your passwords (y/n)? : ",type="str")
        if want_specials.lower() == "y":
            append_chars("!#$%&*+-@><=_")
            break
        elif want_specials.lower() == "n":
            break
    random.shuffle(wanted_chars)
    generate(passwords_count,passwords_len)
def pwgen_boot():
    animate_print(" Hello this is password generator created by Smisch",0.02)
    time.sleep(1)
    clear_console("line")
    ask_for_definitions()
pwgen_boot()
