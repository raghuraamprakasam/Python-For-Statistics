# nested match case
choice = int(input("Enter the value from 0 to 2:"))
match choice:
    case 0:
        print("June")
        x = float(input("Enter sub from 0.1 to 0.3:"))
        match x:
            case 0.1:
                print("Week 1 of june")
            case 0.2:
                print("Week 2 of june")
            case 0.3:
                print("Week 3 of june")
            case _:
                print("Enter a valid sub head")
    case 1:
        print("July")
        y = float(input("Enter sub from 1.1 to 1.3:"))
        match y:
            case 1.1:
                print("Week 1 of july")
            case 1.2:
                print("Week 2 of july")
            case 1.3:
                print("Week 3 of july")
            case _:
                print("Enter a valid sub head")
    
    case 2:
        print("August")
        z = float(input("Enter sub from 2.1 to 2.3:"))
        match z:
            case 2.1:
                print("Week 1 of aug")
            case 2.2:
                print("Week 2 of aug")
            case 2.3:
                print("Week 3 of aug")
            case _:
                print("Enter a valid sub head")

    case _:
        print("Enter a valid value from 0 to 3")
        
