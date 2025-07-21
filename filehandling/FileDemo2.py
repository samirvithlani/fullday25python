name = "yash thakkar"
age =22
rollNo="007"

marks = {"Maths":77,"English":76,"social":88}

with open("marksheet.txt","w") as file:
    file.write(f"Student Name    = {name}\n")
    file.write(f"Student Age     = {age}\n")
    file.write(f"Student Roll NO = {rollNo}\n")
    file.write(f"Subject      Marks      \n")
    for i,j in marks.items():
        file.write(f"{i}      {j}\n")
        
        
        