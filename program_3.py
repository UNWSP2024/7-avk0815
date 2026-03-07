# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    print("Enter population data (year, state, population). Type 'done' to finish.")

    # Now have the user enter a year. 
    while True:
        user_input = input("Enter year, state, population (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            year, state, population = user_input.split(',')
            year = int(year.strip())
            state = state.strip()
            population = int(population.strip())
            all_entered_values.append([year, state, population])
        except ValueError:
            print("Invalid input. Please enter data in the format: year, state, population")
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    while True:
        try:
            year_to_sum = int(input("Enter the year to sum population for: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the year.")
    sum_population_for_year(all_entered_values, year_to_sum)

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.
    for record in all_entered_values:
        if record[0] == year_to_sum:
            population_sum = 0
            population_sum += record[2]
    # print the totalled population
    print(f"Total population for the year {year_to_sum}: {population_sum}") 

# Call the main function.
if __name__ == '__main__':
    main()