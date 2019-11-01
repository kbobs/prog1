# This program calculates sales commissions.

# Create a variable to control the loop.
keep_going = 'y'

# Calculate a series of commissions.
while keep_going == 'y' or keep_going == 'Y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the % commission rate: '))
    bonus_comm = 50
    
    if comm_rate>=0 and comm_rate<=100:
            
        # Calculate the commission.
        commission = sales * comm_rate/100

        # Display the commission.
        print('The commission is £', \
              format(commission, '.2f'),sep='')
    elif sales>5000:

        # Calculate the commission with a £50 bonus is sales are over £5000
        commission = (sales * comm_rate/100) + bonus_comm

        # Display the commission with bonus.
        print("The commission is £", format(commission, '.2f'), sep='')
        print("Congratulations, you have earned a £50 bonus on your commission.")

        # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another ' + \
                           'commission (Enter y for yes): ')
    else:

        print('There is an input error')
# end of while loop

print('In that case I wave my underpants at your auntie.')
