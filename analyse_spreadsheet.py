import csv


# Reads a CSV file and returns a list of dictionaries
def read_data():
    with open('Olympics_2024.csv', 'r') as csvfile:
        spreadsheet = csv.DictReader(csvfile)
        return list(spreadsheet)

data = read_data()
# print(f'{data}')

# Calculates total medals per country
def calculate_total_medals():
    total_medals_per_country = {}  # Defines variables for dictionaries
    for row in data:
        country = row['NOC']
        total_medals = row['Total']
        if country not in total_medals_per_country:
            total_medals_per_country[country] = 0
        total_medals_per_country[country] += 1
    return total_medals_per_country

# Displays total number of medals per country from csv
results = calculate_total_medals()
print("Total Medals Per Country:\n")
for country, total_medals in results.items():
    print(f'{country}: {total_medals}')


# Filters the data based on the country name entered by user
def filter_data(user_input):
    filter_data_per_country = {}  # Define variable for dictionary
    for row in data:
        country = row['NOC']
        if country == user_input:
            filter_data_per_country.get(row)
        return filter_data_per_country

user_input = ""
while user_input != "exit":
    user_input = input("Enter the country to view olympic details (or 'exit' to quit):\n")

    filtered_data = filter_data(user_input)

    print(filtered_data)
