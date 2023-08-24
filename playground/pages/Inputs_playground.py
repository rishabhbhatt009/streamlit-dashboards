import streamlit as st

st.title("Input Playground")

############################################################################
# Set the options and the questions

viz_lib = ["Matplotlib", "Bokeh", "Altair", "Plotly"]
question = "What's your favourite viz library?"

############################################################################
st.divider()
st.header("Radio Buttons")
st.subheader("You can only pick one")

viz_selected_radio = st.radio(label=question, options=viz_lib)
st.write(f'Your fav viz is **{viz_selected_radio}**')

############################################################################
st.divider()
st.header("Drop down box aka select box")
st.subheader("You can only pick one")

viz_selected_drop_down = st.selectbox(label=question, options=viz_lib)
st.write(f'Your fav viz is **{viz_selected_drop_down}**')

############################################################################
st.divider()
st.header("Multi select")
st.subheader("You can pick many")

viz_selected_multi = st.multiselect(label=question, options=viz_lib)
st.write(f'Your fav viz is **{viz_selected_multi}**')

############################################################################
st.divider()
st.header("Checkboxes")

# Create a dictionary of the labels and the current state
options = {option: False for option in viz_lib}

# Loop through the dictionary to create the checkbox and write the current value
for key,val in options.items():
    options[key] = st.checkbox(label=key)

output = ','.join([key for key,val in options.items() if val==True])

st.write(f'Your fav viz is **{output if output else "None"}**')

############################################################################
st.divider()
st.header("Sliders")

st.slider(label='This is a slider', 
          min_value=0, 
          max_value=100, 
          value=50,
          format='%d%%',
          help='Slide away !'
          )

############################################################################
st.divider()
st.header("Item Sliders")

slider_item = st.select_slider(
    label = f"How much do you like {viz_selected_drop_down}",
    options = ['Very Much', 'Somewhat', 'A little', 'Not at all']
)

st.write(f"You like {viz_selected_drop_down} {slider_item.lower()}!")


############################################################################
st.divider()
st.header("Text inputs")

user_text = st.text_input(label=question)

############################################################################
st.divider()
st.header("Text Area")
user_text_large = st.text_area(label=question)

############################################################################
st.divider()
st.header("Number inputs")
user_number = st.number_input(label='Write a number')

############################################################################
st.divider()
st.header("Dates")
user_data = st.date_input(label='Enter a date')

############################################################################
