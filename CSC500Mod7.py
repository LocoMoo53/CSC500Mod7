## Jason Thomas
## CSC 500
##Module 7

def main():
    ## Dictionaries as per instructions
    rooms_dict = {
        'CSC 101': '3004',
        'CSC 102': '4501',
        'CSC 103': '6755',
        'NET 110': '1244',
        'COM 241': '1411'
    }

    instructors_dict = {
        'CSC 101': 'Haynes',
        'CSC 102': 'Alvarado',
        'CSC 103': 'Rich',
        'NET 110': 'Burke',
        'COM 241': 'Lee'
    }

    times_dict = {
        'CSC 101': '8:00 a.m.',
        'CSC 102': '9:00 a.m.',
        'CSC 103': '10:00 a.m.',
        'NET 110': '11:00 a.m.',
        'COM 241': '1:00 p.m.'
    }

    ## User input (Course number) and coverts to uppercase to ignore case sensitivity
    user_course = input("Enter course number: ").upper()

    ## Print statement as per instructions
    if user_course in rooms_dict:
        print(f"Room Number: {rooms_dict[user_course]}")
        print(f"Instructor: {instructors_dict[user_course]}")
        print(f"Meeting Time: {times_dict[user_course]}")
    else:
        print("Course not found.")

if __name__ == "__main__":
    main()
