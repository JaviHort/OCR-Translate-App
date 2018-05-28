    # -*- coding: utf-8 -*-
import time
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import googleTrans
import opencv_OCR
import processor
import base64
import os

#Diccionario para guardar las direcciones de los clientes y sus estados de conexion
clientes = {}

# Estructura de cada cliente
# {
#     'lang_src': ''
#     'lang_dest': ''
#     'status': ''
# }

#ocr_terms = {'Assamese': 'asm', 'Tibetan': 'bod', 'Cherokee': 'chr', 'Welsh': 'cym','Dzongkha': 'dzo', 'Persian': 'fas', 'Frankish': 'frk', 'Hindi': 'hin', 'Hungarian': 'hun', 'Inuktitut': 'iku', 'Indonesian': 'ind', 'Icelandic': 'isl',  'Javanese': 'jav', 'Japanese': 'jpn', 'Kannada': 'kan', 'Georgian': 'kat', 'Georgian - Old': 'kat_old', 'Kazakh': 'kaz', 'Central Khmer': 'khm', 'Kirghiz; Kyrgyz': 'kir', 'Korean': 'kor', 'Kurdish': 'kur', 'Lao': 'lao', 'Latin': 'lat', 'Latvian': 'lav', 'Lithuanian': 'lit', 'Malayalam': 'mal', 'Marathi': 'mar', 'Macedonian': 'mkd', 'Maltese': 'mlt', 'Malay': 'msa', 'Burmese': 'mya', 'Nepali': 'nep', 'Dutch; Flemish': 'nld', 'Norwegian': 'nor', 'Oriya': 'ori', 'Panjabi; Punjabi': 'pan', 'Polish': 'pol', 'Portuguese': 'por', 'Pushto; Pashto': 'pus', 'Romanian; Moldavian; Moldovan': 'ron', 'Russian': 'rus', 'Sanskrit': 'san', 'Sinhala; Sinhalese': 'sin', 'Slovak': 'slk', 'Slovenian': 'slv', 'Spanish; Castilian': 'spa', 'Spanish; Castilian - Old': 'spa_old', 'Albanian': 'sqi', 'Serbian': 'srp', 'Serbian - Latin': 'srp_latn', 'Swahili': 'swa', 'Swedish': 'swe', 'Syriac': 'syr', 'Tamil': 'tam', 'Telugu': 'tel', 'Tajik': 'tgk', 'Tagalog': 'tgl', 'Thai': 'tha', 'Tigrinya': 'tir', 'Turkish': 'tur', 'Uighur; Uyghur': 'uig', 'Ukrainian': 'ukr', 'Urdu': 'urd', 'Uzbek': 'uzb', 'Uzbek - Cyrillic': 'uzb_cyrl', 'Vietnamese': 'vie', 'Yiddish': 'yid'}
#translate_terms = {'albanian': 'sq', 'armenian': 'hy', 'chichewa': 'ny', 'corsican': 'co', 'dutch': 'nl', 'filipino': 'tl', 'frisian': 'fy', 'georgian': 'ka', 'hausa': 'ha', 'hawaiian': 'haw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu', 'Filipino': 'fil', 'Hebrew': 'he'}

fromOCRToTrans = {
    'afr': 'af', 
    'amh': 'am', 
    'ara': 'ar', 
    'asm': '', 
    'aze': 'az', 
    'aze_cyrl': 'az', 
    'bel': 'be', 
    'ben': 'bn', 
    'bod': '', 
    'bos': 'bs', 
    'bul': 'bg', 
    'cat': 'ca', 
    'ceb': 'ceb', 
    'ces': 'cs', 
    'chi_sim': 'zh-cn', 
    'chi_tra': 'zh-tw', 
    'chr': '', 
    'cym': 'cy', 
    'dan': 'da', 
    'deu': 'de', 
    'dzo': '', 
    'ell': 'el', 
    'eng': 'en', 
    'enm': 'en', 
    'epo': 'eo', 
    'est': 'et', 
    'eus': 'eu', 
    'fas': 'fa', 
    'fin': 'fi', 
    'fra': 'fr', 
    'frk': '', 
    'frm': 'fr', 
    'gle': 'ga', 
    'glg': 'gl', 
    'grc': 'el', 
    'guj': 'gu', 
    'hat': 'ht', 
    'heb': 'iw', 
    'hin': 'hi', 
    'hrv': 'hr', 
    'hun': 'hu', 
    'iku': '', 
    'ind': 'id', 
    'isl': 'is', 
    'ita': 'it', 
    'ita_old': 'it', 
    'jav': 'jw', 
    'jpn': 'ja', 
    'kan': 'kn', 
    'kat': 'ka', 
    'kat_old': 'ka', 
    'kaz': 'kk', 
    'khm': 'km', 
    'kir': 'ky', 
    'kor': 'ko', 
    'kur': 'ku', 
    'lao': 'lo', 
    'lat': 'la', 
    'lav': 'lv', 
    'lit': 'lt', 
    'mal': 'ml', 
    'mar': 'mr', 
    'mkd': 'mk', 
    'mlt': 'mt', 
    'msa': 'ms', 
    'mya': 'my', 
    'nep': 'ne', 
    'nld': 'nl', 
    'nor': 'no', 
    'ori': '', 
    'pan': 'pa', 
    'pol': 'pl', 
    'por': 'pt', 
    'pus': 'ps', 
    'ron': 'ro', 
    'rus': 'ru', 
    'san': '', 
    'sin': 'si', 
    'slk': 'sk', 
    'slv': 'sl', 
    'spa': 'es', 
    'spa_old': 'es', 
    'sqi': 'sq', 
    'srp': 'sr', 
    'srp_latn': 'sr', 
    'swa': 'sw', 
    'swe': 'sv', 
    'syr': '', 
    'tam': 'ta', 
    'tel': 'te', 
    'tgk': 'tg', 
    'tgl': '', 
    'tha': 'th', 
    'tir': '', 
    'tur': 'tr', 
    'uig': '', 
    'ukr': 'uk', 
    'urd': 'ur', 
    'uzb': 'uz', 
    'uzb_cyrl': 'uz', 
    'vie': 'vi', 
    'yid': 'yi'
}

# Idiomas por defecto:
# -> Idioma de la imagen: inglés
# -> Idioma al que traducir: español
lang_src = 'eng'
lang_dest = 'es'

class SimpleEcho(WebSocket):

    def handleMessage(self):
        global lang_src
        global lang_dest
        if clientes[self.address]['status'] == "enviando imagen":
            archivo = open("imagen.png", 'wb')
            archivo.write(base64.b64decode(self.data))
            archivo.close()
            print("Imagen recibida. - " + time.strftime("%c"))
            #self.sendMessage(unicode("Desde servidor -> Imagen recibida"))
            texto_traducido = processor.execute('imagen.png', 
                                                clientes[self.address]['lang_src'], 
                                                clientes[self.address]['lang_dest'], 
                                                fromOCRToTrans[clientes[self.address]['lang_src']])
            os.remove("imagen.png")
            self.sendMessage(unicode(texto_traducido))
            clientes[self.address]['status'] = "conectado"
        
        else:
            if(self.data == unicode("Enviando imagen...")):
                print("Esperando envio de imagen... - " + time.strftime("%c"))
                clientes[self.address]['status'] = "enviando imagen"
            else:
                languages = self.data.split(';')
                clientes[self.address]['lang_src'] = languages[0]
                clientes[self.address]['lang_dest'] = languages[1]
                print(self.data + " - " + time.strftime("%c"))
                #self.sendMessage("Desde servidor -> Idioma origen: " + lang_src + " Idioma destino: " + lang_dest)
        

    def handleConnected(self):
        print(self.address, 'connected - ' + time.strftime("%c"))
        clientes[self.address] = {}
        clientes[self.address]['status'] = "conectado"
        clientes[self.address]['lang_src'] = ''
        clientes[self.address]['lang_dest'] = ''

    def handleClose(self):
        print(self.address, 'closed - ' + time.strftime("%c"))
        del clientes[self.address]


puerto = int(input("Introduce el puerto para el servidor: "))
server = SimpleWebSocketServer('', puerto, SimpleEcho)
print("Servidor en marcha...")
server.serveforever()
