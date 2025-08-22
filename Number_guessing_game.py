import random
a = int(input("Enter the upper limit :" ))
b = int(input("Enter the lower limit :" ))
random_number = random.randint(b,a)
attempt = 0
while True: 
    guess = int(input("Enter the Guess Number : "))
    attempt += 1
    if guess > random_number:
        print("Too High , Try Smaler Number")
    elif guess < random_number:
        print("Too Low , Try Larger Number")
    elif guess == random_number:
        print("Congratulation! , You Win")
        print("Your Number is ",random_number)
        print(" You won in ", attempt,"attempt")
        break
    else:
        print("Enter a Valid Number :")    


    

