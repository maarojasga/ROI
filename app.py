import streamlit as st

st.set_page_config(layout="wide") # Usa un layout más ancho para el formulario

st.title("📝 Déjanos conocer tu empresa")
st.info(
    "Por favor, completa la información solicitada a continuación. "
    "Pasa el cursor sobre los íconos (?) para obtener ayuda sobre cada campo."
)

# Utilizar st.form para agrupar los campos y tener un solo botón de envío
with st.form("caracterizacion_empresa_form"):

    st.header("🏢 Datos de la Empresa")

    # --- Sección: Información General ---
    st.subheader("Información General")
    col1, col2 = st.columns(2)
    with col1:
        nombre_empresa = st.text_input(
            "Nombre de la Empresa",
            help="Nombre comercial completo de la empresa."
        )
        pais_sede = st.selectbox(
            "País Sede",
            ["Colombia", "México", "Perú", "Chile", "Argentina", "Ecuador", "España", "Otro"],
            help="País donde se encuentra la sede principal de la empresa."
        )
        anos_operacion = st.number_input(
            "Años en Operación",
            min_value=0,
            step=1,
            help="Número total de años que la empresa lleva operando."
        )
    with col2:
        id_empresa = st.text_input(
            "ID Empresa (NIT o RUT)",
            help="Número de Identificación Tributaria (NIT en Colombia) o Registro Único Tributario (RUT) u otro identificador fiscal principal, sin dígito de verificación si aplica."
        )
        ciudad_sede = st.text_input(
            "Ciudad Sede",
            help="Ciudad donde se encuentra la sede principal."
        )
        sitio_web = st.text_input(
            "Sitio Web",
            help="URL del sitio web principal de la empresa (ej. www.empresa.com)."
        )
        st.caption("Asegúrate de incluir 'www' o 'https://'.")

    # --- Sección: Tamaño y Empleo ---
    st.subheader("Tamaño y Empleo")
    col1, col2, col3 = st.columns(3)
    with col1:
        tamano_empresa_options = ['Micro (<10 empleados)', 'Pequeña (10-50 empleados)', 'Mediana (51-200 empleados)', 'Grande (>200 empleados)']
        tamano_empresa = st.selectbox(
            "Tamaño de la Empresa",
            options=tamano_empresa_options,
            index=1, # Índice para 'Pequeña (10-50)'
            help="Clasificación del tamaño según el número de empleados."
        )
    with col2:
        numero_empleados = st.number_input(
            "Número de Empleados",
            min_value=0,
            step=1,
            help="Número total de empleados actuales (incluyendo contratistas de tiempo completo)."
        )
    with col3:
        porcentaje_remoto = st.number_input(
            "Porcentaje de Empleados Remotos (%)",
            min_value=0.0, max_value=100.0, step=1.0, format="%.1f",
            help="Porcentaje aproximado de empleados que trabajan de forma remota la mayor parte del tiempo."
        )

    st.divider() # Separador visual

    # --- Sección: Servicios IT ---
    st.header("🖥️ Servicios IT")
    col1, col2, col3 = st.columns(3)
    with col1:
        servicio_principal_options = [
    "Desarrollo de Software",
    "Ciberseguridad",
    "Cloud",
    "Big Data",
    "Fintech",
    "Outsourcing",
    "Consultoría IT",
    "Servicios en la Nube",
    "Soporte Técnico",
    "Gestión de Infraestructura",
    "Desarrollo de Aplicaciones",
    "Análisis de Datos y E",
    "Inteligencia Artificial",
    "Diseño y Desarrollo",
    "Marketing Digital",
    "Formación IT",
    "Servicios de Telecomunicaciones",
    "Internet de las Cosas",
    "Blockchain"
]
        
        servicio_principal = st.selectbox(
            "Servicio Principal de IT",
            options=servicio_principal_options,
            help="Describe brevemente el principal servicio o producto relacionado con Tecnologías de la Información que ofrece la empresa."
        )
    with col2:
        clientes_principales = st.text_input(
            "Clientes Principales (Tipo o Nombres)",
            help="Menciona algunos clientes clave o el tipo de industria a la que sirven principalmente."
        )
    with col3:
        exporta_servicios = st.radio(
            "¿Exporta Servicios de IT?",
            options=["Sí", "No"],
            index=1, # Índice para 'No'
            horizontal=True,
            help="Indica si la empresa vende sus servicios de IT a clientes fuera del país de sede."
        )

    st.divider()

    # --- Sección: Ciberseguridad ---
    st.header("🔒 Ciberseguridad")
    col1, col2 = st.columns(2)
    with col1:
        nivel_iso27001_options = ["No implementado", "En proceso de implementación", "Implementado, no certificado", "Certificado"]
        nivel_iso27001 = st.selectbox(
            "Nivel de Implementación ISO 27001",
            options=nivel_iso27001_options,
            index=0, # Índice para 'No implementado'
            help="Selecciona el estado actual respecto a la norma ISO 27001 de seguridad de la información."
        )
        incidentes_ciber_12meses = st.number_input(
            "Incidentes de Ciberseguridad (Últimos 12 Meses)",
            min_value=0,
            step=1,
            help="Número de incidentes de seguridad informática (accesos no autorizados, malware, phishing exitoso, etc.) detectados en el último año."
        )
    with col2:
        tipo_incidente_options = [
    "Malware Virus",
    "Gusanos",
    "Troyanos",
    "Ransomware",
    "Spyware",
    "Adware",
    "Phishing Correos electrónicos fraudulentos",
    "Smishing",
    "Vishing",
    "Spear Phishing",
    "Whaling",
    "Pretexting",
    "Ataque DoS/DDoS Sobrecarga de servidores",
    "Interrupción de servicios",
    "Violación de Datos Acceso no autorizado a información sensible",
    "Pérdida o robo de datos",
    "Ataque a Aplicación Web Inyecciones SQL",
    "Cross-Site Scripting (XSS)",
    "Vulnerabilidades de autenticación",
    "Amenaza Interna Acciones maliciosas de empleados",
    "Errores humanos",
    "Ataque a Cadena de Suministro Compromiso de proveedores o socios",
    "Ataque de Fuerza Bruta Intentos repetidos de adivinar contraseñas",
    "Configuración Errónea Contraseñas débiles",
    "Permisos incorrectos",
    "Software sin actualizar",
    "Robo/Pérdida de Dispositivo Portátiles, móviles, memorias USB sin cifrar",
    "Ataque de Día Cero Explotación de vulnerabilidades desconocidas",
    "Suplantación de Identidad Direcciones IP falsificadas",
    "Correos electrónicos falsificados",
    "Otro"
]
        
        tipo_incidente_mas_comun = st.selectbox(
            "Tipo de Incidente Más Común",
            options=tipo_incidente_options,
            help="Describe brevemente el tipo de incidente de ciberseguridad que ocurre con mayor frecuencia."
        )
        tiempo_respuesta_incidente = st.number_input(
            "Tiempo Promedio Respuesta a Incidentes (Horas)",
            min_value=0.0,
            step=0.5,
            format="%.1f",
            help="Tiempo promedio estimado en horas desde que se detecta un incidente hasta que se inicia la respuesta activa."
        )
    st.info("La norma ISO 27001 establece un sistema de gestión de seguridad de la información reconocido internacionalmente.")

    st.divider()

    # --- Sección: Financiero ---
    st.header("💰 Financiero")
    col1, col2, col3 = st.columns(3)
    with col1:
        facturacion_anual_cop = st.number_input(
            "Facturación Anual (COP)",
            min_value=0,
            step=100000,
            format="%d", # Formato para enteros
            help="Ingresos brutos anuales aproximados de la empresa en Pesos Colombianos (COP). Ingresa solo números."
        )
        st.caption("Ej: 1500000000 para 1.500 millones COP.")
    with col2:
        presupuesto_ciberseguridad = st.number_input(
            "Presupuesto Anual Ciberseguridad (%)",
            min_value=0.0, max_value=100.0, step=0.1, format="%.1f",
            help="Porcentaje aproximado de la facturación anual destinado a ciberseguridad (herramientas, personal, consultoría)."
        )
    with col3:
        roi_iso27001_estimado = st.number_input(
            "ROI Estimado por ISO 27001 (%)",
            min_value=0.0, max_value=500.0, # Un límite superior razonable
            step=1.0, format="%.1f",
            help="Retorno de la Inversión (ROI) estimado o esperado si se implementara/certificara ISO 27001 (si aplica, si no, dejar en 0)."
        )
        st.caption("Puede basarse en reducción de incidentes, mejora de confianza, etc.")

    st.divider()

    # --- Sección: Regulatorio ---
    st.header("📜 Regulatorio y Cumplimiento")
    col1, col2 = st.columns(2)
    with col1:
        cumple_ley1581 = st.radio(
            "¿Cumple con Ley 1581 de 2012 (Protección de Datos Colombia)?",
            options=["Sí", "No", "Parcialmente", "No aplica"],
            index=1, # Índice para 'No'
            horizontal=True,
            help="Indica el nivel de cumplimiento con la ley de protección de datos personales de Colombia."
        )
        st.caption("Aplica si maneja datos personales de ciudadanos colombianos.")
    with col2:
        sanciones_regulatorias = st.number_input(
            "Valor Sanciones Regulatorias Recibidas (COP, últimos 3 años)",
            min_value=0,
            step=1000,
            format="%d",
            help="Suma total aproximada en COP de multas o sanciones recibidas por incumplimientos regulatorios (protección de datos, etc.) en los últimos 3 años."
        )

    st.divider()

    # --- Sección: Operacional ---
    st.header("⚙️ Operacional")
    col1, col2, col3 = st.columns(3)
    with col1:
        proveedor_cloud = st.text_input(
            "Proveedor Principal de Cloud",  # Índice para 'aws'
            help="Principal proveedor de servicios en la nube utilizado (Amazon Web Services, Microsoft Azure, GCP, etc.) o si la infraestructura es propia (On-Premise)."
        )
    with col2:
        metodologias_desarrollo = [
    "Agile (Scrum/Kanban)",
    "DevOps",
    "Cascada (Waterfall)",
    "SAFe (Scaled Agile)",
    "Lean Development",
    "Prototipado",
    "TDD (Test-Driven Development)",
    "Rad (Desarrollo Rápido de Aplicaciones)",
    "Otro"
]

        metodologia_desarrollo = st.selectbox(
            "Metodología Principal de Desarrollo",
            options=metodologias_desarrollo,
            index=0, # Índice para 'DevOps'
            help="Metodología predominante usada para el desarrollo de software o servicios."
        )
    with col3:
        tecnologias_clave = st.text_input(
            "Tecnologías Clave Utilizadas",
            value="python", # Corregido 'pyton' a 'python'
            help="Menciona las principales tecnologías, lenguajes de programación o plataformas que utiliza la empresa (ej. Python, Java, .NET, React)."
        )

    st.divider()

    # --- Sección: Mercado ---
    st.header("📈 Mercado")
    col1, col2 = st.columns(2)
    with col1:
        participa_mintic = st.radio(
            "¿Participa en programas MinTIC o similares?",
            options=["Sí", "No"],
            index=0, # Índice para 'Si'
            horizontal=True,
            help="Indica si la empresa ha participado o participa activamente en convocatorias, programas o iniciativas del Ministerio TIC de Colombia u organismos gubernamentales similares de apoyo al sector."
        )
    with col2:
        competidores_directos = st.text_input(
            "Principales Competidores Directos",
            help="Nombra 1-3 de los competidores más directos en su mercado principal."
        )

    st.divider()

    # --- Sección: Riesgos y Oportunidades ---
    st.header("⚠️ Riesgos y Oportunidades")
    col1, col2 = st.columns(2)
    with col1:
        riesgo_reputacional = st.slider(
            "Nivel de Riesgo Reputacional Percibido",
            min_value=1, max_value=5, value=1, # Asumiendo escala 1-5, valor 1 (bajo)
            help="Califica de 1 (Muy Bajo) a 5 (Muy Alto) el riesgo percibido para la reputación de la empresa debido a factores como incidentes de ciberseguridad, incumplimiento, etc."
        )
        st.caption("Escala: 1=Muy Bajo, 2=Bajo, 3=Medio, 4=Alto, 5=Muy Alto")
    with col2:
        oportunidad_crecimiento = st.slider(
            "Percepción de Oportunidad de Crecimiento en el Mercado",
            min_value=1, max_value=5, value=3, # Asumiendo escala 1-5, valor 3 (medio) por defecto
            help="Califica de 1 (Muy Baja) a 5 (Muy Alta) la oportunidad percibida para el crecimiento de la empresa en su mercado actual o en nuevos mercados."
        )
        st.caption("Escala: 1=Muy Baja, 2=Baja, 3=Media, 4=Alta, 5=Muy Alta")


    # --- Botón de Envío ---
    submitted = st.form_submit_button("💾 Guardar Información")

# --- Procesamiento después del envío ---
if submitted:
    st.success("¡Formulario enviado con éxito!")
    st.balloons()

    # Opcional: Mostrar los datos recopilados
    st.subheader("Resumen de la Información Ingresada:")
    data = {
        "Nombre Empresa": nombre_empresa,
        "ID Empresa": id_empresa,
        "País Sede": pais_sede,
        "Ciudad Sede": ciudad_sede,
        "Años Operación": anos_operacion,
        "Sitio Web": sitio_web,
        "Tamaño Empresa": tamano_empresa,
        "Número Empleados": numero_empleados,
        "Porcentaje Remoto (%)": porcentaje_remoto,
        "Servicio Principal IT": servicio_principal,
        "Clientes Principales": clientes_principales,
        "Exporta Servicios": exporta_servicios,
        "Nivel ISO 27001": nivel_iso27001,
        "Incidentes Ciber (12m)": incidentes_ciber_12meses,
        "Tipo Incidente Común": tipo_incidente_mas_comun,
        "Tiempo Respuesta Incidentes (h)": tiempo_respuesta_incidente,
        "Facturación Anual (COP)": facturacion_anual_cop,
        "Presupuesto Ciberseguridad (%)": presupuesto_ciberseguridad,
        "ROI Estimado ISO 27001 (%)": roi_iso27001_estimado,
        "Cumple Ley 1581": cumple_ley1581,
        "Sanciones Regulatorias (COP, 3a)": sanciones_regulatorias,
        "Proveedor Cloud": proveedor_cloud,
        "Metodología Desarrollo": metodologia_desarrollo,
        "Tecnologías Clave": tecnologias_clave,
        "Participa MinTIC": participa_mintic,
        "Competidores Directos": competidores_directos,
        "Riesgo Reputacional (1-5)": riesgo_reputacional,
        "Oportunidad Crecimiento (1-5)": oportunidad_crecimiento,
    }
    st.json(data) # Muestra los datos en formato JSON
    # O podrías usar st.write(data) o mostrarlos individualmente