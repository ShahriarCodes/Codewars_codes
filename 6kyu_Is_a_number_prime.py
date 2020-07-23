
def prime_number(num):
    
    if num > 1:
  
       for i in range(2,num):
           if (num % i) == 0:

            return False
               
       else:
           return True 
       
    else:
        return False
    
prime_number(4)




# def prime_number(num):
    
#     if num > 1:
#        # check for factors
#        for i in range(2,num):
#            if (num % i) == 0:
#                print(num,"is not a prime number")
#                print(i,"times",num//i,"is",num)
#                break
#        else:
#            print(num,"is a prime number")

#     # if input number is less than
#     # or equal to 1, it is not prime
#     else:
#        print(num,"is not a prime number")

# prime_number(4)
