# Weekly Task 04 - Part of coursework for ATU 24-25: 4122 -- PROGRAMMING AND SCRIPTING
# Author Linda Nikolajeva

# Programme that that asks the user to input any positive integer
# And outputs the successive values
# At each step calculates the next value
# By taking the current value
# And if it is even divide it by two
# But if it is odd multiply it by three and add one
# And the programme ends when the current value is one

# Sources used: https://www.youtube.com/watch?v=094y1Z2wpJg&t=1s accessed 02/03/2025
# Source code: https://python-forum.io/thread-9591.html
# https://github.com/Demagogue14/My-Projects/blob/main/collatz.py
# https://www.reddit.com/r/learnpython/comments/17mm9yp/simple_collatz_sequence_problem_code_help/?rdt=65076#:~:text=If%20number%20is%20even%2C%20then,function%20returns%20the%20value%201.
# https://chatgpt.com/c/67c4422a-74f0-8005-a5dc-03fea95eeda3
# https://chatgpt.com/c/67c442a0-9348-8005-b916-1b756ae4399b 
# source used to fix numbers printing twice https://chatgpt.com/c/67c44353-5540-8005-af71-bc727666b301
# ... the above link not working.. need to go back to using code from 2nd link

def collatz(number):
    if number % 2 == 0:
        return number//2
    else:    
        result = 3*number + 1
        return result       
try:
    n = int(input("Give me a number: "))
    while n != 1:
        print(n)
        n = collatz(abs(n))
    if n == 1:
        print(n)
except ValueError:
    print('Type a number please!')