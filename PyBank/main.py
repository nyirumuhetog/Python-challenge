import csv

# Open the CSV file
with open('yourfilename.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    next(csvreader)
    # Initialize variables
    total_months = 0
    total_profit_losses = 0
    previous_profit_loss = 0
    profit_losses_changes = []
    dates = []
    # Loop through the rows of the CSV file
    for row in csvreader:
        # Increment the total number of months
        total_months += 1
        # Add the profit/loss to the total
        total_profit_losses += int(row[1])
        # Calculate the change in profit/loss from the previous month
        if previous_profit_loss != 0:
            change = int(row[1]) - previous_profit_loss
            profit_losses_changes.append(change)
        # Save the date for later
        dates.append(row[0])
        # Remember the current profit/loss for the next iteration
        previous_profit_loss = int(row[1])
    # Calculate the average change in profit/loss
    average_change = sum(profit_losses_changes) / len(profit_losses_changes)
    # Find the greatest increase in profits
    max_increase = max(profit_losses_changes)
    max_increase_date = dates[profit_losses_changes.index(max_increase) + 1]
    # Find the greatest decrease in losses
    max_decrease = min(profit_losses_changes)
    max_decrease_date = dates[profit_losses_changes.index(max_decrease) + 1]
    # Print the results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
    print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")