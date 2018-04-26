# -*- coding: utf-8 -*-
import time
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import googleTrans
import opencv_OCR
import processor
import base64

#Diccionario para guardar las direcciones de los clientes y sus estados de conexion
clientes = {}

# Idiomas por defecto:
# -> Idioma de la imagen: español
# -> Idioma al que traducir: inglés
lang_src = 'spa'
lang_dest = 'en'

class SimpleEcho(WebSocket):

    def handleMessage(self):
        global lang_src
        global lang_dest
        if clientes[self.address] == "enviando imagen":
            archivo = open("imagen.png", 'wb')
            archivo.write(base64.b64decode(self.data))
            archivo.close()
            print("Imagen recibida. - " + time.strftime("%c"))
            self.sendMessage(unicode("Desde servidor -> Imagen recibida"))
            texto_traducido = processor.execute('imagen.png', lang_src, lang_dest)
            self.sendMessage(unicode("Texto traducido -> " + texto_traducido))
            clientes[self.address] = "conectado"
        
        else:
            if(self.data == unicode("Enviando imagen...")):
                print("Esperando envio de imagen... - " + time.strftime("%c"))
                clientes[self.address] = "enviando imagen"
            else:
                languages = self.data.split('_')
                lang_src = languages[0]
                lang_dest = languages[1]
                print(self.data + " - " + time.strftime("%c"))
                self.sendMessage("Desde servidor -> Idioma origen: " + lang_src + " Idioma destino: " + lang_dest)
        

    def handleConnected(self):
        print(self.address, 'connected - ' + time.strftime("%c"))
        clientes[self.address] = "conectado"

    def handleClose(self):
        print(self.address, 'closed - ' + time.strftime("%c"))
        del clientes[self.address]


server = SimpleWebSocketServer('', 9797, SimpleEcho)
server.serveforever()
