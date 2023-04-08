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

st.header('Solar Energy')

st.selectbox('Capacity Calculation',
             ['Central Capacity', 'Power Input (Pin)', 'Power Output (P)', 'Efficiency', 'Irradiance (G)',
              'Temperature (T)'])
