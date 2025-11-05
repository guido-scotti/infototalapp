import datetime
from email.message import EmailMessage
from config import EMAIL_ORIGEN

hoy = datetime.datetime.today().strftime("%d/%m/%Y")
asunto_email = f"🔥 Informe Diario INFO TOTAL – {hoy}"

# ===================================
# ARMADO DEL MAIL PARA SUSCRIPTOS
# ===================================
def email_suscriptos(noticias_html, cotizaciones_html):

    mensaje = EmailMessage()
    mensaje["Subject"] = asunto_email
    mensaje["From"] = EMAIL_ORIGEN
    mensaje.set_content("Informe Diario INFO TOTAL – Tu servicio de Finanzas y Economia.")

    mensaje.add_alternative(f"""
    <html>
    <body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 
                Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #f3f4f6;">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f3f4f6; padding: 20px 0;">
        <tr>
            <td align="center">
            <table width="600" cellpadding="0" cellspacing="0" style="width:100%; background-color: #ffffff;">
                        <!-- Header -->
                <tr>
                <td style="background: #1e40af url('https://raw.githubusercontent.com/guido-scotti/totalinfoapp/main/src/img/gradient.png') no-repeat center top; background-size: cover; padding: 40px 30px; color: #ffffff;">
                    <table width="100%" cellpadding="0" cellspacing="0">
                        <tr>
                        <td>
                            <h1 style="margin: 0 0 8px 0; font-size: 32px; font-weight: 700; color: #ffffff;">INFO TOTAL</h1>
                            <p style="margin: 0; font-size: 16px; color: #dbeafe;">Tu resumen financiero para arrancar el día informado</p>
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
                    ¡Gracias por ser parte de la comunidad Info Total!
                    </p>
                </td>
                </tr>                
                <tr>
                <td align="center" style="padding: 0 30px 30px 30px;">
                    <table cellpadding="0" cellspacing="0" 
                    style="width:100%; max-width:600px; background:#ABEAA8; border-radius:8px; 
                    border:1px solid #86efac; text-align:center;">
                    <tr>
                        <td style="padding: 24px;">
                        <table width="100%" cellpadding="0" cellspacing="0">
                            <tr>
                            <td align="left">
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
                    <h3 align="center" style="margin: 0 0 16px 0; font-size: 20px; font-weight: 600; color: #111827;">
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
                    background: #1e40af url('https://raw.githubusercontent.com/guido-scotti/totalinfoapp/main/src/img/gradient.png') no-repeat center top; background-size: cover;  
                    color: #ffffff;">
                    <table width="100%" cellpadding="0" cellspacing="0">
                        <tr>
                        <td align="center">
                            <p style="margin: 0 0 8px 0; font-size: 13px; color: #ffffff;">Has recibido este correo porque estás suscrito a <strong>Info Total</strong></p>
                            <p style="margin: 0 0 16px 0; font-size: 13px; color: #ffffff;">© 2025 <strong>Info Total</strong>. Todos los derechos pertenecen a sus respectivas fuentes.</p>
                            <p style="margin: 0; font-size: 13px;">
                            <a href="#" style="color: #22d3ee; text-decoration: none;">Preferencias</a> 
                            <span style="color: #9ca3af;"> • </span>
                            <a href="https://forms.gle/7JcAgtbXVzjYwqSB7" style="color: #22d3ee; text-decoration: none;">Administrar Suscripción</a>
                            <span style="color: #9ca3af;"> • </span>
                            <a href="https://infototalapp.com/unsubscribe" style="color: #22d3ee; text-decoration: none;">Cancelar Suscripción</a>
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
    return mensaje


# ===================================
# ARMADO DEL MAIL PARA NO SUSCRIPTOS
# ===================================
def email_no_suscriptos(cotizaciones_html):

    mensaje = EmailMessage()
    mensaje["Subject"] = asunto_email
    mensaje["From"] = EMAIL_ORIGEN
    mensaje.set_content("Versión promocional del Informe Diario de Finanzas y Economia Info Total – Sumate al servicio completo.")

    mensaje.add_alternative(f"""
    <html>
    <body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 
                Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #f3f4f6;">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f3f4f6; padding: 20px 0;">
        <tr>
            <td align="center">
            <table width="600" cellpadding="0" cellspacing="0" style="width:100%; background-color: #ffffff;">
                        <!-- Header -->
                <tr>
                <td style="background: #1e40af url('https://raw.githubusercontent.com/guido-scotti/totalinfoapp/main/src/img/gradient.png') no-repeat center top; background-size: cover; padding: 40px 30px; color: #ffffff;">
                    <table width="100%" cellpadding="0" cellspacing="0">
                        <tr>
                        <td>
                            <h1 style="margin: 0 0 8px 0; font-size: 32px; font-weight: 700; color: #ffffff;">INFO TOTAL</h1>
                            <p style="margin: 0; font-size: 16px; color: #dbeafe;">Tu resumen financiero para arrancar el día informado</p>
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
                    <h2 style="margin: 0 0 12px 0; font-size: 22px; font-weight: 600; color: #111827;">¡Buenos días!</h2>
                    <p style="margin: 0; font-size: 15px; line-height: 1.6; color: #4b5563;">
                        <strong>📈 Sumate a nuestra comunidad.</strong> 
                    </p>
                    <p style="margin: 0; font-size: 15px; line-height: 1.6; color: #4b5563;">
                    Cada mañana, recibí en tu correo un informe seleccionado con lo que realmente mueve a las 
                    <strong>finanzas</strong> y la <strong>economía</strong> del país y del mundo.
                    </p>
                </td>
                </tr>  
                <tr>
                <td align="center" style="padding-bottom: 20px;">
                    <a href="https://forms.gle/EmmHDbXgJY9hV9XV9"
                    style="display:inline-block; background-color:#009EE3; color:white; padding:15px 30px;
                    text-decoration:none; border-radius:8px; font-size:18px; margin-top:15px;">
                    <strong>SUSCRIBIRME GRATIS AHORA</strong>
                    </a>  
                </td>
                </tr>         
                <tr>
                <td align="center" style="padding: 0 30px 30px 30px;">
                    <table cellpadding="0" cellspacing="0" 
                    style="width:100%; max-width:600px; background:#ABEAA8; border-radius:8px; 
                    border:1px solid #86efac; text-align:center;">
                    <tr>
                        <td style="padding: 24px;">
                        <table width="100%" cellpadding="0" cellspacing="0">
                            <tr>
                            <td align="left">
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
                    background: #1e40af url('https://raw.githubusercontent.com/guido-scotti/totalinfoapp/main/src/img/gradient.png') no-repeat center top; background-size: cover;  
                    color: #ffffff;">
                    <table width="100%" cellpadding="0" cellspacing="0">
                        <tr>
                        <td align="center">
                            <p style="margin: 0 0 8px 0; font-size: 13px; color: #ffffff;">Este correo forma parte de una muestra gratuita del 
                            servicio de <strong>Info Total</strong>.</p>
                            <p style="margin: 0 0 16px 0; font-size: 13px; color: #ffffff;">© 2025 <strong>Info Total</strong>. Todos los derechos pertenecen a sus respectivas fuentes.</p>
                            <p style="margin: 0; font-size: 13px;">
                            <a href="https://forms.gle/EmmHDbXgJY9hV9XV9" 
                            style="color: #22d3ee; text-decoration: none;">Suscribirme ahora</a>
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
    return mensaje