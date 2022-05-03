#Author: Ramona Grant
#Date Created: May 1, 2022
#Course: ITT103
#Purpose:This program will calculate the commission for sales person based on the class and sales.

# accepting input from user

sales_person_number = input("enter sales person number: ")
sales = input("enter sales amount: ")
sales_class = input("enter the sales class: ")



# defining a function named commission
def commission(sales_person_number, sales, sales_class):

  # checking the sales class
  if sales_class == 1:
    
    # checking the sales amount, calculating the commission and printing
    if sales <= 1000:
      rate = 0.06
      print(sales_person_number, ":", sales * rate)

    elif sales > 1000 and sales < 2000:
      rate = 0.07
      print(sales_person_number, ":", sales * rate)

    else:
      rate = 0.1
      print(sales_person_number, ":", sales * rate)

  elif sales_class == 2:

    if sales < 1000:
      rate = 0.04
      print(sales_person_number, ":", sales * rate)

    else:
      rate = 0.06
      print(sales_person_number, ":", sales * rate)
  
  elif sales_class == 3:

    rate = 0.45
    print(sales_person_number, ":", sales * rate)

  else: # if the sales class is not valid the following 
        # print statement is executed
    print("the sales class is not Valid")




# checking if the inputs are null
if (sales_person_number and sales and sales_class):
  # if the inputs are not null we cast them to integer that we can use them in
  # equations
  sales_person_number = int(sales_person_number)
  sales = int(sales)
  sales_class = int(sales_class)
  
  # invoking the function above and passing the 
  # sales_person_number, sales and sales_class as function arguments
  commission(sales_person_number, sales, sales_class)
else:
  # if any of the inputs is null the following print statement will be executed
  print("null value entered")

