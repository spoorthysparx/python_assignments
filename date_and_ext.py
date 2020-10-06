import os,datetime

def get_files_between_range():
    start_range=convert_to_date(input('Enter the start date as yyyy-mm-dd: '))
    end_range=convert_to_date(input("Enter the end date as yyyy-mm-dd: "))
    ext = input("Enter the file extension: ")
    get_files_by_date_and_ext(start_range,end_range,ext)

def get_files_by_date_and_ext(start_date, end_date,extension):
    path=input("enter the path:")
    for (root, directories, files) in os.walk(path):
        for name in files:
            file = os.path.join(root, name)
            created_date = get_created_date(file)
            if check_file_in_range(created_date, start_date, end_date) and name.endswith(extension):
                print(file, "\t", created_date)
            

def check_file_in_range(created_date, start_date, end_date):
    if start_date <= created_date and created_date <= end_date:
        return True
    else:
        return False


def convert_to_date(x):
    year, month, day = map(int, x.split('-'))
    return datetime.date(year, month, day)

def get_created_date(file):
    return datetime.date.fromtimestamp(os.path.getctime(file))    

get_files_between_range()


