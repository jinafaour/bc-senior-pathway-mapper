import streamlit as st

st.title("BC Senior Pathway Mapper (Grades 10-12)")
st.write("Map your cognitive profile to senior secondary prerequisites.")

profile_code = st.selectbox("Select Your Pathfinder Profile Code", ["PA", "AC", "SC", "AN", "AP", "CA", "SA", "NA", "NP", "PN"])
target_field = st.selectbox("Select Target Post-Secondary Field", ["Engineering / Applied Science", "Health Sciences", "Business / Commerce", "Computer Science"])

if st.button("Generate Pathway"):
    st.markdown("---")
    st.subheader(f"Recommended Roadmap for Profile: {profile_code}")
    
    if target_field == "Engineering / Applied Science":
        st.write("**Grade 10:** Pre-Calculus 10, Science 10, ADST Electronics/Metal")
        st.write("**Grade 11:** Pre-Calculus 11, Physics 11, Chemistry 11, English Studies 11")
        st.write("**Grade 12:** Calculus 12, Pre-Calculus 12, Physics 12, Chemistry 12, English 12")
    elif target_field == "Health Sciences":
        st.write("**Grade 10:** Pre-Calculus 10, Science 10")
        st.write("**Grade 11:** Pre-Calculus 11, Chemistry 11, Life Sciences 11 (Biology), English Studies 11")
        st.write("**Grade 12:** Pre-Calculus 12, Anatomy & Physiology 12, Chemistry 12, English 12")
    else:
        st.write("**Grade 10:** Foundations of Math 10, Science 10")
        st.write("**Grade 11:** Foundations of Math 11, English Studies 11, Modern Languages/Arts")
        st.write("**Grade 12:** Foundations of Math 12 / Pre-Calculus 12, English 12, Grade 12 Electives")
