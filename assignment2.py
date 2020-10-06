import os,datetime

def get_all_files(filepath):
    for (root, directories, files) in os.walk(filepath):
        for name in files:
            file = os.path.join(root, name)
            print(file)

def files_by_extension(filepath):
    extension = input("Enter the file extension: \n").strip('.')
    for (root, directories, files) in os.walk(filepath):
        for name in files:
            if name.endswith(extension):
                file = os.path.join(root, name)
                print(file)

def files_created_yesterday(filepath):
    start_date = todays_date - datetime.timedelta(days=1)
    end_date = start_date
    get_files_by_date(start_date, end_date,filepath)

def files_between_date(filepath):
    start_date = convert_to_date(input("Enter the start date (yyyy-mm-dd): "))
    end_date = convert_to_date(input("Enter the end date (yyyy-mm-dd): "))
    get_files_by_date(start_date, end_date,filepath)

def get_files_between_range_and_ext(filepath):
    start_date = convert_to_date(input("Enter the start date (yyyy-mm-dd): "))
    end_date = convert_to_date(input("Enter the end date (yyyy-mm-dd): "))
    ext = input("Enter the file extension: ")
    get_files_by_date(start_date,end_date,filepath,ext)


def get_files_by_date(start_date, end_date,filepath,ext = None):
    for (root, directories, files) in os.walk(filepath):
        for name in files:
            file = os.path.join(root, name)
            created_date = get_created_date(file)
            if ext!=None:
                if check_file_in_range(created_date, start_date, end_date) and file.endswith(ext):
                    print(file, "\t", created_date)
            else:
                if check_file_in_range(created_date, start_date, end_date):
                    print(file, "\t", created_date)

def get_created_date(file):
    return datetime.date.fromtimestamp(os.path.getctime(file))

def check_file_in_range(created_date, start_date, end_date):
    if start_date <= created_date and created_date <= end_date:
        return True
    else:
        return False

def convert_to_date(x):
    year, month, day = map(int, x.split('-'))
    return datetime.date(year, month, day)

todays_date = datetime.date.today()

print("what you want to extract")
print("1->all files\n2->files with extension\n3->created yesterday\n4->files between the range\n5->files between range and extension\n6->exit")
path = input("Enter file path: ")
while True:
    user_input=int(input("Enter the command: "))
    if user_input==1:
        get_all_files(path)
    elif user_input==2:
        files_by_extension(path)
    elif user_input==3:
        files_created_yesterday(path)
    elif user_input==4:
        files_between_date(path)
    elif user_input==5:
        get_files_between_range_and_ext(path)
    elif user_input==6:
        break    


