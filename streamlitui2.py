import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="Happy Birthday Aditi ❤️",
    page_icon="🎂",
    layout="centered"
)

# Title
st.markdown(
    """
    <h1 style='text-align:center; color:#ff4b4b;'>
        🎉 Happy Birthday Aditi Shrivastava 🎉
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# Love message
st.markdown(
    """
    <h3 style='text-align:center;'>
        To the most beautiful part of my life ❤️
    </h3>
    <p style='text-align:center; font-size:18px;'>
        Aditi, you make my world brighter every single day.<br>
        Your smile is my favorite place to be.<br><br>
        💖 I LOVE YOU 💖
    </p>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Proposal section
st.markdown(
    """
    <h2 style='text-align:center; color:#e91e63;'>
        💍 Will You Be Mine Forever? 💍
    </h2>
    <p style='text-align:center; font-size:18px;'>
        Aditi Shrivastava,<br>
        I want to hold your hand through every smile and every dream.<br>
        Will you accept my love today and always? ❤️
    </p>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Dancing character Bhanu
st.markdown(
    """
    <h2 style='text-align:center;'>
        🕺 Bhanu is Dancing for You 🕺
    </h2>
    <p style='text-align:center;'>
        Because today is special 🎂
    </p>
    """,
    unsafe_allow_html=True
)

dance_area = st.empty()

dance_frames = [
    "🕺🎶   Bhanu is dancing 💃",
    "💃🎶   Bhanu is dancing 🕺",
    "🕺✨   Bhanu is dancing 💖",
    "💃✨   Bhanu is dancing 🎉",
]

for _ in range(3):  # number of dance loops
    for frame in dance_frames:
        dance_area.markdown(
            f"<h3 style='text-align:center;'>{frame}</h3>",
            unsafe_allow_html=True
        )
        time.sleep(0.6)

# Celebration effects
st.balloons()

st.markdown(
    """
    <h3 style='text-align:center; color:#ff1493;'>
        🎂 Happy Birthday My Love 🎂<br>
        — From Bhanu ❤️
    </h3>
    """,
    unsafe_allow_html=True
)
