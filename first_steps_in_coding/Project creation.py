# Building a huge project
# To calculate separately how many hours takes from one specialist to finish his part

name = input("Please enter a job position of the specialist here: ")
project = int(input("Please enter a quantity of projects here: "))
level =  input("Please enter a level of a specialist here: 1 for junior specialist or 2 for middle specialist: ")

# jun_total_hours = project * 3 # required time to finish average project for junior specialist

# mid_total_hours = project * 2 # require time to finish average project for middle specialist
if level == "1":
    total_hours = project * 3
elif level == "2":
    total_hours = project * 2
else :
    print("Your input is invalid")
    total_hours = None
if total_hours is not None:
    print(f"It will takes for {name} {total_hours} hours to complete all projects.")