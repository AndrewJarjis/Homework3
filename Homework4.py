names = ["Alice Doncic", "Bob Saget", "Charlie Sheen"]
hometowns = ["New York", "London", "Paris"]
favorite_foods = ["Pizza", "Sushi", "Steak"]


def display_student_info(index, category):
    if category == 'hometown' or category == 'home':
        print(f"{names[index]} is from {hometowns[index]}")
    elif category == 'favorite food' or 'food':
        print(f"{names[index]}'s favorite food is {favorite_foods[index]}")
    else:
        print("Invalid category name.")


def search_by_name(name):
    list_index = -1
    for j in range(len(names)):
        if name in names[j].lower():
            list_index = j
            print(f'Student: {names[j]}')
            break
    return list_index


while True:

    search_by_name_str = input("Welcome! Do you want to search by student name? (y/n): ").lower()
    if search_by_name_str == "y":
        name_query = input("Enter student name (full or partial): ").lower()
        name_index = search_by_name(name_query)
        if name_index == -1:
            print("Student not found.")
            continue
        index = name_index
    else:
        student_num = int(input(f"Enter a student number (1-{len(names)}): "))
        if student_num < 1 or student_num > len(names):
            print("Invalid student number. Please try again.")
            continue
        index = student_num - 1
        print(f'Student: {names[index]}')
    print('What category would you like to know?')
    category_name = input("Enter \"hometown\" or \"favorite food\": ").lower()
    category_list = ['hometown', 'favorite food', 'home', 'food']
    if category_name not in category_list:
        print("Invalid category name. Please try again.")
        continue

    display_student_info(index, category_name)

    another_search = input("Do you want to learn about another student? (y/n): ").lower()
    if another_search != "y":
        break

    list_all_str = input("Do you want to list all students? (y/n): ")
    if list_all_str.lower() == "y":
        for i in range(len(names)):
            print(f"{i + 1}. {names[i]}")

print("Thank you for using the student information system.")
