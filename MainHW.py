#homework week 2 / group 2 
#ex1
def read_file(file_path: str) -> list:
    """
    reads the file mentioned in the path, and returns the list with records

    Input:
    file_path (str)
        the path to a file you want to read

    Output:
    records (list)
        list of all records
    """
    records = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append(row)
    return(records)

def total_and_avarege_calculation (records):
    """
    calculates the total and avarege of the records list 

    Input:
    records (list)
        list of all records
    
    Output:
    total,average(float)
        total and avarege of a records list 

    """
    total = sum(float(record['Grade']) for record in records)
    average = total / len(records)
    return (total,average)


def filter_results(records):
    """
    filter the grades by the 80.0 grade 

    Input:
    records (list)
        list of all records
    
    Output:
    filtered_records(list)
        filtered list 

    """
    filtered_records = [record for record in records if float(record['Grade']) >= 80.0]
    return(filtered_records)


def print_results(records):
    """
    prints the student report for the filtered records.

    Input:
    records (list)
        list of all records
    
    Output:
    print of the information

    """
    print("Student Report")
    print("--------------")
    for record in filtered_records:
        print(f"Name: {record['Name']}")
    print(f"Grade: {record['Grade']}")
    print("--------------------")


def main():
    """
    
    Main function to run the code generally
     
    """
    file_path = input("Enter the path to the CSV file: ")
    #request the input of the path to the CSV file with students' data 

    records = read_file(file_path)
    #runs the function and creates the list with records

    total,average = total_and_avarege_calculation (records)
    #run the function of total and avarege  

    print(f"Average Grade: {average}")
    print("--------------------")  
    #prints avarege grade 

    filtered_records = filter_results(records)
    #creates a list with records where the grade is greater than or equal to 80
    
    print_results(filtered_records)
    #print record of filtered results 
    

