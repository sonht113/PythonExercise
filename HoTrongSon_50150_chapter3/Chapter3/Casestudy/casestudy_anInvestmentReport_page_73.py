"""
Author: Hồ Trọng Sơn
Date: 23/07/2021
Program: casestudy_anInvestmentReport_page_73.py

PROBLEM:
    Compute an investment report.
        1. The inputs are starting investment amount number of years interest rate (an integer percent)
        2. The report is displayed in tabular form with a header.
        3. Computations and outputs:
            -   for each year compute the interest and add it to the investment print a formatted row
                of results for that year
        4. The ending investment and interest earned are also

SOLUTION:
"""
# Accept the inputs
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))

# Convert the rate to a decimal number
rate = rate / 100

# Initialize the accumulator for the interest
totalInterest = 0.0

# Display the header for the table
print("%4s%18s%10s%16s" % ("Year", "Starting balance", "Interest", "Ending balance"))

# Compute and display the results for each year
for year in range(1, years + 1):
    interest = startBalance * rate
    totalInterest += interest;
    endBalance = startBalance + interest
    print("%4d%18.2f%10.2f%16.2f" % (year, startBalance, interest, endBalance))
    startBalance = endBalance
print(totalInterest);
print(endBalance);

 # Display result:
 #        Enter the investment amount: 2000
 #        Enter the number of years: 2
 #        Enter the rate as a %: 3
 #        Year  Starting balance  Interest  Ending balance
 #            1           2000.00     60.00         2060.00
 #            2           2060.00     61.80         2121.80
 #        Ending balance: $121.8
 #        Total interest earned: $2121.8