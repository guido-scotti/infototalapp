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