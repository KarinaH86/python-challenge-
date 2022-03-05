
# Dependencies
import csv
import os

# Files to load and output 
budget_csv = os.path.join("..","Resources", "budget_data.csv")
output_path = os.path.join("..","analysis", "budget_analysis.txt')

# Declare variables 
totalMonths = 0
month_of_change = []
net_change_list = []
greatestInc = ["", 0]
greatestDec = ["", 9999999999999999999]
total_net = 0

revenueChanges = []
                           

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Calculate the totals 
        total_months += 1
        totalRevenue = totalRevenue + int(row[1]

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
                                          
        # Calculate the greatest increase
        if (revChange < greatestInc[1]):
            greatestInc[1] = revChange
            greatestinc[0] = row["Date"]

        # Calculate the greatest decrease
        if (revChange < greatestDec[1]:
            greatestDec[1] = revChange 
            greatestDec[0] = row["Date"]
         revenueChanges.append(revChange)

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# print output to terminal as follows:
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatestInc[0]} (${greatestInc[1]})\n"
    f"Greatest Decrease in Profits: {greatestDec[0]} (${greatestDec[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
            txt_file.write("Total Months: " + str(totalMonths)
            txt_file.write("\n")
            txt_file.write("Revenue: " = "$" + str(totalRevenue)
            txt_file.write("\n")
            txt_file.write("Avarage Change: " + "$" + str(round(averageChange,2)))
            txt_file.write("\n")
            txt_file.write("GreatestInc" + str(greatestInc[0]) = ", ($" + str(greatestInc[1] + ")")
            txt_file.write("\n")
            txt_file.write("GreatestDec:" = str(greatestDec[0]) = ",($" + str(greatestDec[1]) + ")")
