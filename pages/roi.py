import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📊 Resultados del ROI en Ciberseguridad")

if "form_data" not in st.session_state or not st.session_state["form_data"]:
    st.warning("No se encontraron datos del formulario. Por favor, completa primero el formulario.")
    if st.button("Ir al formulario"):
        st.switch_page("app.py")  # Asegúrate que 'app.py' es el nombre de tu archivo principal del formulario
    st.stop()

data = st.session_state["form_data"]

# --- Sección para mostrar datos clave del formulario ---
st.divider()
st.subheader("📝 Resumen de Datos Clave del Formulario Utilizados")
col_datos1, col_datos2, col_datos3 = st.columns(3)
with col_datos1:
    st.write(f"**Facturación Anual (COP):** {data.get('Facturación Anual (COP)', 0):,.0f}")
    st.write(f"**Presupuesto Ciberseguridad (%):** {data.get('Presupuesto Ciberseguridad (%)', 0.0):.1f}%")
with col_datos2:
    st.write(f"**ROI Estimado por ISO 27001 (%):** {data.get('ROI Estimado ISO 27001 (%)', 0.0):.1f}%")
    st.write(f"**Sanciones Regulatorias (COP, 3a):** {data.get('Sanciones Regulatorias (COP, 3a)', 0):,.0f}")
with col_datos3:
    st.write(f"**Cumple Ley 1581:** {data.get('Cumple Ley 1581', 'No aplica')}")
    st.write(f"**Nivel de Riesgo Reputacional (1-5):** {data.get('Riesgo Reputacional (1-5)', 1)}") # Default del slider es 1
st.divider()


# --- Lógica del ROI ---
def calcular_roi_segmentado(form_data):
    facturacion_anual = form_data.get("Facturación Anual (COP)", 0)
    presupuesto_ciber_porc = form_data.get("Presupuesto Ciberseguridad (%)", 0.0)
    roi_estimado_iso_porc = form_data.get("ROI Estimado ISO 27001 (%)", 0.0)
    sanciones_regulatorias_valor = form_data.get("Sanciones Regulatorias (COP, 3a)", 0)
    # El valor por defecto del slider es 1, así que usamos eso si la clave no estuviera (aunque debería estar)
    riesgo_reputacional_nivel = form_data.get("Riesgo Reputacional (1-5)", 1)
    cumple_ley_1581_estado = form_data.get("Cumple Ley 1581", "No aplica")

    # Cálculo del ahorro por ISO
    # Si presupuesto_ciber_porc o roi_estimado_iso_porc es 0, el ahorro será 0.
    inversion_ciber_estimada = facturacion_anual * (presupuesto_ciber_porc / 100.0 if presupuesto_ciber_porc > 0 else 0)
    ahorro_por_iso = inversion_ciber_estimada * (roi_estimado_iso_porc / 100.0 if roi_estimado_iso_porc > 0 else 0)
    
    # Cálculo de penalización legal
    penalizacion_legal_calculada = 0
    if isinstance(sanciones_regulatorias_valor, (int, float)) and cumple_ley_1581_estado in ["No", "Parcialmente"]:
        # Usamos un factor de ejemplo, podría ser el valor completo de las sanciones o un %
        penalizacion_legal_calculada = sanciones_regulatorias_valor * 0.5 
    
    # Cálculo de penalización reputacional
    penalizacion_reputacional_calculada = 0
    if isinstance(riesgo_reputacional_nivel, (int, float)):
        # Factor de ejemplo para convertir el nivel de riesgo a un valor monetario.
        # Este factor (10,000,000 aquí) es crucial y debe ajustarse a la realidad de la empresa.
        penalizacion_reputacional_calculada = riesgo_reputacional_nivel * 10000000 

    roi_total_neto = ahorro_por_iso - penalizacion_legal_calculada - penalizacion_reputacional_calculada
    
    return {
        "ROI Financiero (Ahorro ISO)": ahorro_por_iso,
        "Estimación Costo Incumplimiento Legal": penalizacion_legal_calculada,
        "Estimación Impacto Reputacional": penalizacion_reputacional_calculada,
        "ROI Neto Estimado Ciberseguridad": roi_total_neto
    }

roi_resultados = calcular_roi_segmentado(data)

st.subheader("💰 Estimación del Retorno de Inversión (ROI)")
col_roi1, col_roi2 = st.columns(2)
with col_roi1:
    st.metric("📈 Ahorro Estimado por ISO 27001", f"${roi_resultados['ROI Financiero (Ahorro ISO)']:,.0f} COP")
    st.metric("⚖️ Costo Estimado por Incumplimiento Legal", f"${roi_resultados['Estimación Costo Incumplimiento Legal']:,.0f} COP")
with col_roi2:
    st.metric("📉 Impacto Estimado Reputacional (Negativo)", f"${roi_resultados['Estimación Impacto Reputacional']:,.0f} COP") # Generalmente es un costo/pérdida
    st.metric("✅ ROI Neto Estimado en Ciberseguridad", f"${roi_resultados['ROI Neto Estimado Ciberseguridad']:,.0f} COP",
              delta_color=("inverse" if roi_resultados['ROI Neto Estimado Ciberseguridad'] < 0 else "normal"))


if roi_resultados["ROI Neto Estimado Ciberseguridad"] > 0:
    st.success("La inversión y gestión en ciberseguridad parece estar generando un valor positivo neto.")
else:
    st.error("El ROI neto estimado es negativo. Se recomienda revisar y optimizar las estrategias e inversiones en ciberseguridad para mitigar pérdidas y mejorar el retorno.")

st.divider()

# --- GRÁFICO DE INCIDENTES ---
# La clave en app.py es "Detalles Incidentes".
# Cada incidente en la lista tiene la clave "Incidente" para el tipo.
if "Detalles Incidentes" in data and data["Detalles Incidentes"]:
    st.subheader("🛡️ Análisis de Incidentes de Ciberseguridad Reportados")
    try:
        df_incidentes = pd.DataFrame(data["Detalles Incidentes"])

        # Verificar que las columnas necesarias existan y no estén vacías
        if not df_incidentes.empty and "Incidente" in df_incidentes and "Duración (h)" in df_incidentes: #
            df_plot = df_incidentes.copy()

            fig = px.bar(
                df_plot,
                x="Incidente",  # CORREGIDO: Usar "Incidente" como en app.py
                y="Duración (h)",
                text="Duración (h)",
                labels={"Duración (h)": "Duración en Horas", "Incidente": "Tipo de Incidente"}, #
                title="Duración de Incidentes de Ciberseguridad Reportados",
                color="Incidente" #
            )
            fig.update_traces(texttemplate='%{text:.1f}h', textposition="outside")
            fig.update_layout(
                xaxis_title="Tipo de Incidente",
                yaxis_title="Duración en Horas",
                xaxis_tickangle=-45,
                uniformtext_minsize=8,
                uniformtext_mode='hide',
                legend_title_text='Tipos de Incidente'
            )
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("##### Datos de los Incidentes Reportados:")
            st.dataframe(df_incidentes.style.format({"Duración (h)": "{:.1f}"}))
        else:
            st.info("No hay suficientes datos en los incidentes detallados para generar un gráfico (se requieren columnas 'Incidente' y 'Duración (h)').")
    except Exception as e:
        st.error(f"Ocurrió un error al generar el gráfico de incidentes: {e}")
        st.warning("Verifica que los datos de incidentes tengan las columnas 'Incidente' y 'Duración (h)'.")
else:
    st.info("No se registraron incidentes específicos detallados en el formulario (sección 'Detalles Incidentes').")

st.divider()

# --- SECCIÓN DE RECOMENDACIONES ---
st.subheader("💡 Recomendaciones Personalizadas")

def generar_recomendaciones(form_data, roi_data):
    recomendaciones = []
    # --- Análisis del ROI Neto ---
    if roi_data["ROI Neto Estimado Ciberseguridad"] < 0:
        recomendaciones.append(
            "**🔴 ROI Neto Negativo:** Su Retorno de Inversión Neto Estimado en Ciberseguridad es negativo. "
            "Es crucial identificar áreas de mejora para optimizar sus inversiones y reducir pérdidas potenciales."
        )
        costo_legal = roi_data["Estimación Costo Incumplimiento Legal"]
        costo_reputacional = roi_data["Estimación Impacto Reputacional"]

        if costo_reputacional >= costo_legal and costo_reputacional > 0 : # Considerar si es el mayor o igual
            recomendaciones.append(
                f"  - El **Impacto Reputacional Estimado** (${costo_reputacional:,.0f} COP) es un factor muy significativo. "
                f"Su actual percepción de Riesgo Reputacional es de **{form_data.get('Riesgo Reputacional (1-5)', 'N/A')}/5**. " #
                "Fortalecer la postura de seguridad, mejorar la comunicación en crisis y construir confianza son claves. "
                "El factor multiplicador actual en la fórmula es de 10,000,000 por cada punto de riesgo; considere si este factor refleja adecuadamente su contexto."
            )
        elif costo_legal > 0:
            recomendaciones.append(
                f"  - El **Costo Estimado por Incumplimiento Legal** (${costo_legal:,.0f} COP) está afectando su ROI. "
                f"Dado que el estado de cumplimiento de la Ley 1581 es '{form_data.get('Cumple Ley 1581', 'N/A')}' y se reportaron sanciones, " #
                "es fundamental priorizar la adecuación a esta normativa para evitar o reducir sanciones futuras."
            )
        
        if roi_data["ROI Financiero (Ahorro ISO)"] <= 0: # Si es cero o negativo (aunque la fórmula actual no lo hace negativo)
            msg_ahorro_iso = "- El **Ahorro Estimado por ISO 27001 es bajo o nulo.** "
            if form_data.get("Facturación Anual (COP)", 0) == 0: #
                msg_ahorro_iso += "Esto se debe a que la 'Facturación Anual' reportada es cero, y este cálculo depende de ella. "
            if form_data.get("Presupuesto Ciberseguridad (%)", 0.0) == 0: #
                msg_ahorro_iso += "El 'Presupuesto de Ciberseguridad (%)' es cero. Considere asignar un presupuesto. "
            if form_data.get("ROI Estimado ISO 27001 (%)", 0.0) == 0: #
                msg_ahorro_iso += "El 'ROI Estimado para ISO 27001 (%)' es cero. Si espera beneficios, reevalúe esta estimación. "
            recomendaciones.append(msg_ahorro_iso.strip())

    else: # ROI Neto Positivo o Cero
        recomendaciones.append(
            "**🟢 ROI Neto Positivo o Cero:** ¡Excelente! Su Retorno de Inversión Neto Estimado en Ciberseguridad es positivo o cero. "
            "Esto sugiere que sus estrategias e inversiones actuales están, en general, bien orientadas."
        )
        if roi_data["ROI Financiero (Ahorro ISO)"] > 0:
             recomendaciones.append(
                f"  - El **Ahorro Estimado por ISO 27001** (${roi_data['ROI Financiero (Ahorro ISO)']:,.0f} COP) es un contribuyente positivo importante. "
                "Continuar y optimizar la adhesión a estándares como ISO 27001 es valioso."
            )
        elif form_data.get("Nivel ISO 27001", "No implementado") != "Certificado": #
            recomendaciones.append(
                f"  - Aunque el ROI es positivo, su nivel actual de implementación de ISO 27001 es '{form_data.get('Nivel ISO 27001', 'N/A')}'. " #
                "Avanzar hacia la certificación podría desbloquear aún más beneficios y ahorros."
            )


    # --- Análisis de Cumplimiento Legal Detallado ---
    if form_data.get("Cumple Ley 1581") in ["No", "Parcialmente"]: #
        recomendaciones.append(
            f"- **Atención al Cumplimiento Normativo (Ley 1581):** Ha indicado un cumplimiento '{form_data.get('Cumple Ley 1581')}' con la Ley 1581. " #
            "Es prioritario adecuar sus procesos para garantizar la protección de datos personales. Esto no solo evita sanciones "
            f"(${form_data.get('Sanciones Regulatorias (COP, 3a)', 0):,.0f} COP reportadas en los últimos 3 años), sino que también fortalece la confianza." #
        )
    elif form_data.get("Cumple Ley 1581") == "Sí": #
        recomendaciones.append(
            "- **Fortaleza en Cumplimiento Normativo:** ¡Muy bien por cumplir con la Ley 1581! Mantener este estándar es clave."
        )

    # --- Análisis basado en Incidentes ---
    incidentes = form_data.get("Detalles Incidentes", []) #
    if incidentes:
        df_incidentes_rec = pd.DataFrame(incidentes)
        if not df_incidentes_rec.empty and "Duración (h)" in df_incidentes_rec:
            total_horas_perdidas = df_incidentes_rec["Duración (h)"].sum()
            num_incidentes_detallados = len(df_incidentes_rec)
            recomendaciones.append(
                f"- **Análisis de Incidentes Detallados:** Se reportaron **{num_incidentes_detallados} incidente(s) específicos**, sumando un total de **{total_horas_perdidas:,.1f} horas de duración**. "
                "Cada hora de inactividad o recuperación tiene costos asociados (directos e indirectos). Reducir la frecuencia y la duración de los incidentes es una vía clara para mejorar el ROI. "
                "Analice las causas raíz de estos incidentes para fortalecer sus defensas."
            )
            if "Incidente" in df_incidentes_rec: #
                try:
                    tipos_comunes = df_incidentes_rec["Incidente"].mode() #
                    if not tipos_comunes.empty:
                        recomendaciones.append(
                            f"  - **Tipos de incidentes más frecuentes (detallados):** {', '.join(tipos_comunes)}. Considere enfocar esfuerzos preventivos y de mitigación en estas áreas."
                        )
                except Exception: # En caso de que .mode() falle por algún tipo de dato inesperado.
                    pass 
    
    # Considerar el número general de incidentes si no hay detalles
    if not incidentes and form_data.get("Incidentes Ciber (12m)", 0) > 0: #
         recomendaciones.append(
            f"- **Registro General de Incidentes:** Aunque no se detallaron incidentes específicos en esta ocasión, se reportaron **{form_data.get('Incidentes Ciber (12m)', 0)} incidentes en los últimos 12 meses**. " #
            "Es importante llevar un registro detallado de cada uno (tipo, impacto, duración, causa raíz, lecciones aprendidas) para identificar patrones y áreas de mejora."
        )
    elif not incidentes and form_data.get("Incidentes Ciber (12m)", 0) == 0: #
        recomendaciones.append(
            "- **Registro de Incidentes:** No se reportaron incidentes generales ni específicos. Si bien esto es ideal, asegúrese de tener procesos para detectar y registrar cualquier incidente futuro."
            )


    # --- Recomendación General Final ---
    recomendaciones.append(
        "- **Visión Estratégica y Mejora Continua:** La ciberseguridad debe ser vista como una inversión estratégica y un proceso de mejora continua. "
        "Reevalúe periódicamente su perfil de riesgo, actualice sus defensas conforme evolucionan las amenazas y fomente una cultura de seguridad en toda la organización. "
        "Considere realizar análisis de riesgos más profundos y pruebas de penetración para validar la efectividad de sus controles."
    )
    return recomendaciones

recomendaciones_generadas = generar_recomendaciones(data, roi_resultados)
if recomendaciones_generadas:
    for i, rec in enumerate(recomendaciones_generadas):
        if rec.startswith("**🔴 ROI Neto Negativo:**"):
            st.error(rec)
        elif rec.startswith("**🟢 ROI Neto Positivo o Cero:**"):
            st.success(rec)
        elif rec.startswith("- **Atención al Cumplimiento Normativo") or rec.startswith("- **Análisis de Incidentes Detallados:") or rec.startswith("- **Registro General de Incidentes:"):
            st.warning(rec)
        else:
            st.markdown(rec)
else:
    st.info("No se pudieron generar recomendaciones específicas con los datos proporcionados.")