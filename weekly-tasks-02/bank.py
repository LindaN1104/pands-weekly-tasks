# Programme that prompts the user 
# And read in two money amounts (in cent)
# Then adds the two amounts
# Then prints out the answer in a human readable format 
# With a euro sign and decimal point between the euro and cent of the amount 
# Author Linda Nikolajeva
# Part of coursework for ATU 24-25: 4122 -- PROGRAMMING AND SCRIPTING

# lines 10 to 23 were adapted from from a programme suggested by ChatGPT
def format_money(amount_in_cents):
    euros = amount_in_cents // 100
    cents = amount_in_cents % 100
    return f"€{euros}.{cents:02d}"
# lines 10 to 13 are the string that tells the programme we are dealing with money amounts
# line 10 takes a number and converts is to cents
# without line 10 the programme thinks it is dealing with characters rather than integers
# line 10 essentiall converts the inputed amounts from characters to integers
# line 11 calculates how many euros in the amount inputed
# line 12 calculates the remaining cents
# line 13 makes sure the cents given are always to two decimal places
# Note to self, insert note about using integers and not floating numbers,
# as those don't round properly

# Prompt user for two money amounts in cents
amount1 = int(input("Enter the first amount (in cents): "))
amount2 = int(input("Enter the second amount (in cents): "))
# lines 25 and 26 assing values to amount1 and amount2
# and print the prompt thats gets user to input two amounts

total = amount1 + amount2
# line 30 adds the two amounts together

print("Total amount:", format_money(total))
# line 34 prints/ displays the amount in user friendly format
# without this command the computer would do the calculation and keep the answer to itself