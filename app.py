# CIS 211 Lab 4 starter
# Youth Basketball Club

import streamlit as st


club_info = {
    "name": "Youth Basketball Club",
    "day": "Saturday",
    "time": "11:00 PM",
}



activities = [
    "Friendly Basketball Games",
    "Skills Training",
    "Team Bonding and Sportsmanship",
]

st.title(club_info["name"])
st.caption("A fictional CIS 211 course project. These are not real campus arrangements.")




st.header("About Our Club")
st.markdown("""
The **Youth Basketball Club** is a place where young players can come together
to improve their basketball skills and learn more about the game.
Our goal is to help players become better at basketball while also teaching
them the importance of *teamwork and sportsmanship*.
We welcome players of all skill levels who want to learn and have fun.
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
- A Water Bottle

Learn more about youth basketball at the [Jr. NBA website](https://jr.nba.com/).
""")


