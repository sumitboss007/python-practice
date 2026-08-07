name = input("What's your name ? ")
 
match name:
    case "Harry" | "Sumit" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")