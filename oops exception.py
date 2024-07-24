# python program to handel zerodivisionerror exception
num1 = int(input("enter first number:"))
num2 = int(input("enter division number:"))
try :
      print(num1/num2)
except:
      print("somrthing went wrong")
else: 
      print("else block")
finally:
      print("finally block")
      print("line 6")

    #   python progrm that open a file and handels a filenotfounderror exception if file does not exist

try:
    
    open("rahul.txt")
except FileNotFoundError as e:
    print("File not found")


    # python progrm that prompts the user input two number and rasies a typeerror exception if the input are not numerical

    def get_number(prompt):
     while True:
        try:
            return float(input(prompt))
        except ValueError:
            raise TypeError("Input must be a number.")

try:
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    print(f"The numbers you entered are {num1} and {num2}.")
except TypeError as e:
      print(e)





# python program that promptsthe user to input an integer and rasies a value error exception if the input ids not valid integer
user_input = input("Please enter an integer: ")
try:
        
        value = int(user_input)
        print(f"You entered the integer: {value}")
except ValueError:
          raise ValueError("The input is not a valid integer. Please enter a valid integer.")