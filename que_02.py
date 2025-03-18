def get_value(obj, key_path):
    keys = key_path.split("/")
    for key in keys:
        if isinstance(obj, dict) and key in obj:
            obj = obj[key]
        else:
            return None
    return obj

# Open and read JSON file without using json module
with open("jsonfile.json", "r") as file:
    data = eval(file.read())  # Convert string to dictionary (Use eval cautiously)

# Ask user for key input
while True:
    key_path = input("Enter the key path (use '/' to separate levels, or type 'exit' to quit): ").strip()
    
    if key_path.lower() == "exit":
        print("Exiting...")
        break

    value = get_value(data, key_path)
    
    if value is not None:
        print(f"Value: {value}")
    else:
        print("Key not found!")
