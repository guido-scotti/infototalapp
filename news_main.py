# -*- coding: utf-8 -*-
"""
Informe Promocional de Noticias – Versión de Difusión
Objetivo: captar nuevos suscriptores para el servicio diario de informes INFO TOTAL.
Adaptado para envío mediante Brevo (Sendinblue).
"""

import feedparser
import datetime
import requests
from email.message import EmailMessage

import os # importa el módulo os para manejar variables de entorno
from dotenv import load_dotenv
load_dotenv()

# ================================
# CONFIGURACIÓN EMAIL / BREVO
# ================================
API_KEY_BREVO = os.getenv("BREVO_API_KEY") # trae la API key desde el archivo .env
EMAIL_ORIGEN = os.getenv("EMAIL_ORIGEN", "info@infototalapp.com") # trae el email origen desde el archivo .env 
lista_de_destinatarios = [
    #"mariano.swidzinski@gmail.com",
    "scottigui@gmail.com"
    #"aleciojoel@gmail.com"
        ]

# ================================
# CONFIGURACIÓN NOTICIAS
# ================================
NOTICIAS_POR_MEDIO = 6
hoy = datetime.datetime.today().strftime("%d/%m/%Y")
asunto_email = f"🔥 Tu Informe Diario INFO TOTAL – {hoy} | Nuestra comunidad de noticias"

rss_urls = {      
    "Ambito Financiero" : "https://www.ambito.com/rss/pages/home.xml",
    "Ambito Financiero - Economía" : "https://www.ambito.com/rss/pages/economia.xml",
    "Ambito Financiero - Finanzas" : "https://www.ambito.com/rss/pages/finanzas.xml",    
    "La Política Online - Noticias": "http://www.lapoliticaonline.com.ar/files/rss/ultimasnoticias.xml",
    "La Política Online - Economía": "http://www.lapoliticaonline.com.ar/files/rss/economia.xml",
    "La Política Online - Ciudad": "http://www.lapoliticaonline.com.ar/files/rss/ciudad.xml",
    "La Política Online - Provincia": "http://www.lapoliticaonline.com.ar/files/rss/provincia.xml",
    "Página 12": "https://www.pagina12.com.ar/rss/portada",    
    "Clarín": "https://www.clarin.com/rss/politica/",  
    "El Cronista": "https://www.cronista.com/files/rss/news.xml",
    "La Gaceta (Tucumán)": "https://www.lagaceta.com.ar/rss",
    "Misiones Online": "https://www.misionesonline.net/feed",
    "Diario de Cuyo": "https://www.diariodecuyo.com.ar/rss/rss.xml",
    "El Intransigente": "https://www.elintransigente.com/rss",
    "TN – Todo Noticias": "https://tn.com.ar/rss.xml",
    "TodoAgro – Noticias Agrarias": "https://www.todoagro.com.ar/noticias/feed/",
    "Noticias Argentinas (NA)": "https://noticiasargentinas.com/rss",
    "El Ciudadano (Rosario)": "https://www.elciudadanoweb.com/feed/",
    "Crónica": "https://www.diariocronica.com.ar/rss/actualidad/",
    "Noticias Ambientales": "https://noticiasambientales.com/rss",
    # #Segmento Cultura -----------------------------------------------
    #"Clarin - cultura": "https://www.clarin.com/rss/cultura/",
    #"Ambito Financiero - Espectáculos" : "https://www.ambito.com/rss/pages/espectaculos.xml",
    # #Segmento deportes Ole ------------------------------------------
    #"Olé – Deportes": "https://www.ole.com.ar/rss/ultimas-noticias/",
    #"Olé – Lo Último": "http://www.ole.com.ar/rss/ultimas-noticias/",
    #"Olé – Equipos": "http://www.ole.com.ar/rss/equipos/",
    #"Olé – Boca Juniors":	"http://www.ole.com.ar/rss/boca-juniors/",
    #"Olé – River Plate":	"http://www.ole.com.ar/rss/river-plate/",    
    # #Segmento Mundo ------------------------------------------------
    #"BBC mundo": "http://www.bbc.co.uk/mundo/index.xml",
    #"BBC News - World": "http://feeds.bbci.co.uk/news/world/rss.xml",
    #"CNN - World": "http://rss.cnn.com/rss/edition_world.rss",
    #"The Guardian - World News": "https://www.theguardian.com/world/rss",
    #"Al Jazeera - World": "https://www.aljazeera.com/xml/rss/all.xml",
   # "NPR - World News": "https://feeds.npr.org/1004/rss.xml",
    #"New York Times - World": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
   # "Deutsche Welle (DW) - World": "https://rss.dw.com/rdf/rss-en-world",
   # "France 24 - World": "https://www.france24.com/en/rss",
   # "Euronews - International": "https://www.euronews.com/rss?level=theme&name=news",    
   # "El País – Economía (España)": "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/economia/portada",
   # "Cinco Días (España)": "https://cincodias.elpais.com/rss/cincodias/portada.xml",
   # "90 minutos":"https://www.90min.com/posts.rss",
   # "Buenos Aires Times": "https://www.batimes.com.ar/feed"    
}

# ================================
# FUNCIONES AUXILIARES
# ================================
def obtener_cotizaciones_dolar():
    try:
        response = requests.get("https://dolarapi.com/v1/dolares")
        response.raise_for_status()
        datos = response.json()
        filas_html = ""
        for c in datos:
            nombre = c["nombre"]
            compra = f"${c['compra']:.2f}" if c['compra'] else "-"
            venta = f"${c['venta']:.2f}" if c['venta'] else "-"
            filas_html += f"""
                <tr>
                    <td style="border:1px solid #ccc;padding:8px;text-align:center;">{nombre}</td>
                    <td style="border:1px solid #ccc;padding:8px;text-align:center;">{compra}</td>
                    <td style="border:1px solid #ccc;padding:8px;text-align:center;">{venta}</td>
                </tr>
            """
        return filas_html
    except Exception as e:
        print(f"⚠️ Error al obtener cotizaciones del dólar: {e}")
        return "<tr><td colspan='3'>Error al cargar cotizaciones</td></tr>"

def preparar_link(link):
    return link if link.startswith("http") else None

def limpiar_html(texto):
    return texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

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
# ARMADO DEL EMAIL PROMOCIONAL
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
      <b style="color:#004aad">política, economía, mercados, dólar, deportes, cultura y panorama internacional.</b>
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
# ENVÍO POR BREVO
# ================================
from sib_api_v3_sdk import Configuration, ApiClient
from sib_api_v3_sdk.api.transactional_emails_api import TransactionalEmailsApi
from sib_api_v3_sdk.models import SendSmtpEmail

configuration = Configuration()
configuration.api_key['api-key'] = API_KEY_BREVO
api_instance = TransactionalEmailsApi(ApiClient(configuration))

html_email = mensaje.get_body(preferencelist=('html')).get_content()
texto_plano = mensaje.get_body(preferencelist=('plain')).get_content()

for i, destinatario in enumerate(lista_de_destinatarios, start=1):
    email_data = SendSmtpEmail(
        to=[{"email": destinatario}],
        sender={"name": "INFO TOTAL", "email": EMAIL_ORIGEN},
        subject=asunto_email,
        html_content=html_email,
        text_content=texto_plano,
        reply_to={"email": "info@infototalapp.com", "name": "INFO TOTAL"}
    )
    try:
        response = api_instance.send_transac_email(email_data)
        print(f"✅ Email {i} enviado a {destinatario}")
    except Exception as e:
        print(f"❌ Error al enviar a {destinatario}: {e}")
