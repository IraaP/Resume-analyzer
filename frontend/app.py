import streamlit as st
import requests

st.title("AI-Powered Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=['pdf'])

if uploaded_file is not None:
    st.write("Analyzing resume...")

    # Send file to backend
    files = {'resume': uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:5000/analyze", files=files)

    if response.status_code == 200:
        result = response.json()
        st.subheader("Analysis Results")
        st.write(f"📌 **Job Match Score:** {result['job_match_score']}%")
        st.write(f"📌 **Readability Score:** {result['readability_score']}")

        if result['missing_skills']:
            st.write("🚀 **Suggested Skills to Learn:**")
            st.write(", ".join(result['missing_skills']))
    else:
        st.error("Error analyzing resume.")