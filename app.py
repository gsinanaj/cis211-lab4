# CIS 211 Lab 4 starter
# Campus Basketball Club

import streamlit as st


club_info = {
    "name": "Campus Basketball Club",
    "day": "Tuesday",
    "time": "6:00 PM",
}



activities = [
    "Full Court 5v5 Basketball Games",
    "Skills Training",
    "Basketball Related Contests for Prizes",
]

st.title(club_info["name"])
st.caption("A fictional CIS 211 course project. These are not real campus arrangements.")




st.header("About Our Club")
st.markdown("""
The **Campus Basketball Club** is the perfect place for college students to ease their mind off school. Our club organizes pickup games, tournaments, and skillwork sessions where students
can sharpen themselves as players and compete in a *friendly environment*.
We welcome students of all skill levels, whether they are experienced players
or just looking to have fun.
""")


st.header("Our Activities")
# This loop displays the club activities.
for activity in activities:
    st.write(activity)

st.header("Club Information")
# This displays the meeting day and time.
st.write("Meeting Day:", club_info["day"])
st.write("Meeting Time:", club_info["time"])

st.header("What to Bring")
st.markdown("""
- Basketball Shoes
- Comfortable Athletic Clothes
- Signed Waiver

Learn more about club basketball at the [NIRSA website]https://nirsa.net/).
""")


