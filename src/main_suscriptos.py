# -*- coding: utf-8 -*-
"""
Informe de Noticias – Versión paga para Suscriptos
Objetivo: Ofrecer el servicio diario de informes INFO TOTAL.
Adaptado para envío mediante Brevo (Sendinblue).
"""

import datetime
from config import LISTA_SUSCRIPTOS, EMAIL_ORIGEN, API_KEY_BREVO
from auxiliares import obtener_cotizaciones_dolar, obtener_noticias
from email_construction import email_suscriptos
from email_sending import enviar_email

hoy = datetime.datetime.today().strftime("%d/%m/%Y")
asunto_email = f"🔥 Informe Diario INFO TOTAL – {hoy}"
cotizaciones_html = obtener_cotizaciones_dolar()

# ================================
# CONSTRUCCIÓN DE CONTENIDO HTML
# ================================
noticias_html = obtener_noticias()

# ================================
# LLAMADO A LA FUNCIÓN DE EMAIL
# ================================
mensaje = email_suscriptos(noticias_html, cotizaciones_html)

# ================================
# ENVIO POR BREVO
# ================================
enviar_email(LISTA_SUSCRIPTOS, mensaje, asunto_email, EMAIL_ORIGEN, API_KEY_BREVO)