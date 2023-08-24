import streamlit as st

# Create your title, header, and subheader
st.title("Welcome to playground")
st.header("This is a demo by Rishab")
st.subheader("Enjoy !")

# Play with some nifty text
st.text('''
        Hello World.
        
        Hi my name is Rishabh. 
        I am trying to learn Streamlit.
        
        Cheers !!!
        ''')

#Add a divider!
st.divider()

# Create a button
button_celebrate = st.button(label="Celebrate")
# Add an action to your button - the best action in streamlit
if button_celebrate : 
    st.balloons()

#Show the code! 
button_snow = st.button(label="Snow")
with st.echo() : 
    if button_snow : 
        st.snow()

st.divider()


# Lets try to make a clicker counter! Create an empty placeholder, a counter, and a button


button_counter1 = st.button(label="Click-1") # Add the button action
counter1 = 0 # Create a counter 
text1 = st.empty() # Create an updateable placeholder

# (SPOILER ALERT!) Doesn't work?! What's wrong!
with st.echo():
    if button_counter1 : 
        text1.write(f'Button-1 clicked {counter1} times')


# Use the session state
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0 

button_counter2 = st.button(label="Click-2") # Add the button action
text2 = st.empty() # Create an updateable placeholder

# Recreate the button and assign the action
with st.echo() : 
    if button_counter2 : 
        st.session_state.counter += 1
        text2.write(f'Button-2 clicked {st.session_state.counter} times')

st.divider()