import streamlit as st

def convert_unit(value, unit_from, unit_to):
    # Define conversion factors for different units
    conversions = {
        "meter": 1,
        "kilometer": 1000,
        "gram": 1,
        "kilogram": 1000
    }
    
    # Check if the units are valid
    if unit_from not in conversions or unit_to not in conversions:
        return "Invalid units"
    
    # Convert the value from 'unit_from' to meters (base unit)
    value_in_base_unit = value * conversions[unit_from]
    
    # Convert the value in meters to the target 'unit_to'
    converted_value = value_in_base_unit / conversions[unit_to]
    
    return converted_value

# Streamlit UI
st.title("Unit Converter")

value = st.number_input("Enter the value", min_value=0.0, format="%.2f")

unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])

unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")
