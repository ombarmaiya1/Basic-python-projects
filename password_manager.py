m_pass = input("Enter your master password : ").lower()
def view():
    with open('password.txt', 'r') as f:
        for lines in f:
            print(lines.rstrip())

def add():
    name = input("Account Name : ")
    pwd = input("Password : ")
    with open('password.txt','a') as f:
        f.write(name + " = " + pwd +"\n")
    print("Password added.")
while True:
    mode = input("Enter the mode (add/view or Q to quit) : ").lower()
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    elif mode == "q":
        break
    else:
        print("Enter a valid input : ")