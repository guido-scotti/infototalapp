import datetime
from email.message import EmailMessage
from sib_api_v3_sdk import Configuration, ApiClient
from sib_api_v3_sdk.api.transactional_emails_api import TransactionalEmailsApi
from sib_api_v3_sdk.models import SendSmtpEmail

hoy = datetime.datetime.today().strftime("%d/%m/%Y")
asunto_email = f"🔥 Informe Diario INFO TOTAL – {hoy}"

def enviar_email(destinatarios, mensaje, asunto_email, EMAIL_ORIGEN, API_KEY_BREVO):
    configuration = Configuration()
    configuration.api_key['api-key'] = API_KEY_BREVO
    api_instance = TransactionalEmailsApi(ApiClient(configuration))

    html_email = mensaje.get_body(preferencelist=('html')).get_content()
    texto_plano = mensaje.get_body(preferencelist=('plain')).get_content()

    for i, destinatario in enumerate(destinatarios, start=1):
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