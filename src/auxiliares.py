## FUNCIONES AUXILIARES ##
import requests

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