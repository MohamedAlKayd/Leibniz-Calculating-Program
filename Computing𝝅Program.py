# Mohamed Yasser Anwar Mahmoud AlKayd
# Computing 𝝅 Program

# - Start of the Program -

num_terms = int(input("Please enter the number of terms: "))

def pi(num_terms): #define the pi function used
    start_point = 0 #we start at 0 
    base_value = 1 #1 is the base value we are subtracting from
    for a in range(num_terms): #use for loop to define 
        start_point += base_value/(2*a+1)
        base_value = -base_value #negate the value 
    return 4*start_point #end function call and return the result 
    
answer=pi(num_terms) #using the function
print("The approximate value of pi is",answer)
1
 
answer=sum((-1)**i/(2*i+1) for i in reversed(range(num_terms)))*4 #process the range of the sequence in reverse using leibniz's equation
print("The approximate value of pi is",answer)

# - End of the Program -