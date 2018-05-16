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

#ocr_terms = {'Afrikaans': 'afr', 'Amharic': 'amh', 'Arabic': 'ara', 'Assamese': 'asm', 'Azerbaijani': 'aze', 'Azerbaijani - Cyrillic': 'aze_cyrl', 'Belarusian': 'bel', 'Bengali': 'ben', 'Tibetan': 'bod', 'Bosnian': 'bos', 'Bulgarian': 'bul', 'Catalan; Valencian': 'cat', 'Cebuano': 'ceb', 'Czech': 'ces', 'Chinese - Simplified': 'chi_sim', 'Chinese - Traditional': 'chi_tra', 'Cherokee': 'chr', 'Welsh': 'cym', 'Danish': 'dan', 'German': 'deu', 'Dzongkha': 'dzo', 'Greek Modern (1453-)': 'ell', 'English': 'eng', 'English Middle (1100-1500)': 'enm', 'Esperanto': 'epo', 'Estonian': 'est', 'Basque': 'eus', 'Persian': 'fas', 'Finnish': 'fin', 'French': 'fra', 'Frankish': 'frk', 'French Middle (ca. 1400-1600)': 'frm', 'Irish': 'gle', 'Galician': 'glg', 'Greek Ancient (-1453)': 'grc', 'Gujarati': 'guj', 'Haitian; Haitian Creole': 'hat', 'Hebrew': 'heb', 'Hindi': 'hin', 'Croatian': 'hrv', 'Hungarian': 'hun', 'Inuktitut': 'iku', 'Indonesian': 'ind', 'Icelandic': 'isl', 'Italian': 'ita', 'Italian - Old': 'ita_old', 'Javanese': 'jav', 'Japanese': 'jpn', 'Kannada': 'kan', 'Georgian': 'kat', 'Georgian - Old': 'kat_old', 'Kazakh': 'kaz', 'Central Khmer': 'khm', 'Kirghiz; Kyrgyz': 'kir', 'Korean': 'kor', 'Kurdish': 'kur', 'Lao': 'lao', 'Latin': 'lat', 'Latvian': 'lav', 'Lithuanian': 'lit', 'Malayalam': 'mal', 'Marathi': 'mar', 'Macedonian': 'mkd', 'Maltese': 'mlt', 'Malay': 'msa', 'Burmese': 'mya', 'Nepali': 'nep', 'Dutch; Flemish': 'nld', 'Norwegian': 'nor', 'Oriya': 'ori', 'Panjabi; Punjabi': 'pan', 'Polish': 'pol', 'Portuguese': 'por', 'Pushto; Pashto': 'pus', 'Romanian; Moldavian; Moldovan': 'ron', 'Russian': 'rus', 'Sanskrit': 'san', 'Sinhala; Sinhalese': 'sin', 'Slovak': 'slk', 'Slovenian': 'slv', 'Spanish; Castilian': 'spa', 'Spanish; Castilian - Old': 'spa_old', 'Albanian': 'sqi', 'Serbian': 'srp', 'Serbian - Latin': 'srp_latn', 'Swahili': 'swa', 'Swedish': 'swe', 'Syriac': 'syr', 'Tamil': 'tam', 'Telugu': 'tel', 'Tajik': 'tgk', 'Tagalog': 'tgl', 'Thai': 'tha', 'Tigrinya': 'tir', 'Turkish': 'tur', 'Uighur; Uyghur': 'uig', 'Ukrainian': 'ukr', 'Urdu': 'urd', 'Uzbek': 'uzb', 'Uzbek - Cyrillic': 'uzb_cyrl', 'Vietnamese': 'vie', 'Yiddish': 'yid'}
#translate_terms = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu', 'Filipino': 'fil', 'Hebrew': 'he'}

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
            texto_traducido = processor.execute('imagen.png', clientes[self.address]['lang_src'], clientes[self.address]['lang_dest'])
            #os.remove("imagen.png")
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
