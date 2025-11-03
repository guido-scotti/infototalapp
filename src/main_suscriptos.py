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
  <body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 
              Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #f3f4f6;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f3f4f6; padding: 20px 0;">
      <tr>
        <td align="center">
          <table width="600" cellpadding="0" cellspacing="0" style="max-width: 600px; background-color: #ffffff;">
                    <!-- Header -->
            <tr>
              <td style="background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%); padding: 40px 30px; color: #ffffff;">
                  <table width="100%" cellpadding="0" cellspacing="0">
                    <tr>
                      <td>
                        <h1 style="margin: 0 0 8px 0; font-size: 32px; font-weight: 700; color: #ffffff;">INFO TOTAL</h1>
                        <p style="margin: 0; font-size: 16px; color: #dbeafe;">Tu resumen inteligente para arrancar el día informado</p>
                      </td>
                    </tr>
                    <tr>
                      <td style="padding-top: 20px;">
                        <p style="margin: 0; font-size: 14px; color: #dbeafe;">📅 {hoy} - Edición Matutina</p>
                      </td>
                    </tr>
                  </table>
              </td>
            </tr>

            <tr>
              <td style="padding: 30px;">
                <h2 style="margin: 0 0 12px 0; font-size: 22px; font-weight: 600; color: #111827;">¡Buenos días, Suscriptor!</h2>
                <p style="margin: 0; font-size: 15px; line-height: 1.6; color: #4b5563;">
                  Acá está tu resumen personalizado de las noticias más relevantes del día. 
                  Hemos seleccionado cuidadosamente 6 artículos de las principales fuentes informativas.
                </p>
              </td>
            </tr>                
            <tr>
              <td style="padding: 0 30px 30px 30px;">
                <table width="100%" cellpadding="0" cellspacing="0" 
                  style="background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
                  border-radius: 8px; border: 1px solid #86efac;">
                  <tr>
                    <td style="padding: 24px;">
                      <table width="100%" cellpadding="0" cellspacing="0">
                        <tr>
                          <td>
                            <h2 style="margin: 0 0 20px 0; font-size: 20px; font-weight: 600; color: #111827;">
                              💵 Cotización del Dólar
                            </h2>
                          </td>
                          <td align="right">
                            <p style="margin: 0; font-size: 14px; color: #4b5563;">{hoy}</p>
                          </td>
                        </tr>
                        {cotizaciones_html}
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <tr>
              <td style="padding: 30px;">
                <h3 style="margin: 0 0 16px 0; font-size: 20px; font-weight: 600; color: #111827;">
                  🗞️ Últimas Noticias Seleccionadas
                </h3>
                {noticias_html}
              </td>
            </tr>
            <tr>
              <td style="padding: 0 30px 30px 30px;">
                <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #eff6ff; border: 1px solid #bfdbfe; border-radius: 6px; padding: 16px;">
                  <tr>
                    <td align="center">
                      <p style="margin: 0; font-size: 14px; color: #4b5563;">
                        <strong>¿Preguntas o comentarios?</strong> Contáctanos en 
                        <a href="mailto:info@infototalapp.com" style="color: #2563eb; text-decoration: none;">info@infototalapp.com</a>
                      </p>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            <tr>
              <td style="padding: 30px; border-top: 1px solid #e5e7eb; 
                background: linear-gradient(135deg, #1e40af 0%, #1d4ed8 100%);
                color: #ffffff;"">
                  <table width="100%" cellpadding="0" cellspacing="0">
                    <tr>
                      <td align="center">
                        <p style="margin: 0 0 8px 0; font-size: 13px; color: #ffffff;">Has recibido este correo porque estás suscrito a <strong>Info Total</strong></p>
                        <p style="margin: 0 0 16px 0; font-size: 13px; color: #ffffff;">© 2025 <strong>Info Total</strong>. Todos los derechos reservados.</p>
                        <p style="margin: 0; font-size: 13px;">
                          <a href="#" style="color: #22d3ee; text-decoration: none;">Preferencias</a> 
                          <span style="color: #9ca3af;"> • </span>
                          <a href="#" style="color: #22d3ee; text-decoration: none;">Administrar Suscripción</a>
                          <span style="color: #9ca3af;"> • </span>
                          <a href="#" style="color: #22d3ee; text-decoration: none;">Cancelar Suscripción</a>
                        </p>
                      </td>
                    </tr>
                  </table>
              </td>
            </tr>
        </table>
      </td>
      </tr>
    </table>
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