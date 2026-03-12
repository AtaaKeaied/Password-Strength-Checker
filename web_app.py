import streamlit as st
import re
import random
import string

st.set_page_config(
    page_title="Password Shield",
    page_icon="🛡️",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 40
    elif len(password) >= 8:
        score += 20
    else:
        feedback.append("Minimum 8 characters recommended.")
        
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 20
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    if re.search("[0-9]", password):
        score += 20
    else:
        feedback.append("Add at least one number.")
        
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        feedback.append("Use special characters (e.g., @, #, $).")
        
    return score, feedback

def generate_secure_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

st.title("🛡️ Password Security Toolkit")
st.subheader("Advanced analysis & secure generation tool")

user_pass = st.text_input("Enter your password to test:", type="password")

if user_pass:
    final_score, all_notes = check_password_strength(user_pass)
    st.write(f"### Security Score: {final_score}/100")
    st.progress(final_score / 100)
    
    if final_score >= 80:
        st.success("Rating: VERY STRONG ✅")
    elif final_score >= 50:
        st.warning("Rating: MODERATE ⚠️")
    else:
        st.error("Rating: WEAK ❌")
        
    if all_notes:
        with st.expander("Suggestions:"):
            for note in all_notes:
                st.write(f"- {note}")

st.markdown("---")

st.write("### ✨ Need a secure suggestion?")
if st.button("Generate Random Strong Password"):
    new_password = generate_secure_password()
    st.success("Generated Password:")
    st.code(new_password, language=None)

st.markdown("---")
st.caption("University Project | Cybersecurity Research Group")
