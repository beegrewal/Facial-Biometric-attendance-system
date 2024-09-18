import streamlit as st
import hashlib
import os
import cv2
import numpy as np
import pandas as pd
import joblib
from datetime import date, datetime
from sklearn.neighbors import KNeighborsClassifier
import plotly.express as px
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# Admin credentials
nimgs = 10
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD_HASH = hashlib.sha256('admin@2002'.encode()).hexdigest()

# Initialize face detector
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Create necessary directories
if not os.path.isdir('Attendance'):
    os.makedirs('Attendance')
if not os.path.isdir('static'):
    os.makedirs('static')
if not os.path.isdir('static/faces'):
    os.makedirs('static/faces')
if f'Attendance-{datetoday}.csv' not in os.listdir('Attendance'):
    with open(f'Attendance/Attendance-{datetoday}.csv', 'w') as f:
        f.write('Name,Roll,Department,Phone Number,Incoming Time,Outgoing Time')

# Utility functions for user authentication
def load_user_db():
    if os.path.exists('user_db.py'):
        import importlib.util
        spec = importlib.util.spec_from_file_location("user_db", "user_db.py")
        user_db_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(user_db_module)
        return user_db_module.user_db
    return {}

def save_user_db(user_db):
    with open('user_db.py', 'w') as file:
        file.write(f"user_db = {user_db}\n")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_admin(username, password):
    return username == ADMIN_USERNAME and hash_password(password) == ADMIN_PASSWORD_HASH

def authenticate_student(username, password):
    user_db = load_user_db()
    return user_db.get(username) == hash_password(password)

# Functions related to attendance
def totalreg():
    return len(os.listdir('static/faces'))

def extract_faces(img):
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_points = face_detector.detectMultiScale(gray, 1.2, 5, minSize=(20, 20))
        if len(face_points) == 0:
            return []  # No faces detected, return empty list
        return face_points
    except Exception as e:
        print(f"Error in face detection: {e}")
        return []  # Return empty list if an error occurs

def identify_face(facearray):
    model = joblib.load('static/face_recognition_model.pkl')
    return model.predict(facearray)

def train_model():
    faces = []
    labels = []
    userlist = os.listdir('static/faces')
    for user in userlist:
        for imgname in os.listdir(f'static/faces/{user}'):
            img = cv2.imread(f'static/faces/{user}/{imgname}')
            resized_face = cv2.resize(img, (50, 50))
            faces.append(resized_face.ravel())
            labels.append(user)
    faces = np.array(faces)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(faces, labels)
    joblib.dump(knn, 'static/face_recognition_model.pkl')

def extract_attendance(attendance_date=None):
    if attendance_date is None:
        attendance_date = datetoday
    attendance_file = f'Attendance/Attendance-{attendance_date}.csv'
    
    if not os.path.exists(attendance_file):
        return None, 0
    
    df = pd.read_csv(attendance_file)
    names = df['Name']
    rolls = df['Roll']
    departments = df['Department']
    phone_numbers = df['Phone Number']
    incoming_times = df['Incoming Time']
    outgoing_times = df['Outgoing Time']
    l = len(df)
    return df, l

def add_attendance(name, attendance_type):
    username, userid, department, phone = name.split('_')[0], name.split('_')[1], name.split('_')[2], name.split('_')[3]
    current_time = datetime.now().strftime("%H:%M:%S")

    df = pd.read_csv(f'Attendance/Attendance-{datetoday}.csv')
    user_rows = df[df['Roll'] == int(userid)]

    if user_rows.empty:
        with open(f'Attendance/Attendance-{datetoday}.csv', 'a') as f:
            f.write(f'\n{username},{userid},{department},{phone},{current_time},' if attendance_type == 'Incoming' 
                    else f'\n{username},{userid},{department},{phone},,{current_time}')
    elif attendance_type == 'Incoming' and pd.isna(user_rows['Incoming Time'].values[0]):
        df.loc[df['Roll'] == int(userid), 'Incoming Time'] = current_time
        df.to_csv(f'Attendance/Attendance-{datetoday}.csv', index=False)
    elif attendance_type == 'Outgoing':
        df.loc[df['Roll'] == int(userid), 'Outgoing Time'] = current_time
        df.to_csv(f'Attendance/Attendance-{datetoday}.csv', index=False)

def getallusers():
    userlist = os.listdir('static/faces')
    names = []
    rolls = []
    departments = []
    phones = []
    l = len(userlist)
    for i in userlist:
        name, roll, department, phone = i.split('_')
        names.append(name)
        rolls.append(roll)
        departments.append(department)
        phones.append(phone)
    return userlist, names, rolls, departments, phones, l

def deletefolder(duser):
    pics = os.listdir(duser)
    for i in pics:
        os.remove(duser+'/'+i)
    os.rmdir(duser)

def process_camera_frame(action):
    cap = cv2.VideoCapture(0)
    
    st.write("Camera is open. Press 'Esc' to stop.")
    
    # Create a placeholder to update the image
    frame_placeholder = st.empty()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture image from camera.")
            break

        faces = extract_faces(frame)
        if len(faces) > 0:
            (x, y, w, h) = faces[0]  # Get the first detected face
            face = frame[y:y+h, x:x+w]
            resized_face = cv2.resize(face, (50, 50)).ravel()
            identified_user = identify_face([resized_face])

            if len(identified_user) > 0:
                name = identified_user[0]
                add_attendance(name, action)
                st.success(f"Marked {name} as {action}")
                
                # Display attendance of the identified user
                user_attendance_df, _ = extract_attendance(datetoday)
                user_attendance = user_attendance_df[user_attendance_df['Name'] == name] if user_attendance_df is not None else pd.DataFrame()
                if not user_attendance.empty:
                    st.write(f"Attendance for {name}:")
                    st.write(user_attendance[['Name', 'Roll', 'Department', 'Phone Number', 'Incoming Time', 'Outgoing Time']])

            cv2.rectangle(frame, (x, y), (x+w, y+h), (86, 32, 251), 1)
        
        # Convert frame to RGB and display with Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)

        if cv2.waitKey(1) == 27:  # Escape key to exit
            break

    cap.release()
    cv2.destroyAllWindows()

# Admin application with sidebar navigation
def admin_app():
    st.title("Admin Dashboard")

    # Sidebar for navigation using streamlit-option-menu
    with st.sidebar:
        selected_option = option_menu(
            menu_title=None,
            options=['Home', 'Attendance', 'Add New Student', 'Delete Student', 'Mark Attendance', 'Developer', 'Back to Main Page'],
            icons=['house', 'list-check', 'person-plus', 'person-x', 'camera', 'code', 'house-door'],
            menu_icon="cast",
            default_index=0
        )

    if selected_option == 'Back to Main Page':
        st.session_state['admin_authenticated'] = False
        st.session_state['student_authenticated'] = False
        st.experimental_rerun()

    elif selected_option == 'Home':
        st.write("Welcome to the Admin Dashboard")

    elif selected_option == 'Attendance':
        st.header("View Attendance")
        selected_date = st.date_input("Select a date", value=date.today())
        selected_date_str = selected_date.strftime("%m_%d_%y")
        df, l = extract_attendance(selected_date_str)
        
        if df is not None:
            st.write(f"Total Users in Database: {totalreg()}")
            st.write(f"Date: {selected_date.strftime('%d-%B-%Y')}")
            st.write(pd.DataFrame({
                'S No': range(1, l+1), 
                'Name': df['Name'], 'ID': df['Roll'], 
                'Department': df['Department'], 'Phone Number': df['Phone Number'],
                'Incoming Time': df['Incoming Time'], 
                'Outgoing Time': df['Outgoing Time']
            }))
        else:
            st.warning("No attendance found for the selected date.")

    elif selected_option == 'Add New Student':
        st.header("Add New Student")
        newusername = st.text_input("Enter New Student Name")
        newuserid = st.number_input("Enter New Student Id", min_value=1)
        newdepartment = st.text_input("Enter Department")
        newphone = st.text_input("Enter Phone Number")

        if st.button("Add New Student", key='add_new_student'):
            userimagefolder = f'static/faces/{newusername}_{newuserid}_{newdepartment}_{newphone}'
            if not os.path.isdir(userimagefolder):
                os.makedirs(userimagefolder)
            else:
                st.error("Student already exists")
                return

            user_db = load_user_db()
            user_db[newusername] = hash_password(newphone)  # Store name as username, phone as password
            save_user_db(user_db)

            cap = cv2.VideoCapture(0)
            i = 0
            while True:
                ret, frame = cap.read()
                faces = extract_faces(frame)
                
                if len(faces) > 0:
                    (x, y, w, h) = faces[0]  # Get the first detected face
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (86, 32, 251), 1)
                    face = frame[y:y+h, x:x+w]
                    cv2.imwrite(f'{userimagefolder}/{i}.jpg', face)
                    i += 1
                cv2.imshow("Adding new User", frame)
                if cv2.waitKey(1) == 27 or i == nimgs:  # Escape key or nimgs photos taken
                    break
            cap.release()
            cv2.destroyAllWindows()
            st.success(f"{newusername} with ID {newuserid} Added Successfully")
            train_model()

    elif selected_option == 'Delete Student':
        st.header("Delete Existing Student")
        usernames, names, rolls, departments, phones, l = getallusers()

        deleteusername = st.selectbox("Select Student to Delete", usernames)
        if st.button("Delete Student", key='delete_student'):
            deletefolder(f'static/faces/{deleteusername}')
            train_model()
            st.success(f"{deleteusername} Deleted Successfully")

    elif selected_option == 'Mark Attendance':
        st.header("Mark Attendance")
        action = st.selectbox("Select Action", ["Incoming", "Outgoing"])

        if st.button("Start Camera", key='start_camera'):
            process_camera_frame(action)

    elif selected_option == 'Developer':
        st.markdown(""" 
        - **Team:** Debugging Crew
        - **Team Leader:** Bhagwan Singh
        - **UI/UX:** Raja 
        - **Documentation:** Manisha 
        - **Modules/Algorithm:** Pravesh 
        """)

# Student application with restricted access
def student_app():
    st.title("Student Dashboard")

    # Sidebar for navigation
    with st.sidebar:
        selected_option = option_menu(
            menu_title=None,
            options=['Home', 'Back to Main Page'],
            icons=['house', 'house-door'],
            menu_icon="cast",
            default_index=0
        )

    if selected_option == 'Back to Main Page':
        st.session_state['admin_authenticated'] = False
        st.session_state['student_authenticated'] = False
        st.experimental_rerun()

    elif selected_option == 'Home':
        st.write("Welcome to the Student Dashboard")
        
        selected_date = st.date_input("Select a date", value=date.today())
        selected_date_str = selected_date.strftime("%m_%d_%y")
        df, _ = extract_attendance(selected_date_str)

        current_username = st.session_state['username']

        if df is not None:
            # Filter only the current user's attendance
            student_attendance = df[df['Name'] == current_username]

            if not student_attendance.empty:
                st.write(f"Date: {selected_date.strftime('%d-%B-%Y')}")
                st.write(student_attendance[['Name', 'Roll', 'Department', 'Phone Number', 'Incoming Time', 'Outgoing Time']])

        else:
            st.warning("No attendance found for the selected date.")

# Main application logic
def main():
    if 'admin_authenticated' not in st.session_state:
        st.session_state['admin_authenticated'] = False
    if 'student_authenticated' not in st.session_state:
        st.session_state['student_authenticated'] = False

    st.title("FACE AUTHENTICATION BIOMETRIC ATTENDANCE SYSTEM")

    # Role selection moved to sidebar
    role = st.sidebar.selectbox("Select Role", ['Admin', 'Student'])
    

    if st.session_state['admin_authenticated'] and role == 'Admin':
        admin_app()
    elif st.session_state['student_authenticated'] and role == 'Student':
        student_app()
    else:
        st.subheader("Login Page")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if role == 'Admin':
                if authenticate_admin(username, password):
                    st.success("Logged in as Admin")
                    st.session_state['admin_authenticated'] = True
                    st.session_state['student_authenticated'] = False
                    st.experimental_rerun()
                else:
                    st.error("Invalid Admin credentials")

            elif role == 'Student':
                if authenticate_student(username, password):
                    st.success(f"Logged in as {username}")
                    st.session_state['student_authenticated'] = True
                    st.session_state['admin_authenticated'] = False
                    st.session_state['username'] = username  # Save the username for later reference
                    st.experimental_rerun()
                else:
                    st.error("Invalid Student credentials")
    st.sidebar.info("Made with Debugging Crew")

if __name__ == "__main__":
    main()
