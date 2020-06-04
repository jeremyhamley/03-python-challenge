#convert employee data to new format and output to csv file
#import modules: os , csv
import os
import csv
#define the path to access the csv file with raw data
csvpath = os.path.join("Resources-PyBoss", "employee_data.csv")

#create empty lists: Emp ID, First Name, Last Name, DOB, SSN, State
emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []
#add dictionary of state abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#open and read data in csv file
with open(csvpath,'r') as employee_data:
    read_employee_data = csv.reader(employee_data, delimiter = ',')
    #read header
    employee_header = next(read_employee_data)
    for employee in read_employee_data:
        #record employee id
        emp_id.append(employee[0])

        #split name - record first and last name
        split_name = employee[1].split(" ")
        first_name.append(split_name[0])
        last_name.append(split_name[1])

        #split and format dob
        split_dob = employee[2].split("-")
        dob.append(f'{split_dob[1]}/{split_dob[2]}/{split_dob[0]}')

        #split ssn - record last 4 digits of ssn
        split_ssn = employee[3].split("-")
        ssn.append(f'***-**-{split_ssn[2]}')

        #convert state to abbreviation
        state.append(f'{us_state_abbrev[(employee[4])]}')        

#zip lists together       
new_employee_data = zip(emp_id, first_name, last_name, dob, ssn, state)
#set variable and path to output new employee data
output_file = os.path.join("new_employee_data.csv")
#open a new csv file and save the newly formatted employee data as a csv file
with open(output_file, "w") as new_data:
    writer = csv.writer(new_data)
    #write header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    #write zipped data
    writer.writerows(new_employee_data)
    new_data.close()
 