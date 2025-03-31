choice = "xyz"

match choice:
    case "spring":
        print("Plant the garden!")
    case "summer":
        print("Water the garden!")
    case "fall":
        print("Harvest the garden!")
    case "winter":
        print("Stay indoors!")    
    
    case _:
        print("Invalid choice")     
        


    