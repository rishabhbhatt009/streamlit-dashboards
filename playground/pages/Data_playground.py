import numpy as np
import pandas as pd
import streamlit as st

# Create your titile, header, and subheader
st.title("Let's play with some data!")

# Create a random dataframe
n_cols = 5
df = pd.DataFrame(np.random.randn(20, n_cols), columns=[f"col{i}" for i in range(n_cols)])

############################################################################
st.header("A dataframe written using st.write()")
st.write(df)

############################################################################
st.header("A sortable dataframe written using st.dataframe()")
st.subheader("We can control width when using st.dataframe()")
st.dataframe(df)

############################################################################
st.header("A static table, created from a dataframe, written using st.table()")
st.table(df)

############################################################################
st.header("Editable Dataframes!")
viz_libs = pd.DataFrame(
    [
        {"library": "Plotly", "rating": np.NaN, "used? 🎈": False},
        {"library": "Altair", "rating": np.NaN, "used? 🎈": False},
        {"library": "Matplotlib", "rating": np.NaN, "used? 🎈": False}
    ]
)

edited_df = st.data_editor(data=viz_libs, num_rows='dynamic')

if edited_df['rating'].isna().all():
    favorite_library = "a mystery as you haven't rated anything!"
else:
    favorite_library = edited_df.loc[edited_df["rating"].idxmax()]["library"]

st.write(f"Your favorite library is {favorite_library}")

############################################################################
# download button
st.download_button(label='Download Table',
                   data=edited_df.to_csv(),
                   file_name='dataframe.csv',
                   mime='text/csv'
                   )