if __name__ == "__main__":
    print('Welcome to File Module')


def create_file():
        filename = input("Enter file name (with .txt): ")

        if not filename.endswith(".txt"):
            print("Error: Only .txt files are allowed.\n")
            return

        try:
            with open(filename, "x"):
                print(f"File '{filename}' created successfully!\n")

        except FileExistsError:
            print(f"File '{filename}' already exists.\n")

        except Exception as e:
            print("Error creating file:", e)

def write_file():
    try:
        filename = input('Enter file name to write:- ')


        date = input("Enter date (YYYY-MM-DD HH:MM:SS): ")
        entry = input("Enter your journal entry:\n")

        with open(filename, "w") as file:
            file.write(f"[{date}]\n{entry}\n\n")

        print("Entry added successfully!\n")

    except Exception as e:
        print("Error while adding entry:", e)


def view_data():

    filename = input('Enter file name to view data:- ')

    if not filename:
        return

    try:
        with open(filename, "r") as file:
            content = file.read()

            if content.strip() == "":
                print("No journal entries found.\n")
            else:
                print("\nYour Journal Entries:")
                print("-" * 40)
                print(content)

    except FileNotFoundError:
        print("Error: File does not exist.\n")


def append_file():
    try:
        filename = input('Enter file name to append:- ')


        date = input("Enter date (YYYY-MM-DD HH:MM:SS): ")
        entry = input("Enter your journal entry:\n")

        with open(filename, "a") as file:
            file.write(f"[{date}]\n{entry}\n\n")

        print("Entry added successfully!\n")

    except Exception as e:
        print("Error while adding entry:", e)


def main():

    print('\nFile Operations:\n')

    while True: 

        print('1. Create a new file')
        print('2. Write to a file')
        print('3. Read from a file')
        print('4. Append to a file')
        print('5. Back to Main Menu')

        choice = int(input('Enter your choice:- '))

        print('')

        match choice:
            case 1: 
                create_file()
            case 2: 
                write_file()
            case 3: 
                view_data()
            case 4:
                append_file()
            case 5:
                break
            case _:
                print('\nInvalid choice!\n')

