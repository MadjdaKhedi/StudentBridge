# app.py
import streamlit as st
import os

st.title("🇨🇳 Scholarship Registration Form")

with st.form("register"):
    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    dob = st.date_input("Date of Birth")
    nationality = st.text_input("Nationality")
    major = st.text_input("Intended Major")
    level = st.selectbox("Level of Study", ["Bachelor", "Master", "PhD"])
    preferred_uni = st.text_input("Preferred University (Optional)")

    passport = st.file_uploader("Upload Passport", type=["pdf", "jpg", "png"])
    transcripts = st.file_uploader("Upload Transcripts", type=["pdf", "jpg", "png"])
    degree = st.file_uploader("Upload Degree Certificate", type=["pdf", "jpg", "png"])
    statement = st.file_uploader("Personal Statement (Optional)", type=["pdf", "docx"])

    submitted = st.form_submit_button("Submit")

    if submitted:
        if not (full_name and email and phone and dob and nationality and major and level and passport and transcripts and degree):
            st.warning("Please fill all required fields and upload mandatory documents.")
        else:
            folder = f"submissions/{email.replace('@', '_')}/"
            os.makedirs(folder, exist_ok=True)
            with open(os.path.join(folder, "passport_" + passport.name), "wb") as f:
                f.write(passport.read())
            with open(os.path.join(folder, "transcripts_" + transcripts.name), "wb") as f:
                f.write(transcripts.read())
            with open(os.path.join(folder, "degree_" + degree.name), "wb") as f:
                f.write(degree.read())
            if statement:
                with open(os.path.join(folder, "statement_" + statement.name), "wb") as f:
                    f.write(statement.read())

            st.success("✅ Registration submitted successfully!")
