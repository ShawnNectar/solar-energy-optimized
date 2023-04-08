import numpy as np
import streamlit as st

hidden_from_streamlit = '''

    IMPORTANT VALUES

    Capacity = (P / Pin) x (G / Gin) x (T / Tin)
        Unity: W/m^2
        P = W                   Power Output
        Pin = W                 Power Input
        G = W/m^2               Irradiance on Solar Panel
        Gin = W/m^2             Irradiance Standard Condition
        T = °C                  Cell Temperature
        Tin = °C                Cell Temperature Standard Condition
        Efficiency = %          Efficiency of Solar Panel

    Power Input:
        Pin = P / (G / Gin) x (T / Tin) x Efficiency
            Unity: W
            P = W               Power Output
            G = W/m^2           Irradiance on Solar Panel
            Gin = W/m^2         Irradiance Standard Condition
            T = °C              Cell Temperature
            Tin = °C            Cell Temperature Standard Condition
            Efficiency = %      Efficiency of Solar Panel


    Efficiency = (P / (G x A)) x 100%
        Unity: %
        P = W                   Power Output
        G = W/m^2               Irradiance on Solar Panel
        A = m^2                 Area of Solar Panel

    Power Output:
        P = Isc x Voc x FF x G/Gref x T/Tref
            Unity: W
            Isc = A             Short-Circuit Current
            Voc = V             Open-Circuit Voltage
            FF = dimensionless  Fill Factor
            Gref = W/m^2        Reference Irradiance
            Tref = °C           Reference Temperature

    Irradiance on solar panel:
        G = G0 x cos(θ)
            Unity: W/m^2
            G0 = W/m^2          Solar Constant
            θ = degrees         Angle of Incidence of Sunlight on The Solar Panel

    Temperature:
        T = Ta + (NOCT - 20) x G/Gref x (1 - H/100) / 800
            Unity: °C
            Ta = °C             Ambient Temperature
            NOCT = °C           Nominal Operating Cell Temperature
            Gref = W/m^2        Reference Irradiance
            H = %               Relative humidity


    '''

# Gin and Tin Standard Value in case of a Non-Input
Gin = 1000
Tin = 25

# Base st.text
text_one = "If you don't have Pin, P, Efficiency, Irradiance or T values, go to 'Calculators'"

text_two = "The Gin and Tin's values are available on manufacturer's guide"

text_three = "If not, the standard values will be Gin = 1000W/m2 and Tin = 25°C"

text_four = "NO VALUES CAN BE ZERO!"

st.header('Solar Energy')

# Quick pick to calculator, the main is 'Central Capacity', the others are support calculators
page_selection_calculator = st.selectbox('Calculators',
                                         ['Central Capacity', 'Power Input (Pin)', 'Power Output (P)', 'Efficiency',
                                          'Irradiance (G)', 'Temperature (T)'])

if page_selection_calculator == 'Central Capacity':
    st.write('Central Capacity')

    # Receiving the variables values from user
    P = st.number_input('Power Output')
    Pin = st.number_input('Power Input')
    G = st.number_input('Irradiance on Solar Panel')
    Gin = st.number_input('Irradiance Standard Condition')
    T = st.number_input('Cell Temperature')
    Tin = st.number_input('Cell Temperature Standard Condition')

    text_show_one = st.text(text_one)
    text_show_two = st.text(text_two)
    text_show_three = st.text(text_three)
    text_show_four = st.text(text_four)

    # Checking if the values are functional
    if P and Pin and G and Gin and T and Tin:
        # Applying the capacity formula -> Capacity = (P / Pin) x (G / Gin) x (T / Tin)
        capacity = np.divide(P, Pin) * np.divide(G, Gin) * np.divide(T, Tin)

        if st.button('Calculate'):
            # Removing text_one, text_two and text_three after clicking the button
            text_show_one.empty()
            text_show_two.empty()
            text_show_three.empty()
            text_show_four.empty()

            # Showing the results
            st.write(f'The solar panel capacity is {capacity} W/m^2')
            st.write(f"It means that each meter square of solar panel you will have {capacity} Watts")

if page_selection_calculator == 'Power Input (Pin)':
    st.write('Power Input')

    # Receiving the variables values from user
    P = st.number_input('Power Output')
    G = st.number_input('Irradiance on Solar Panel')
    Gin = st.number_input('Irradiance Standard Condition')
    T = st.number_input('Cell Temperature')
    Tin = st.number_input('Cell Temperature Standard Condition')
    Efficiency = st.number_input('Efficiency of Solar Panel')

    text_show_four = st.text(text_four)

    # Checking if the values are functional
    if P and G and Gin and T and Tin and Efficiency:
        # Applying the Power Input formula -> Pin = P / (G / Gin) x (T / Tin) x Efficiency
        Pin = np.multiply(np.divide(P, np.divide(G, Gin)), np.multiply(np.divide(T, Tin), Efficiency))

        if st.button('Calculate'):
            # Removing text_four after calculated
            text_show_four.empty()

            # Showing Results
            st.write(f"The Power Input (Pin) is {Pin} W")

if page_selection_calculator == 'Power Output (P)':
    st.write('Power Output')

if page_selection_calculator == 'Efficiency':
    st.write('Efficiency')

if page_selection_calculator == 'Irradiance (G)':
    st.write('Irradiance')

if page_selection_calculator == 'Temperature (T)':
    st.write('Temperature')
