import streamlit as st
import helper
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="AI Duplicate Detector",
    page_icon="🤖",
    layout="centered"
)

# 🔥 PREMIUM CSS
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    font-family: 'Segoe UI', sans-serif;
}

/* Center Card */
.block-container {
    
    max-width: 900px;
    margin: auto;
    margin-top: 70px;


    background: rgba(255, 255, 255, 0.05);
    padding: 2rem 3rem;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* Title */
h1, h2, h3 {
    text-align: center;
    color: white;
}

/* Inputs */
.stTextInput > div > div > input {
    background-color: rgba(255,255,255,0.1);
    color: white;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.2);
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
}

/* Result Box */
.result-box {
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
}

.success {
    background: rgba(0,255,0,0.1);
    color: #00ffcc;
    border: 1px solid #00ffcc;
}

.error {
    background: rgba(255,0,0,0.1);
    color: #ff4c4c;
    border: 1px solid #ff4c4c;
}

/* Footer */
.footer {
    text-align: center;
    color: #aaa;
    margin-top: 30px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown("# 🤖 Duplicate Question Detector")
st.markdown("### Smart NLP system to detect similar questions")

# Sidebar
st.sidebar.title("⚙️ Settings")
st.sidebar.markdown("Customize your experience")


# Inputs
q1 = st.text_input("📝 Enter Question 1")
q2 = st.text_input("📝 Enter Question 2")

# Analyze button
if st.button("🚀 Analyze"):
    if q1.strip() == "" or q2.strip() == "":
        st.warning("⚠️ Please enter both questions")
    else:
        with st.spinner("Analyzing with AI... 🤖"):
            query = helper.query_point_creator(q1, q2)
            result = model.predict(query)[0]

            # If your model supports probability
            try:
                prob = model.predict_proba(query)[0][1]
            except:
                prob = None

        if result:
            st.markdown(
                '<div class="result-box success">✅ Duplicate Questions</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="result-box error">❌ Not Duplicate</div>',
                unsafe_allow_html=True
            )


# Footer
st.markdown('<div class="footer">🚀 Built with Streamlit + ML + NLP</div>', unsafe_allow_html=True)