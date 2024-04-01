def mayas_pizdit(value):
    print(value)

def mayas_sprashivaet(prompt):
    return input(prompt)

def execute_line(line):
    parts = line.split()
    if len(parts) < 2:
        print("Invalid syntax")
        return

    command = parts[0]
    if command == "mayas_pizdit":
        value = " ".join(parts[1:])
        mayas_pizdit(value)
    elif command == "mayas_sprashivaet":
        prompt = " ".join(parts[1:])
        return mayas_sprashivaet(prompt)
    else:
        print("Unknown command")

def execute_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            execute_line(line.strip())

if __name__ == "__main__":
    file_path = input("Enter MAyasScript file path: ")
    execute_file(file_path)