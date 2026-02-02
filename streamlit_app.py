import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
#fine
st.set_page_config(layout="wide")

# -------- Tabs superiores --------
tabs = st.tabs(["600", "IX", "Halcyon", "Braquiterapia", "Tomógrafo", "Equipos", "Excel"])

with tabs[0]:
    col_left, col_right = st.columns([1.1, 1])

    # -------- Sidebar --------
    with st.sidebar:
        st.button("Diaria")
        st.button("Mensual")
        st.button("Anual")
        st.button("Inicio")

    # -------- Panel izquierdo --------
    with col_left:
        st.title("Control de calidad diario – Aceleradores")

        fecha = st.date_input("Fecha", date.today())

        st.subheader("SEGURIDAD")

        def binario(label):
            return st.radio(label, ["Funciona", "No funciona"], horizontal=True)

        seguridad = {
            "Luces en consola": binario("Luces en consola"),
            "Luces en puerta": binario("Luces en puerta"),
            "Sistema de visualización": binario("Sistema de visualización"),
            "Sistema anti-colisión": binario("Sistema anti-colisión"),
        }

        st.subheader("ASPECTOS MECÁNICOS")

        mecanicos = {
            "Movimiento brazo": binario("Movimiento brazo"),
            "Movimiento colimador": binario("Movimiento colimador"),
            "Movimiento camilla": binario("Movimiento camilla"),
        }

        st.subheader("Constancias")
        tol = st.text_input("Tolerancia láser", "2 mm")
        res = st.text_input("Resultado láser")

        c1, c2, c3 = st.columns(3)
        with c1: st.button("Añadir")
        with c2: st.button("Reporte")
        with c3: st.button("Limpiar")

    # -------- Panel derecho (gráficas) --------
    with col_right:
        st.subheader("Análisis histórico")

        aspecto = st.selectbox("Aspecto", ["Seguridad", "Mecánico", "Dosimétrico"])
        variable = st.selectbox("Variable", ["Luces puerta", "Luces consola"])
        f1 = st.date_input("Fecha inicio")
        f2 = st.date_input("Fecha final")

        # Simulación
        df = pd.DataFrame({
            "fecha": pd.date_range("2025-10-13", periods=10),
            "valor": [1,1,1,1,1,1,1,1,1,1]
        })

        fig, ax = plt.subplots()
        ax.scatter(df["fecha"], df["valor"])
        ax.set_title(f"{variable} vs tiempo")
        st.pyplot(fig)

    # -------- Tabla inferior --------
    st.divider()
    st.subheader("Histórico")

    data = pd.DataFrame({
        "ID": [190,189,188],
        "Usuario": ["Javier", "Javier", "Cristian"],
        "Luces puerta": ["Funciona","Funciona","Funciona"],
        "Sis. Anticolisión": ["Funciona","Funciona","Funciona"],
    })

    st.data_editor(data, use_container_width=True)
