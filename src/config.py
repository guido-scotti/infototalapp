import os # importa el módulo os para manejar variables de entorno
from dotenv import load_dotenv
load_dotenv()

# ================================
# CONFIGURACIÓN EMAIL / BREVO
# ================================
API_KEY_BREVO = os.getenv("BREVO_API_KEY") # trae la API key desde el archivo .env
EMAIL_ORIGEN = os.getenv("EMAIL_ORIGEN", "info@infototalapp.com") # trae el email origen desde el archivo .env 

#LISTA_SUSCRIPTOS = obtener_suscriptos(API_KEY_BREVO, lista_id=3)

LISTA_SUSCRIPTOS = [
    "scottigui@gmail.com",
    "guido_scotti@hotmail.com",
    #"kiaraagustinatort@gmail.com"
    #"alejandroraul.maldonado@gmail.com",
    #"mariano.swidzinski@gmail.com",
    #"aleciojoel@gmail.com"
    #"joel.alecio@catapultsports.com"
]

LISTA_NO_SUSCRIPTOS = [
    "scottigui@gmail.com",
    "guido_scotti@hotmail.com"
]

# ================================
# CONFIGURACIÓN NOTICIAS
# ================================
NOTICIAS_POR_MEDIO = 6  

rss_urls = {      
    #"Ambito Financiero" : "https://www.ambito.com/rss/pages/home.xml",
    #"Ambito Financiero - Economía" : "https://www.ambito.com/rss/pages/economia.xml",
    #"Ambito Financiero - Finanzas" : "https://www.ambito.com/rss/pages/finanzas.xml",    
    #"La Política Online - Noticias": "http://www.lapoliticaonline.com.ar/files/rss/ultimasnoticias.xml",
    #"La Política Online - Economía": "http://www.lapoliticaonline.com.ar/files/rss/economia.xml",
    #"La Política Online - Ciudad": "http://www.lapoliticaonline.com.ar/files/rss/ciudad.xml",
    #"La Política Online - Provincia": "http://www.lapoliticaonline.com.ar/files/rss/provincia.xml",
    #"Página 12": "https://www.pagina12.com.ar/rss/portada",    
    #"Clarín": "https://www.clarin.com/rss/politica/",  
    #"El Cronista": "https://www.cronista.com/files/rss/news.xml",
    #"La Gaceta (Tucumán)": "https://www.lagaceta.com.ar/rss",
    #"Misiones Online": "https://www.misionesonline.net/feed",
    #"Diario de Cuyo": "https://www.diariodecuyo.com.ar/rss/rss.xml",
    #"El Intransigente": "https://www.elintransigente.com/rss",
    #"TN – Todo Noticias": "https://tn.com.ar/rss.xml",
    #"TodoAgro – Noticias Agrarias": "https://www.todoagro.com.ar/noticias/feed/",
    #"Noticias Argentinas (NA)": "https://noticiasargentinas.com/rss",
    #"El Ciudadano (Rosario)": "https://www.elciudadanoweb.com/feed/",
    #"Crónica": "https://www.diariocronica.com.ar/rss/actualidad/",
    #"Noticias Ambientales": "https://noticiasambientales.com/rss",
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