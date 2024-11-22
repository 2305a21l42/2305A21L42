import streamlit as st

# Function to calculate I, P, and H
def Elec_Para(V, R, T):
    I = V / R  # Current (I)
    P = I**2 * R  # Power (P)
    H = I**2 * R * T  # Heat energy (H)
    return I, P, H

# Set up the Streamlit application title
st.title("2305A21L42-PS1")  # Replace with your own Roll No. and Problem Statement No.
st.write("This Application is useful for calculating current through a load,power drawn by the load,and heat energy generated")
# Add inputs for Voltage (V), Resistance (R), and Time (T)
V = st.number_input("Enter Voltage (V) in volts", value=230.0)
R = st.number_input("Enter Resistance (R) in ohms", value=10.0)
T = st.number_input("Enter Time (T) in seconds", value=60)
st.button("compute")

# Call the Elec_Para function to calculate I, P, and H
I, P, H = Elec_Para(V, R, T)

# Display the results
st.subheader("Calculated Electrical Parameters")
st.write(f"Current (I) = {I} A")
st.write(f"Power (P) = {P} W")
st.write(f"Heat Energy (H) = {H} Joules")
