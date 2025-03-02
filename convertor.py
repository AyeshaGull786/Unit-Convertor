#I am creating a unit convertor with the help of streamlit  and python
import pyfiglet
import streamlit as st 
st.markdown(
    """
    <style>
    body{
        background color: #1e1e2f;
        color: white:
    }
    .stApp{
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3); 
    }
    h1{
        text-align: center;
        font-size: 36px;
        text-color: #1e1e2f;
        padding-bottom: 100px;
    }
    .stButton>button{
        background: linear gradient(45 deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        paggingL 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4); 
    }
    .stButton>button:hover{
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box{
        font-size: 20px;
        font-weight: bold;
        text-align:center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        color: #00c9ff;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
   .footer{
       text-align: center;
       margin-top: 150px;
       font-size: 14px;
       color: black;
   }
   </style>
    """,
    unsafe_allow_html= True
)

#we r going to give a title and description of project
st.markdown("<h1> 👾 ᑌᑎIT ᑕOᑎᐯEᖇTOᖇ (ಠ‿ಠ) </h1>", unsafe_allow_html= True)
st.write("✔️ You can easily convert units from one to another like Length, Weight, Temperature, etc.")

#We are going to create a sidebar for the user to select the unit category and the units.
conversion_type = st.sidebar.selectbox("🖇Select the Conversion Types", ["Length", "Weight", "Temperature"])
value = st.number_input("✏️ Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters","Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers",  "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"] )
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        
        
#We are going to create a function to convert the units
def length_convertor(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000, 'Miles': 0.000621371, 
        'Yards': 1.09361, 'Feet':3.28084, 'Inches': 39.37
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1, 'Grams': 1000, 'Miligrams': 1000000, 'Pounds': 2.2046, 'Ounces': 35.27, 
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return(value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit  == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value 

#buttons to perform the conversion
if st.button(" 🔘Convert"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_convertor(value, from_unit, to_unit)
        
    st.markdown(f"<div class= 'result-box'>{value} {from_unit} = {result: .4f} {to_unit}</div>", unsafe_allow_html=True)
    
st.markdown("<div class ='footer'> ｡⚛  🎀  𝓒𝓻𝓮𝓪𝓽𝓮𝓭 𝓫𝔂 𝓐𝔂𝓮𝓼𝓱𝓪 𝓖𝓾𝓵𝓵 🎀  ⚛｡</div>", unsafe_allow_html=True) 
            
    