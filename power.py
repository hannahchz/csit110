#exercise 5 
#Question 5
#Write a function named multiply(num1, num2) that will 
#return the multiplication  of num1 and num2 using only summation.

#Question 6
#Write a function named power(num1, num2) that will 
#return value of num1 to the power of num2 using the multiply function 
#that you have written in the previous question.

def multiply(num1, num2):
    r=0
    if (num2>num1):
      num1, num2 = num2, num1 
    for i in range (num2): #smaller second number
         r+=num1
    return r 
print(multiply(5,4))

def power(num1, num2):
    r=1
    for i in range(num2):
        r=multiply(r, num1)
    return r

print(power(5,4))
print(5**4)