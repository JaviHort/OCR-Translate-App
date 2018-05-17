# -*- coding: utf-8 -*-

import googleTrans
import opencv_OCR


def execute(pathFile, lang_src, lang_dest, ocr_to_trans):
    
    #Preprocesamiento openCV (outsu + blur)
    imagen = opencv_OCR.escaladoGrises(pathFile)
    imagen = opencv_OCR.otsuBinarizacion(imagen, True)
    print('Exitaso de OSR')    
    #Analizamos con tesserocr la imagen indicando el lenguaje
    lenguaje = lang_src
    texto = opencv_OCR.analizarImagen(imagen, lenguaje)
    print('Habemus textum')
    #Traducimos con google translator indicando el idioma destino
    idioma_dest = lang_dest
    texto_traducido = googleTrans.traducir(texto, idioma_dest, ocr_to_trans)

    return texto_traducido
