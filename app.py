def store_names():
    filename = "names.txt"
    print("Enter names (type 'exit' to stop):")
    
    with open(filename, "a") as file:  # Open file in append mode
        while True:
            name = input("Enter name: ")
            if name.lower() == "exit":
                break
            file.write(name + "\n")
    
    print(f"Names have been saved to {filename}")

def show_names():
    filename = "names.txt"
    try:
        with open(filename, "r") as file:
            names = file.readlines()
            if names:
                print("Stored Names:")
                for name in names:
                    print(name.strip())
            else:
                print("No names stored yet.")
    except FileNotFoundError:
        print("No names file found. Start by adding some names.")

if __name__ == "__main__":
    while True:
        choice = input("Choose an option: (1) Store Names (2) Show Names (3) Exit: ")
        if choice == "1":
            store_names()
        elif choice == "2":
            show_names()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
