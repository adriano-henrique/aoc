import os

year = input("Enter the AoC year you're working on: \n")
number = input(f"Enter the AoC problem for year {year}: \n")

base_path = os.getcwd()
number_dir = "p" + str(number)

year_path = os.path.join(base_path, year)

if not os.path.exists(year_path):
    print(f"Creating new folder for year {year}")
    os.makedirs(year_path)

problem_path = os.path.join(year_path, number_dir)

if not os.path.exists(problem_path):
    os.makedirs(problem_path)
files_path = os.path.join(problem_path, "files")

if not os.path.exists(files_path):
    os.makedirs(files_path)
    
file_names = ["p1.txt","p2.txt","tp1.txt","tp2.txt"]
for file_name in file_names:
    file_path = os.path.join(files_path, file_name)
    with open(file_path, 'w') as file:
        file.write("")