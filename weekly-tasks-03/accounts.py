# Weekly Task 03 - Part of coursework for ATU 24-25: 4122 -- PROGRAMMING AND SCRIPTING
# Author Linda Nikolajeva

# Programme that that reads in a 10 character account number
# And outputs the account number
# With only the last 4 digits showing
# And the first 6 digits replaced with Xs

# note to self, insert comment 'in the question, the number is ambigious,
# but the output implies we should be dealing with integers.
# So I am casting the input to an integer'

account_num = input("Enter your 10 digit account number: ").strip()
# no need to convert to int or float as we are not doing maths

hidden_nums = "X" * 6 + account_num(-4:)

print("Your account number is: ", hidden_nums)

# https://chatgpt.com/c/67baff98-e4d0-8005-ba4a-8d373fa65b6b
# note to self ..need to look at W3schools to link in terminology and understanding in comments