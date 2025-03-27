import streamlit as st
import matplotlib.pyplot as plt

# ----------------------------#
# 🔹 Initialize Session State for Dark Mode
# ----------------------------#
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Function to toggle Dark Mode
def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Sidebar Dark Mode Toggle Button
st.sidebar.button("🌙 Toggle Dark Mode", on_click=toggle_dark_mode)

# ----------------------------#
# 🔹 Apply Dark Mode Styles Globally
# ----------------------------#
dark_bg = "#1E1E1E" if st.session_state.dark_mode else "#FFFFFF"
text_color = "#FFFFFF" if st.session_state.dark_mode else "#000000"
button_color = "#F1C40F" if st.session_state.dark_mode else "#007BFF"
slider_color = "#F39C12" if st.session_state.dark_mode else "#007BFF"
table_bg = "#333333" if st.session_state.dark_mode else "#f5eef8"  # Adjusting for visibility
table_text_color = "#FFFFFF" if st.session_state.dark_mode else "#000000"

st.markdown(f"""
    <style>
        body, .stApp {{
            background-color: {dark_bg} !important;
            color: {text_color} !important;
        }}
        .title {{
            color: {'#F1C40F' if st.session_state.dark_mode else '#000000'};
            text-align: center;
        }}
        .bmi-value {{
            color: {text_color};
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            background-color: {'#444444' if st.session_state.dark_mode else '#f4ecf7'};
            padding: 10px;
            border-radius: 10px;
            margin-top: 10px;
        }}
        .category {{
    font-weight: bold;
    padding: 8px 15px;
    border-radius: 5px;
    display: inline-block;
    margin-top: 10px;
    color: black !important;
}}

        .underweight {{ background-color: #f9e79f; }}
        .normal {{ background-color: #d4efdf; }}
        .overweight {{ background-color: #fadbd8; }}
        .obesity {{ background-color: #edbb99; }}
        .stButton>button {{
            background-color: {button_color};
            color: black;
            display: block;
            margin: auto;
            text-align: center;
        }}
        .stSlider label {{
            color: {text_color} !important;
        }}
        .stSlider .css-1aumxhk {{
            color: {slider_color};
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: {table_bg} !important;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
            color: {table_text_color}; 
        }}
        th {{
            background-color: {'#555555' if st.session_state.dark_mode else '#f4ecf7'};
            color: {text_color};
        }}
    </style>
""", unsafe_allow_html=True)

# ----------------------------#
# 🔹 App Title
# ----------------------------#
st.markdown('<h1 class="title">🎯 Smart BMI Calculator</h1>', unsafe_allow_html=True)

# ----------------------------#
# 🔹 Side-by-Side Sliders for Height & Weight
# ----------------------------#
col1, col2 = st.columns(2)

with col1:
    height = st.slider('📏 Height (cm)', 100, 250, 170)

with col2:
    weight = st.slider('⚖️ Weight (kg)', 30, 200, 70)

# ----------------------------#
# 🔹 BMI Calculation & Categorization
# ----------------------------#
bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    category = "Underweight"
    class_name = "underweight"
    health_tip = "🍏 Try increasing your calorie intake with nutrient-rich foods."
elif 18.5 <= bmi < 25:
    category = "Normal Weight"
    class_name = "normal"
    health_tip = "💪 Keep up with a balanced diet and regular exercise."
elif 25 <= bmi < 30:
    category = "Overweight"
    class_name = "overweight"
    health_tip = "🥗 Focus on a healthy diet and increase your physical activity."
else:
    category = "Obesity"
    class_name = "obesity"
    health_tip = "🚴 Consider consulting a doctor for a personalized weight management plan."

# ----------------------------#
# 🔹 Display BMI Result
# ----------------------------#
st.markdown(f"""
    <p class="bmi-value">Your BMI: {bmi:.2f}</p>
    <p class="category {class_name}">{category}</p>
""", unsafe_allow_html=True)

# Display Health Tip
st.markdown(f"**Health Tip:** {health_tip}")

# ----------------------------#
# 🔹 BMI Guide Table
# ----------------------------#
st.markdown(f"""
    <h2 style='text-align: center; color: {text_color};'>📌 BMI Guide</h2>
    <table>
        <tr>
            <th>BMI Range</th>
            <th>Category</th>
            <th>Health Risk</th>
        </tr>
        <tr>
            <td>&lt; 18.5</td>
            <td class="underweight">Underweight</td>
            <td>Possible nutritional deficiency & weakened immune system</td>
        </tr>
        <tr>
            <td>18.5 - 24.9</td>
            <td class="normal">Normal Weight</td>
            <td>Low risk (Healthy Range)</td>
        </tr>
        <tr>
            <td>25 - 29.9</td>
            <td class="overweight">Overweight</td>
            <td>Increased risk of cardiovascular diseases</td>
        </tr>
        <tr>
            <td>≥ 30</td>
            <td class="obesity">Obesity</td>
            <td>High risk of heart disease, diabetes, & hypertension</td>
        </tr>
    </table>
""", unsafe_allow_html=True)
