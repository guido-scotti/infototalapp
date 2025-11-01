# -*- coding: utf-8 -*-
"""
Informe Promocional de Noticias – Versión de Difusión
Objetivo: captar nuevos suscriptores para el servicio diario de informes INFO TOTAL.
Adaptado para envío mediante Brevo (Sendinblue).
"""

import datetime
import feedparser
from email.message import EmailMessage
from sib_api_v3_sdk import Configuration, ApiClient
from sib_api_v3_sdk.api.transactional_emails_api import TransactionalEmailsApi
from sib_api_v3_sdk.models import SendSmtpEmail

from config import rss_urls, NOTICIAS_POR_MEDIO, LISTA_SUSCRIPTOS, EMAIL_ORIGEN, API_KEY_BREVO
from auxiliares import limpiar_html, preparar_link, obtener_cotizaciones_dolar


hoy = datetime.datetime.today().strftime("%d/%m/%Y")
asunto_email = f"🔥 Informe Diario INFO TOTAL – {hoy}"

# ================================
# CONSTRUCCIÓN DE CONTENIDO HTML
# ================================
noticias_html = ""
for medio, url in rss_urls.items():
    feed = feedparser.parse(url)
    entries = feed.entries[:NOTICIAS_POR_MEDIO]
    if not entries:
        continue
    noticias_html += f"<h3 style='color:#004aad;'>{medio}</h3><ul>"
    for entry in entries:
        titulo = limpiar_html(entry.get("title", "(Sin título)"))
        link = preparar_link(entry.get("link", ""))
        if not link:
            continue
        noticias_html += f"<li><a href='{link}' target='_blank'>{titulo}</a></li>"
    noticias_html += "</ul><br>"

cotizaciones_html = obtener_cotizaciones_dolar()

# ================================
# ARMADO DEL MAIL
# ================================
mensaje = EmailMessage()
mensaje["Subject"] = asunto_email
mensaje["From"] = EMAIL_ORIGEN
mensaje.set_content("Informe Diario INFO TOTAL – Tu servicio de noticias.")

mensaje.add_alternative(f"""
<html>
  <body style="font-family: Arial, sans-serif; font-size: 16px; color: #333; line-height: 1.6;">
    <h1 style="color:#004aad;text-align:center;">INFO TOTAL 📰</h1>
    <h2 style="text-align:center;">Tu resumen inteligente para arrancar el día informado</h2>

    <div style="text-align:center; margin-bottom: 40px;">
      <h2 style="color:#004aad;">📈 Nuestra comunidad de Noticias</h2>
      <p>• Informe AM con panorama político, dólar, mercados, deportes, cultura, mundo y más<br>
         • Sin publicidad, sin ruido, solo información filtrada y curada en tiempo real</p>
    </div>

    <p style="font-size:17px;">Cada mañana, recibis en tu correo un informe seleccionado con lo que realmente mueve a la Argentina:
      <b style="color:#004aad" text-align:"center">política, economía, mercados, dólar, deportes, cultura y panorama internacional.</b>
    </p>

    <div style="margin-top:25px;">
      <h3>💵 Cotizaciones del Dólar</h3>
      <table style="border-collapse:collapse;width:100%;max-width:600px;">
        <thead><tr style="background-color:#e0f0ff;">
          <th style="border:1px solid #ccc;padding:10px;">Tipo</th>
          <th style="border:1px solid #ccc;padding:10px;">Compra</th>
          <th style="border:1px solid #ccc;padding:10px;">Venta</th>
        </tr></thead><tbody>
          {cotizaciones_html}
        </tbody>
      </table>
    </div>

    <div style="margin-top:30px;">
      <h3>🗞️ Últimas Noticias Seleccionadas</h3>
      {noticias_html}
    </div>

    <hr style="margin:40px 0;border:none;border-top:1px solid #ccc;">
    <p style="font-size:13px;color:#888;text-align:center;">
      Este correo forma parte del servicio INFO TOTAL.<br>
      Generado automáticamente {hoy}. Este canal/medio se dedica exclusivamente a la recopilación y difusión de noticias provenientes de diversas fuentes públicas. No reclamamos autoría sobre el contenido compartido, el cual pertenece a sus respectivos autores y medios originales. Todo el material es utilizado con fines informativos y educativos, sin intención de infringir derechos de autor. Si algún medio o autor considera inapropiada la difusión de su contenido, puede solicitar su remoción inmediata..
    </p>
  </body>
</html>
""", subtype='html')

# ================================
# ENVIO POR BREVO
# ================================
configuration = Configuration()
configuration.api_key['api-key'] = API_KEY_BREVO
api_instance = TransactionalEmailsApi(ApiClient(configuration))

html_email = mensaje.get_body(preferencelist=('html')).get_content()
texto_plano = mensaje.get_body(preferencelist=('plain')).get_content()

for i, destinatario in enumerate(LISTA_SUSCRIPTOS, start=1):
    email_data = SendSmtpEmail(
        to=[{"email": destinatario}],
        sender={"name": "INFO TOTAL", "email": EMAIL_ORIGEN},
        subject=asunto_email,
        html_content=html_email,
        text_content=texto_plano,
        reply_to={"email": EMAIL_ORIGEN, "name": "INFO TOTAL"}
    )
    try:
        response = api_instance.send_transac_email(email_data)
        print(f"✅ Email {i} enviado a {destinatario}")
    except Exception as e:
        print(f"❌ Error al enviar a {destinatario}: {e}")