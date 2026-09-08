import json
import streamlit as st
FILE_NAME = "grades.json"
students = {
    "Mohammad": {
        "Math": [95, 88, 92],
        "Science": [90, 85, 93],
        "English": [87, 91, 89]
    }
}

try:
    
    with open(FILE_NAME, "r") as file:
       
       students = json.load(file)

except FileNotFoundError:
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# A function that adds grades/scores to a chosen student 
def add_grade(name, subject, score):
    
    if name in students:
        if subject in students[name]:
            if score >= 0 and score <= 100:

                students[name][subject].append(score)
                st.write(f"Updated Grade for {name}: {students[name]}")
            else:
                st.write("please enter a valid grade from 0 to 100 and do not leave blank")
        else:
            st.write("Subject doesn't exist or left blank")
    else:
        st.write("Student doesn't exist or input left blank")
# A function where the user can remove a score
def remove_score(name, subject, score):
    if name in students:
        if subject in students[name]:
            if score in students[name][subject]:
                students[name][subject].remove(score)
            else:
                st.write("Score doesn't exist or wrong input")
        else:
            st.write("Subject doesn't exist or left blank")
    else:
        st.write("Name doesn't exist or left blank")
# A function that saves the updated grades to json
def save_grades():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)
# A function that gets average grade based on all the scores
def get_average(name, subject):

    if name in students:
        if subject in students[name]:
            if len(students[name][subject]) == 0:
                st.write("No Score Available")
                return
            average = sum(students[name][subject]) / len(students[name][subject])
            average1 = round(average, 2)
            st.write(f"Average percentage for {name} is {average1}%")
            if average1 >= 90 and average1 <= 100:
                st.write("Letter grade: A")
            elif average1 >= 80 and average1 <= 89.99:
                st.write("Letter grade: B")
            elif average1 >= 70 and average1 <= 79.99:
                st.write("Letter grade: C")
            elif average1 >= 60 and average1 <= 69.99:
                st.write("Letter grade: D")
            elif average1 <= 59.99:
                st.write("Letter grade: F")
            else:
                st.write("Error")

        else:
            st.write("Wrong subject input or left blank")
    else:
        st.write("Wrong student input or left blank")
def display_score(student):
    if student in students:
        st.write(f"Here are the grades for {student} {students[student]}")
    else:
        st.write("Wrong input or left blank")

def add_student(name, subjects):
    
    student_subjects = {}

    for subject in subjects:
        student_subjects[subject] = []
        
    students[name] = student_subjects
    st.write(f"{name} has been added.")
        
def remove_student(student):
    if student in students:
        del students[student]
        st.write(f"Removed {student}")
    else:
        st.write("Student don't exist try again")

                

st.title("Test Score Tracker")
user_input = st.selectbox("What would you like to do?", 
    [
        "Add Score",
        "Add Student",
        "Display Scores",
        "Get Average",
        "Remove Score",
        "Remove Student"

                                  
    ]

)


if user_input == "Add Score":
    name = st.selectbox("Which Student:" , list(students.keys()))
    subject = st.selectbox("Which Subject:" , list(students[name].keys()))
    score = st.number_input("What score:", min_value=0, max_value=100)

    if st.button("Add Score"):
        add_grade(name, subject, score)
        save_grades()

        


elif user_input == "Add Student":
    name = st.text_input("Enter Student Name:")
    subjects = st.text_input("Enter subjects separated by spaces:")

    if st.button("Add Student"):
        name = name.strip().title()
        subjects = subjects.strip().title().split()

        if name in students:
            st.write("Student already exists")
        else:
            add_student(name, subjects)
            save_grades()



elif user_input == "Display Scores":
    name = st.selectbox("Which Student:" , list(students.keys()))

    if st.button("Display Scores"):
        display_score(name)
        



elif user_input == "Get Average":
    name = st.selectbox("Which Student:" , list(students.keys()))
    subject = st.selectbox("Which Subject:" , list(students[name].keys()))

    if st.button("Get Average"):
        get_average(name, subject)

elif user_input == "Remove Score":
    name = st.selectbox("Which Student:" , list(students.keys()))
    subject = st.selectbox("Which Subject:" , list(students[name].keys()))
    score = st.selectbox(
    "Which score do you want to remove?",
    students[name][subject]
    
)
    if st.button("Remove Score"):
        remove_score(name, subject, score)
        save_grades()

elif user_input == "Remove Student":
    name = st.selectbox("Which Student:" , list(students.keys()))

    if st.button("Remove Student"):
        remove_student(name)
        save_grades()
