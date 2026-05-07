import streamlit as st
import pandas as pd
import hashlib
from PIL import Image
import altair as alt



# Define a function to read the user data from the CSV file
def read_data():
    data = pd.read_csv("data/user_data.csv")
    return data

# Define a function to write the user data to the CSV file
def write_data(data):
    data.to_csv("data/user_data.csv", index=False)

# Create a function to simulate a login check
def simulate_login(username, password):
    if username == "example_user" and password == "example_password":
        return True
    else:
        return False
    
# Function to hash the password using SHA-256 algorithm
def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

# Create a Streamlit app
def loginAndRegister():
    # st.sidebar.subheader(st.session_state)
    st.title("Login and Register Form")

    # Create a menu with two options: Login and Register
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Select an option", menu)

    # Read the user data from the CSV file
    data = read_data()
    # Define variables for the user inputs
    


    # If the user selects "Register"
    if choice == "Register":
        # st.title('Register Form')
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        if st.button("Register"):
            # Check if the username is already in use
            if username in data["Username"].values:
                st.warning("Username already exists. Please choose a different username.")
            # Check if the password and confirm password fields match
            elif password != confirm_password:
                st.warning("Passwords do not match. Please try again.")
            # If the username is new and the passwords match, add the user data to the CSV file
            else:
                hashed_password = hash_password(password)
                new_data = pd.DataFrame({"Username": [username], "Password": [hashed_password]})
                data = pd.concat([data, new_data], axis=0).reset_index(drop=True)
                write_data(data)
                st.success("Registration successful. Please log in.")
                # return True
        # return False
    
    # If the user selects "Login"
    elif choice == "Login":
        # st.title('Login Form')
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            # Check if the username and password are valid
            hashed_password = hash_password(password)
            user_match = data[data["Username"] == username]
            if not user_match.empty and hashed_password == user_match["Password"].values[0]:
                st.success("Logged in successfully.")
                st.empty()
                # Store user data in session state
                if "user_data" not in st.session_state:
                    st.session_state["user_data"] = [username]
                
                return True
                # st.stop()
                
            
            else:
                st.warning("Incorrect username or password. Please try again.")
        return False
                # st.stop()
                

# Run the app
if __name__ == "__main__":

    # Check if user is logged in
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Create the login and registration forms
    if not st.session_state.logged_in:
        if loginAndRegister():
            st.session_state.logged_in = True
            

            html_temp = """
            <div style="background-color:#748c08;padding:1.5px">
            <h1 style="color:white;text-align:center;">Overview of Diabetes 📃</h1>
            </div><br>"""
            st.markdown(html_temp,unsafe_allow_html=True)


            st.title('What is diabetes?')
            st.subheader('In this section:')
            st.markdown(" 👉:blue[What are the different types of diabetes?]") 
            st.markdown(" 👉:blue[How common is diabetes?]") 
            st.markdown(" 👉:blue[Who is more likely to develop type 2 diabetes?]")
            st.markdown(" 👉:blue[What health problems can people with diabetes develop?]") 
            st.markdown(' ')
            st.markdown('Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. **:blue[Insulin]**, a **:blue[hormone]** made by the **:blue[pancreas]**, helps glucose from food get into your cells to be used for energy. Sometimes your body doesn’t make enough—or any—insulin or doesn’t use insulin well. Glucose then stays in your blood and doesn’t reach your cells.')
            st.markdown(' ')
            st.markdown('Over time, having too much glucose in your blood can cause health problems. Although diabetes has no cure, you can take steps to manage your diabetes and stay healthy.')
            st.markdown(' ')
            st.markdown('Sometimes people call diabetes “a touch of sugar” or “borderline diabetes.” These terms suggest that someone doesn’t really have diabetes or has a less serious case, but every case of diabetes is serious.')

            image = Image.open('images/diabetes.png')

            st.image(image, caption='India is often referred to as the "Diabetes Capital of the World", as it accounts for 17%percent of the total number of diabetes patients in the world. There are currently close to 80 million people with diabetes in India and this number is expected to increase to 135 million by 2045.')

            st.title("What are the different types of diabetes?")
            st.markdown(' ')
            st.markdown('The most common types of diabetes are:')
            st.markdown('-> Type 1 diabetes')
            st.markdown('-> Type 2 diabetes')
            st.markdown('-> Gestational diabetes')

            st.subheader('a) Type 1 Diabetes')
            # st.markdown(' ')
            st.markdown('If you have type 1 diabetes, your body does not make insulin. Your immune system attacks and destroys the cells in your pancreas that make insulin. Type 1 diabetes is usually diagnosed in children and young adults, although it can appear at any age. People with type 1 diabetes need to take insulin every day to stay alive.')

            st.subheader('b) Type 2 Diabetes')
            # st.markdown(' ')
            st.markdown('If you have type 2 diabetes, your body does not make or use insulin well. You can develop type 2 diabetes at any age, even during childhood. However, this type of diabetes occurs most often in middle-aged and older people. Type 2 is the most common type of diabetes.')

            st.subheader('c) Gestational Diabetes')
            # st.markdown(' ')
            st.markdown('Gestational diabetes develops in some women when they are pregnant. Most of the time, this type of diabetes goes away after the baby is born. However, if you’ve had gestational diabetes, you have a greater chance of developing type 2 diabetes later in life. Sometimes diabetes diagnosed during pregnancy is actually type 2 diabetes.')

            st.subheader('c) other types of Diabetes')
            st.markdown('Less common types include monogenic diabetes, which is an inherited form of diabetes, and cystic fibrosis-related diabetes.')
            st.markdown(' ')

            st.title('How common is Diabetes?')
            st.markdown('The rate of diabetes diagnoses is increasing around the world, including in India. India has the second-highest total population in the world at more than 1.3 billion people. The International Diabetes Federation estimated that **:red[72.9 million adults]** in India were living with diabetes in 2017. A 2017 study also found that diabetes prevalenceTrusted Source was higher in urban areas.')




            df = pd.read_csv('data/analysis.csv')

            # Convert year column to datetime type
            df['year'] = pd.to_datetime(df['year'], format='%Y')

            # Create a line chart using Altair
            chart = alt.Chart(df).mark_line().encode(
            x=alt.X('year', axis=alt.Axis(title='Year')),
            y=alt.Y('population_diabetes', axis=alt.Axis(title='Population Diabetes')),
            tooltip=[alt.Tooltip('year', format='%Y'), alt.Tooltip('population_diabetes', format=',')]
            ).properties(
            width=700,
            height=400
            )

            # Show the chart in Streamlit
            st.altair_chart(chart, use_container_width=True)
            # st.markdown('<center>**:red[Diabetes report of India 2000-2045]**</center>', unsafe_allow_html=True)
            st.markdown("<center><span style='color:green'>Diabetes report of India 2000-2045</span></center>", unsafe_allow_html=True)

            st.markdown(' ')
            st.title('Who is more likely to develop type 2 diabetes?')
            st.markdown('You are more likely to develop type 2 diabetes if you are age 45 or older, have a family history of diabetes, or are overweight. Physical inactivity, race, and certain health problems such as high blood pressure also affect your chance of developing type 2 diabetes. You are also more likely to develop type 2 diabetes if you have prediabetes or had gestational diabetes when you were pregnant. Learn more about risk factors for type 2 diabetes.')



            st.title('What health problems can people with diabetes develop?')
            st.markdown('Over time, high blood glucose leads to problems such as')
            st.markdown('🔴 Heart disease')
            st.markdown('🔴 Stroke')
            st.markdown('🔴 Kidney disease')
            st.markdown('🔴 Eye problems')
            st.markdown('🔴 Dental disease')
            st.markdown('🔴 Nerve damage')
            st.markdown('🔴 Foot problems')






