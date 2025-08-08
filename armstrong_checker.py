

def is_armstrong(num):
    digits=str(num)
    power=len(digits)
    total=sum(int(d)**power for d in digits)
    return total==num

while True:
    user_input = (input("Enter a number (or type 'exit' to quit): "))
    if user_input.lower()=="exit":
        print("Exiting Armstrong checker, good bye ")
        break
    if not user_input.isdigit():
        print("please enter a valid positive integer. ")
        continue
    number=int(user_input)
    if is_armstrong(number):
       print(number,"is an Armstrong number")
    else:
       print(number,"is NOT an Armstrong number  ")