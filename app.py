# app.py
import streamlit as st
import os
import datetime

st.set_page_config(page_title="Scholarship Registration", layout="centered")
st.title("🇨🇳 Scholarship Registration Form")

with st.form("register"):
    # Personal Details
    full_name         = st.text_input("Full Name", max_chars=100)
    email             = st.text_input("Email")
    phone             = st.text_input("Phone Number")
    dob               = st.date_input(
        "Date of Birth", 
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date.today()
    )
    age = datetime.date.today().year - dob.year
    residency         = st.radio("Do you have residency in China?", ["Yes", "No"])
    nationality       = st.text_input("Nationality")
    country_of_origin = st.text_input("Country of Origin (if different)")
    previous_uni      = st.text_input("Name of Previous University")

    # Academic Details
    current_inst      = st.text_input("Current Institution")
    level_completed   = st.selectbox("Highest Level Completed", 
                            ["", "High School", "Bachelor", "Master", "PhD"])
    gpa               = st.text_input("GPA / Academic Score")
    intended_major    = st.text_input("Intended Major")
    study_level       = st.selectbox("Program Applying For", 
                            ["Bachelor", "Master", "Doctoral", "Chinese Language Program"])
    preferred_uni     = st.text_input("Preferred University (Optional)")
    english_score     = st.text_input("TOEFL / IELTS Score (Optional)")
    hsk_level         = st.selectbox("HSK Level (Optional)", 
                            ["", "HSK 1", "HSK 2", "HSK 3", "HSK 4", "HSK 5", "HSK 6"])

    # Funding Details
    funding_type      = st.radio("Funding Type", ["Scholarship", "Self-funded"])
    sponsor_info      = ""
    if funding_type == "Self-funded":
        sponsor_info  = st.text_input("Sponsor Name and Relationship")

    # Parent/Guardian Details
    st.markdown("---")
    st.subheader("Parent/Guardian Information")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Mother**")
        mother_name     = st.text_input("Mother's Full Name")
        mother_work     = st.text_input("Mother's Workplace")
        mother_position = st.text_input("Mother's Position")
    with col2:
        mother_phone    = st.text_input("Mother's Phone Number")
        mother_email    = st.text_input("Mother's Email")

    col3, col4 = st.columns(2)
    with col3:
        st.write("**Father**")
        father_name     = st.text_input("Father's Full Name")
        father_work     = st.text_input("Father's Workplace")
        father_position = st.text_input("Father's Position")
    with col4:
        father_phone    = st.text_input("Father's Phone Number")
        father_email    = st.text_input("Father's Email")

    # File Uploads
    passport         = st.file_uploader("Upload Passport", type=["pdf","jpg","png"])
    transcripts      = st.file_uploader("Upload Transcripts", type=["pdf","jpg","png"])
    degree           = st.file_uploader("Upload Degree Certificate", type=["pdf","jpg","png"])
    bank_statement   = st.file_uploader("Upload Bank Statement", type=["pdf","jpg","png"])
    cv               = st.file_uploader("Upload CV / Resume", type=["pdf","doc","docx"])
    recomm_letters   = st.file_uploader(
                          "Upload Recommendation Letters", 
                          type=["pdf","doc","docx"], 
                          accept_multiple_files=True)
    statement_doc    = st.file_uploader("Personal Statement (Optional)", type=["pdf","docx"])

    submitted = st.form_submit_button("Submit Application")

    if submitted:
        required = [
            full_name, email, phone, dob, nationality,
            current_inst, level_completed, gpa,
            intended_major, study_level,
            passport, transcripts, degree, bank_statement, cv
        ]
        if not all(required):
            st.warning("Please fill all required fields and upload mandatory documents.")
        else:
            # Prepare submission folder
            folder = os.path.join("submissions", email.replace("@","_"))
            os.makedirs(folder, exist_ok=True)

            def save_file(uploader, prefix=""):
                if uploader:
                    path = os.path.join(folder, f"{prefix}{uploader.name}")
                    with open(path, "wb") as f:
                        f.write(uploader.read())

            # Save all files
            save_file(passport, "passport_")
            save_file(transcripts, "transcripts_")
            save_file(degree, "degree_")
            save_file(bank_statement, "bank_")
            save_file(cv, "cv_")
            save_file(statement_doc, "statement_")
            for idx, letter in enumerate(recomm_letters or []):
                path = os.path.join(folder, f"recommendation_{idx+1}_{letter.name}")
                with open(path, "wb") as f:
                    f.write(letter.read())

            # Save form data as JSON (optional)
            data = {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "dob": str(dob),
                "age": age,
                "residency": residency,
                "nationality": nationality,
                "country_of_origin": country_of_origin,
                "previous_university": previous_uni,
                "current_institution": current_inst,
                "level_completed": level_completed,
                "gpa": gpa,
                "intended_major": intended_major,
                "study_level": study_level,
                "preferred_university": preferred_uni,
                "english_score": english_score,
                "hsk_level": hsk_level,
                "funding_type": funding_type,
                "sponsor_info": sponsor_info,
                "mother_info": {
                    "name": mother_name,
                    "work": mother_work,
                    "position": mother_position,
                    "phone": mother_phone,
                    "email": mother_email
                },
                "father_info": {
                    "name": father_name,
                    "work": father_work,
                    "position": father_position,
                    "phone": father_phone,
                    "email": father_email
                }
            }
            with open(os.path.join(folder, "data.json"), "w") as f:
                import json
                json.dump(data, f, indent=2)

            st.success("✅ Registration submitted successfully!")
