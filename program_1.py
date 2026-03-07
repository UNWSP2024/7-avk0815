# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

def main():
    rainfall = []
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    for i in range(12):
        while True:
            try:
                amount = float(input(f"Enter the total rainfall for {months[i]}: "))
                if amount < 0:
                    print("Rainfall cannot be negative. Please enter a valid amount.")
                    continue
                rainfall.append(amount)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / 12

    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)

    max_month = months[rainfall.index(max_rainfall)]
    min_month = months[rainfall.index(min_rainfall)]

    print(f"\nTotal rainfall for the year: {total_rainfall}")
    print(f"Average monthly rainfall: {average_rainfall}")
    print(f"Month with highest rainfall: {max_month} ({max_rainfall})")
    print(f"Month with lowest rainfall: {min_month} ({min_rainfall})")
    

if __name__ == "__main__":
    main()