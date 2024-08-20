import streamlit as st


# 9_layout.py



left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('press me!')


# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")






