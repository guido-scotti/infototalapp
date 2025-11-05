## FUNCIONES AUXILIARES ##
import requests
import feedparser
from config import rss_urls, NOTICIAS_POR_MEDIO

def preparar_link(link):
    return link if link.startswith("http") else None

def limpiar_html(texto):
    return texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def obtener_cotizaciones_dolar():
    try:
        response = requests.get("https://dolarapi.com/v1/dolares")
        response.raise_for_status()
        datos = response.json()
        filas_html = ""

        for i, c in enumerate(datos):
            nombre = c["nombre"]
            compra = f"${c['compra']:.2f}" if c['compra'] else "-"
            venta = f"${c['venta']:.2f}" if c['venta'] else "-"

            if i % 2 == 0:
                filas_html += "<tr>"

            filas_html += f"""
            <td width="48%" style="vertical-align: top; padding-bottom: 16px; padding-right: 16px;">
                <table width="100%" cellpadding="0" cellspacing="0" 
                       style="background-color: #ffffff; border-radius: 6px; border: 1px solid #e5e7eb;">
                    <tr>
                        <td style="padding: 16px;">
                            <p style="margin: 0 0 12px 0; font-size: 16px; font-weight: 600; color: #111827;">{nombre}</p>
                            <table width="100%" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td width="50%">
                                        <p style="margin: 0 0 4px 0; font-size: 12px; color: #6b7280;">Compra</p>
                                        <p style="margin: 0; font-size: 18px; font-weight: 600; color: #111827;">{compra}</p>
                                    </td>
                                    <td width="50%">
                                        <p style="margin: 0 0 4px 0; font-size: 12px; color: #6b7280;">Venta</p>
                                        <p style="margin: 0; font-size: 18px; font-weight: 600; color: #111827;">{venta}</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
            """

            if i % 2 == 1 or i == len(datos) - 1:
                filas_html += "</tr>"

        return filas_html

    except Exception as e:
        print(f"⚠️ Error al obtener cotizaciones del dólar: {e}")
        return "<tr><td colspan='2'>Error al cargar cotizaciones</td></tr>"
    

def obtener_noticias():
    noticias_html = """
    <table align="center" width="100%" style="max-width:600px;">
    """
    for medio, url in rss_urls.items():
        feed = feedparser.parse(url)
        entries = feed.entries[:NOTICIAS_POR_MEDIO]
        if not entries:
            continue

        noticias_html += f"""
        <tr><td><h3 style="color:#111827; font-size:18px; margin:24px 0 12px;">📰 {medio}</h3></td></tr>
        """

        for entry in entries:
            titulo = limpiar_html(entry.get("title", "(Sin título)"))
            descripcion = limpiar_html(entry.get("summary", ""))[:180] + "..." if entry.get("summary") else ""
            link = preparar_link(entry.get("link", ""))
            categoria = entry.get("tags")[0]["term"] if entry.get("tags") else "General"

            if not link:
                continue

            noticias_html += f"""
            <tr>
              <td style="padding: 0 0 16px 0;">
                <table width="100%" cellpadding="0" cellspacing="0" 
                       style="background-color:#ffffff; border:1px solid #e5e7eb; border-radius:8px;
                              box-shadow:0 1px 3px rgba(0,0,0,0.08); padding:16px; width:100%;">
                  <tr>
                    <td style="font-size:15px; font-weight:600; color:#1e40af; 
                               white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                      {titulo}
                    </td>
                  </tr>
                  <tr>
                    <td style="font-size:13px; color:#374151; line-height:1.4; padding:8px 0;">
                      {descripcion}
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <table width="100%" cellpadding="0" cellspacing="0" style="margin-top:8px;">
                        <tr>
                          <td align="left">
                            <span style="background-color:#dbeafe; color:#1e3a8a; 
                                         padding:4px 8px; border-radius:12px; font-weight:500; font-size:12px;">
                              {medio}
                            </span>
                          </td>
                          <td align="right">
                            <span style="background-color:#ecfdf5; color:#065f46; 
                                         padding:4px 8px; border-radius:12px; font-weight:500; font-size:12px;">
                              {categoria}
                            </span>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" style="padding-top:10px;">
                      <a href="{link}" target="_blank"
                         style="display:inline-block; background: #1e40af;
                                color:#ffffff; text-decoration:none; font-weight:600; font-size:13px;
                                padding:8px 16px; border-radius:6px;">
                        Leer más →
                      </a>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            """

    noticias_html += "</table>"
    return noticias_html


