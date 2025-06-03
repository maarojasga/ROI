import streamlit as st

# --- CALLBACK Y CONFIGURACIÓN INICIAL DE SESSION STATE ---
# Inicializar la variable de sesión para el número de incidentes si no existe.
if 'num_incidentes_a_detallar_control' not in st.session_state:
    st.session_state.num_incidentes_a_detallar_control = 0

# Callback para manejar el cambio en el número de incidentes a detallar.
# Cuando el st.number_input (fuera del form) con la key 'num_incidentes_a_detallar_control'
# cambia, su valor en st.session_state se actualiza automáticamente.
# Este callback simplemente asegura que Streamlit re-ejecute el script para
# que los campos de incidentes dentro del formulario se actualicen.
def actualizar_campos_de_incidentes_callback():
    pass # No se necesita lógica adicional aquí si la key del widget coincide con la de session_state.

st.set_page_config(layout="wide")

st.title("📝 Déjanos conocer tu empresa")
st.info(
    "Por favor, completa la información solicitada a continuación. "
    "Pasa el cursor sobre los íconos (?) para obtener ayuda sobre cada campo."
)

# --- CONTROL PARA EL NÚMERO DE INCIDENTES (FUERA DEL FORMULARIO) ---
st.sidebar.subheader("Configuración de Detalles de Incidentes") # Movido a la sidebar para mejor separación
st.sidebar.number_input(
    "¿Cuántos incidentes específicos deseas detallar?",
    min_value=0, max_value=20, step=1,
    key='num_incidentes_a_detallar_control', # Esta key actualiza st.session_state
    on_change=actualizar_campos_de_incidentes_callback, # Callback permitido fuera del form
    help="Define el número de incidentes para los cuales ingresarás detalles en la sección 'Ciberseguridad' del formulario principal."
)
st.sidebar.caption(f"Actualmente configurado para detallar: {st.session_state.num_incidentes_a_detallar_control} incidente(s).")


# --- INICIO DEL FORMULARIO ---
with st.form("caracterizacion_empresa_form"):

    st.header("🏢 Datos de la Empresa")
    st.subheader("Información General")
    col1, col2 = st.columns(2)
    with col1:
        nombre_empresa = st.text_input("Nombre de la Empresa", help="Nombre comercial completo.")
        pais_sede = st.selectbox("País Sede", ["Colombia", "México", "Perú", "Chile", "Argentina", "Ecuador", "España", "Otro"], help="País de la sede principal.")
        anos_operacion = st.number_input("Años en Operación", min_value=0, step=1, help="Años operando.")
    with col2:
        id_empresa = st.text_input("ID Empresa (NIT o RUT)", help="Identificador fiscal principal.")
        ciudad_sede = st.text_input("Ciudad Sede", help="Ciudad de la sede principal.")
        sitio_web = st.text_input("Sitio Web", help="URL del sitio web (ej. www.empresa.com).")
        st.caption("Incluir 'www' o 'https://'.")

    st.subheader("Tamaño y Empleo")
    col1_tam, col2_tam, col3_tam = st.columns(3)
    with col1_tam:
        tamano_empresa_options = ['Micro (<10 empleados)', 'Pequeña (10-50 empleados)', 'Mediana (51-200 empleados)', 'Grande (>200 empleados)']
        tamano_empresa = st.selectbox("Tamaño de la Empresa", options=tamano_empresa_options, index=1, help="Clasificación por número de empleados.")
    with col2_tam:
        numero_empleados = st.number_input("Número de Empleados", min_value=0, step=1, help="Total de empleados.")
    with col3_tam:
        porcentaje_remoto = st.number_input("Porcentaje de Empleados Remotos (%)", min_value=0.0, max_value=100.0, step=1.0, format="%.1f", help="% de empleados remotos.")

    st.divider()
    st.header("🖥️ Servicios IT")
    col1_it, col2_it, col3_it = st.columns(3)
    with col1_it:
        servicio_principal_options = ["Desarrollo de Software", "Ciberseguridad", "Cloud", "Big Data", "Fintech", "Outsourcing", "Consultoría IT", "Servicios en la Nube", "Soporte Técnico", "Gestión de Infraestructura", "Desarrollo de Aplicaciones", "Análisis de Datos", "Inteligencia Artificial", "Diseño y Desarrollo", "Marketing Digital", "Formación IT", "Servicios de Telecomunicaciones", "Internet de las Cosas", "Blockchain", "Otro"]
        servicio_principal = st.selectbox("Servicio Principal de IT", options=servicio_principal_options, help="Principal servicio IT ofrecido.")
    with col2_it:
        clientes_principales = st.text_input("Clientes Principales (Tipo o Nombres)", help="Clientes clave o industria servida.")
    with col3_it:
        exporta_servicios = st.radio("¿Exporta Servicios de IT?", options=["Sí", "No"], index=1, horizontal=True, help="¿Vende servicios IT fuera del país sede?")

    st.divider()
    st.header("🔒 Ciberseguridad")
    tipo_incidente_options = ["Malware Virus", "Gusanos", "Troyanos", "Ransomware", "Spyware", "Adware", "Phishing Correos electrónicos fraudulentos", "Smishing", "Vishing", "Spear Phishing", "Whaling", "Pretexting", "Ataque DoS/DDoS", "Interrupción de servicios", "Violación de Datos", "Pérdida o robo de datos", "Ataque a Aplicación Web", "Cross-Site Scripting (XSS)", "Vulnerabilidades de autenticación", "Amenaza Interna", "Errores humanos", "Ataque a Cadena de Suministro", "Ataque de Fuerza Bruta", "Configuración Errónea", "Software sin actualizar", "Robo/Pérdida de Dispositivo", "Ataque de Día Cero", "Suplantación de Identidad", "Otro"]
    
    col1_ciber, col2_ciber = st.columns(2)
    with col1_ciber:
        nivel_iso27001_options = ["No implementado", "En proceso de implementación", "Implementado, no certificado", "Certificado"]
        nivel_iso27001 = st.selectbox("Nivel de Implementación ISO 27001", options=nivel_iso27001_options, index=0, help="Estado respecto a ISO 27001.")
        incidentes_ciber_12meses = st.number_input("Incidentes de Ciberseguridad (Últimos 12 Meses)", min_value=0, step=1, help="Incidentes de seguridad en el último año.")
        tiempo_respuesta_incidente = st.number_input("Tiempo Promedio Respuesta a Incidentes (Horas)", min_value=0.0, step=0.5, format="%.1f", help="Tiempo promedio (horas) de respuesta.")
        
        with st.expander("🛠️ Detalles de Incidentes de Ciberseguridad (Configurar cantidad en la barra lateral)"):
            st.markdown("Agrega uno o varios incidentes específicos que haya sufrido la empresa, junto con su duración.")
            
            # Leer el número de incidentes desde st.session_state (actualizado por el widget externo)
            num_a_detallar_en_form = st.session_state.get('num_incidentes_a_detallar_control', 0)
            
            if num_a_detallar_en_form == 0:
                st.write("Configure el número de incidentes a detallar en la barra lateral izquierda.")

            for i in range(int(num_a_detallar_en_form)):
                st.markdown(f"**Incidente #{i+1}**")
                col_inc1, col_inc2 = st.columns(2)
                col_inc1.selectbox(f"Tipo de Incidente #{i+1}", options=tipo_incidente_options, key=f"tipo_incidente_{i}")
                col_inc2.number_input(f"Duración del Incidente #{i+1} (Horas)", min_value=0.0, step=0.5, format="%.1f", key=f"duracion_incidente_{i}")

    with col2_ciber:
        tipo_incidente_mas_comun = st.selectbox("Tipo de Incidente Más Común", options=tipo_incidente_options, help="Incidente de ciberseguridad más frecuente.")
    st.info("La norma ISO 27001 establece un sistema de gestión de seguridad de la información reconocido internacionalmente.")

    st.divider()
    st.header("💰 Financiero")
    col1_fin, col2_fin, col3_fin = st.columns(3)
    with col1_fin:
        facturacion_anual_cop = st.number_input("Facturación Anual (COP)", min_value=0, step=100000, format="%d", help="Ingresos brutos anuales (COP).")
        st.caption("Ej: 1500000000 para 1.500 millones COP.")
    with col2_fin:
        presupuesto_ciberseguridad = st.number_input("Presupuesto Anual Ciberseguridad (%)", min_value=0.0, max_value=100.0, step=0.1, format="%.1f", help="% de facturación anual para ciberseguridad.")
    with col3_fin:
        roi_iso27001_estimado = st.number_input("ROI Estimado por ISO 27001 (%)", min_value=0.0, max_value=500.0, step=1.0, format="%.1f", help="ROI estimado por ISO 27001 (si aplica, sino 0).")
        st.caption("Basado en reducción de incidentes, mejora de confianza, etc.")

    st.divider()
    st.header("📜 Regulatorio y Cumplimiento")
    col1_reg, col2_reg = st.columns(2)
    with col1_reg:
        cumple_ley1581 = st.radio("¿Cumple con Ley 1581 de 2012 (Protección de Datos Colombia)?", options=["Sí", "No", "Parcialmente", "No aplica"], index=1, horizontal=True, help="Cumplimiento ley protección de datos Colombia.")
        st.caption("Aplica si maneja datos personales de colombianos.")
    with col2_reg:
        sanciones_regulatorias = st.number_input("Valor Sanciones Regulatorias Recibidas (COP, últimos 3 años)", min_value=0, step=1000, format="%d", help="Suma (COP) de multas regulatorias en últimos 3 años.")

    st.divider()
    st.header("⚙️ Operacional")
    col1_op, col2_op, col3_op = st.columns(3)
    with col1_op:
        proveedor_cloud = st.text_input("Proveedor Principal de Cloud", help="Principal proveedor cloud (AWS, Azure, GCP, On-Premise).")
    with col2_op:
        metodologias_desarrollo_options = ["Agile (Scrum/Kanban)", "DevOps", "Cascada (Waterfall)", "SAFe (Scaled Agile)", "Lean Development", "Prototipado", "TDD (Test-Driven Development)", "Rad (Desarrollo Rápido de Aplicaciones)", "Otro"]
        metodologia_desarrollo = st.selectbox("Metodología Principal de Desarrollo", options=metodologias_desarrollo_options, index=0, help="Metodología de desarrollo predominante.")
    with col3_op:
        tecnologias_clave = st.text_input("Tecnologías Clave Utilizadas", value="python", help="Principales tecnologías, lenguajes (ej. Python, Java, .NET).")

    st.divider()
    st.header("📈 Mercado")
    col1_mkt, col2_mkt = st.columns(2)
    with col1_mkt:
        participa_mintic = st.radio("¿Participa en programas MinTIC o similares?", options=["Sí", "No"], index=0, horizontal=True, help="¿Participa en programas MinTIC o similares?")
    with col2_mkt:
        competidores_directos = st.text_input("Principales Competidores Directos", help="Nombra 1-3 competidores directos.")

    st.divider()
    st.header("⚠️ Riesgos y Oportunidades")
    col1_risk, col2_risk = st.columns(2)
    with col1_risk:
        riesgo_reputacional = st.slider("Nivel de Riesgo Reputacional Percibido", min_value=1, max_value=5, value=1, help="Riesgo reputacional (1=Muy Bajo, 5=Muy Alto).")
        st.caption("Escala: 1=Muy Bajo, 2=Bajo, 3=Medio, 4=Alto, 5=Muy Alto")
    with col2_risk:
        oportunidad_crecimiento = st.slider("Percepción de Oportunidad de Crecimiento en el Mercado", min_value=1, max_value=5, value=3, help="Oportunidad de crecimiento (1=Muy Baja, 5=Muy Alta).")
        st.caption("Escala: 1=Muy Baja, 2=Baja, 3=Media, 4=Alta, 5=Muy Alta")

    submitted = st.form_submit_button("💾 Guardar Información")

# --- PROCESAMIENTO DESPUÉS DEL ENVÍO ---
if submitted:
    st.success("¡Formulario enviado con éxito!")
    st.balloons()

    incidentes_finales_recopilados = []
    num_incidentes_enviados = st.session_state.get('num_incidentes_a_detallar_control', 0)
    for i in range(int(num_incidentes_enviados)):
        tipo = st.session_state.get(f"tipo_incidente_{i}", None)
        duracion = st.session_state.get(f"duracion_incidente_{i}", 0.0)
        if tipo is not None:
            incidentes_finales_recopilados.append({"Incidente": tipo, "Duración (h)": duracion})

    data = {
        "Nombre Empresa": nombre_empresa, "ID Empresa": id_empresa, "País Sede": pais_sede,
        "Ciudad Sede": ciudad_sede, "Años Operación": anos_operacion, "Sitio Web": sitio_web,
        "Tamaño Empresa": tamano_empresa, "Número Empleados": numero_empleados,
        "Porcentaje Remoto (%)": porcentaje_remoto, "Servicio Principal IT": servicio_principal,
        "Clientes Principales": clientes_principales, "Exporta Servicios": exporta_servicios,
        "Nivel ISO 27001": nivel_iso27001, "Incidentes Ciber (12m)": incidentes_ciber_12meses,
        "Tipo Incidente Común": tipo_incidente_mas_comun,
        "Tiempo Respuesta Incidentes (h)": tiempo_respuesta_incidente,
        "Detalles Incidentes": incidentes_finales_recopilados,
        "Facturación Anual (COP)": facturacion_anual_cop,
        "Presupuesto Ciberseguridad (%)": presupuesto_ciberseguridad,
        "ROI Estimado ISO 27001 (%)": roi_iso27001_estimado, "Cumple Ley 1581": cumple_ley1581,
        "Sanciones Regulatorias (COP, 3a)": sanciones_regulatorias,
        "Proveedor Cloud": proveedor_cloud, "Metodología Desarrollo": metodologia_desarrollo,
        "Tecnologías Clave": tecnologias_clave, "Participa MinTIC": participa_mintic,
        "Competidores Directos": competidores_directos,
        "Riesgo Reputacional (1-5)": riesgo_reputacional,
        "Oportunidad Crecimiento (1-5)": oportunidad_crecimiento,
    }

    st.session_state["form_data"] = data
    # st.json(st.session_state["form_data"]) # Descomentar para depuración
    st.switch_page("pages/roi.py")