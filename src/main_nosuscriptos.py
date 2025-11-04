# -*- coding: utf-8 -*-
"""
Informe Promocional de Noticias – Versión de Difusión
Objetivo: captar nuevos suscriptores para el servicio diario de informes INFO TOTAL.
Adaptado para envío mediante Brevo (Sendinblue).
"""

import datetime
from config import LISTA_NO_SUSCRIPTOS, EMAIL_ORIGEN, API_KEY_BREVO
from auxiliares import obtener_cotizaciones_dolar
from email_construction import email_no_suscriptos
from email_sending import enviar_email

hoy = datetime.datetime.today().strftime("%d/%m/%Y")
asunto_email = f"🔥 Informe Diario INFO TOTAL – {hoy}"

cotizaciones_html = obtener_cotizaciones_dolar()

# ================================
# LLAMADO A LA FUNCIÓN DE EMAIL
# ================================
mensaje = email_no_suscriptos(cotizaciones_html)

# ================================
# ENVIO POR BREVO
# ================================
enviar_email(LISTA_NO_SUSCRIPTOS, mensaje, asunto_email, EMAIL_ORIGEN, API_KEY_BREVO)