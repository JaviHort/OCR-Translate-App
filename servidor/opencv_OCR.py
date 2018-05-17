#python 2.7
#-*- encoding UTF-8 -*-

import tesserocr
from PIL import Image
import cv2 as cv
import os

    
def escaladoGrises(archivo):
    return cv.cvtColor(cv.imread(archivo), cv.COLOR_BGR2GRAY)

def thresholding(imagen, typeTreshold):
    #param = (src, thresh, maxval, type[, dst])
    ret,thresh = cv.threshold(imagen,80,255,typeTreshold)
    return thresh

def adaptiveThresholding(imagen, typeTreshold):
    thresh = cv.adaptiveThreshold(imagen,255,typeTreshold,cv.THRESH_BINARY,11,2)
    return thresh

def otsuBinarizacion(imagen, blur):
    if blur:
        imagen = cv.GaussianBlur(imagen,(5,5),0)
    ret,thresh = cv.threshold(imagen,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    return thresh

def ejecutarOCR(archivo, lenguaje):
    texto = tesserocr.image_to_text(Image.open(archivo), lang=lenguaje)
    print("\topencv_OCR.py: Texto escaneado (tesserocr):\n"+texto)
    return texto
    
def analizarImagen(imagen, lenguaje='eng'):
    #Creamos un archivo temporal para cargar la imagen procesada para el OCR
    archivo_temporal = "{}.png"
    cv.imwrite(archivo_temporal, imagen)
    texto = ejecutarOCR(archivo_temporal, lenguaje)
    #os.remove(archivo_temporal)
    #texto.replace('\n', ' ')
    return texto


#    Codigo  Lenguaje  archivo.traineddata
#    --------------------------
#V    afr	Afrikaans	afr.traineddata
#V    amh	Amharic	amh.traineddata
#V    ara	Arabic	ara.traineddata
#    asm	Assamese	asm.traineddata
#V    aze	Azerbaijani	aze.traineddata
#V    aze_cyrl	Azerbaijani - Cyrillic	aze_cyrl.traineddata
#V    bel	Belarusian	bel.traineddata
#V    ben	Bengali	ben.traineddata
#    bod	Tibetan	bod.traineddata
#V    bos	Bosnian	bos.traineddata
#V    bul	Bulgarian	bul.traineddata
#V    cat	Catalan; Valencian	cat.traineddata
#V    ceb	Cebuano	ceb.traineddata
#V    ces	Czech	ces.traineddata
#V    chi_sim	Chinese - Simplified	chi_sim.traineddata
#V    chi_tra	Chinese - Traditional	chi_tra.traineddata
#    chr	Cherokee	chr.traineddata
#V    cym	Welsh	cym.traineddata
#V    dan	Danish	dan.traineddata
#V    deu	German	deu.traineddata
#    dzo	Dzongkha	dzo.traineddata
#V    ell	Greek, Modern (1453-)	ell.traineddata
#V    eng	English	eng.traineddata
#V    enm	English, Middle (1100-1500)	enm.traineddata
#V    epo	Esperanto	epo.traineddata
#V    est	Estonian	est.traineddata
#V    eus	Basque	eus.traineddata
#V    fas	Persian	fas.traineddata
#V    fin	Finnish	fin.traineddata
#V    fra	French	fra.traineddata
#    frk	Frankish	frk.traineddata
#V    frm	French, Middle (ca. 1400-1600)	frm.traineddata
#V    gle	Irish	gle.traineddata
#V    glg	Galician	glg.traineddata
#V    grc	Greek, Ancient (-1453)	grc.traineddata
#V    guj	Gujarati	guj.traineddata
#V    hat	Haitian; Haitian Creole	hat.traineddata
#V    heb	Hebrew	heb.traineddata
#V    hin	Hindi	hin.traineddata
#V    hrv	Croatian	hrv.traineddata
#V    hun	Hungarian	hun.traineddata
#    iku	Inuktitut	iku.traineddata
#V    ind	Indonesian	ind.traineddata
#V    isl	Icelandic	isl.traineddata
#V    ita	Italian	ita.traineddata
#V    ita_old	Italian - Old	ita_old.traineddata
#V    jav	Javanese	jav.traineddata
#V    jpn	Japanese	jpn.traineddata
#V    kan	Kannada	kan.traineddata
#V    kat	Georgian	kat.traineddata
#V    kat_old	Georgian - Old	kat_old.traineddata
#V    kaz	Kazakh	kaz.traineddata
#V    khm	Central Khmer	khm.traineddata
#V    kir	Kirghiz; Kyrgyz	kir.traineddata
#V    kor	Korean	kor.traineddata
#V    kur	Kurdish	kur.traineddata
#V    lao	Lao	lao.traineddata
#V    lat	Latin	lat.traineddata
#V    lav	Latvian	lav.traineddata
#V    lit	Lithuanian	lit.traineddata
#V    mal	Malayalam	mal.traineddata
#V    mar	Marathi	mar.traineddata
#V    mkd	Macedonian	mkd.traineddata
#V    mlt	Maltese	mlt.traineddata
#V    msa	Malay	msa.traineddata
#V    mya	Burmese	mya.traineddata
#V    nep	Nepali	nep.traineddata
#V    nld	Dutch; Flemish	nld.traineddata
#V    nor	Norwegian	nor.traineddata
#    ori	Oriya	ori.traineddata
#V    pan	Panjabi; Punjabi	pan.traineddata
#V    pol	Polish	pol.traineddata
#V    por	Portuguese	por.traineddata
#V    pus	Pushto; Pashto	pus.traineddata
#V    ron	Romanian; Moldavian; Moldovan	ron.traineddata
#V    rus	Russian	rus.traineddata
#    san	Sanskrit	san.traineddata
#V    sin	Sinhala; Sinhalese	sin.traineddata
#V    slk	Slovak	slk.traineddata
#V    slv	Slovenian	slv.traineddata
#V    spa	Spanish; Castilian	spa.traineddata
#V    spa_old	Spanish; Castilian - Old	spa_old.traineddata
#V    sqi	Albanian	sqi.traineddata
#V    srp	Serbian	srp.traineddata
#V    srp_latn	Serbian - Latin	srp_latn.traineddata
#V    swa	Swahili	swa.traineddata
#V    swe	Swedish	swe.traineddata
#    syr	Syriac	syr.traineddata
#V    tam	Tamil	tam.traineddata
#V    tel	Telugu	tel.traineddata
#V    tgk	Tajik	tgk.traineddata
#    tgl	Tagalog	tgl.traineddata
#V    tha	Thai	tha.traineddata
#    tir	Tigrinya	tir.traineddata
#V    tur	Turkish	tur.traineddata
#    uig	Uighur; Uyghur	uig.traineddata
#V    ukr	Ukrainian	ukr.traineddata
#V    urd	Urdu	urd.traineddata
#V    uzb	Uzbek	uzb.traineddata
#V    uzb_cyrl	Uzbek - Cyrillic	uzb_cyrl.traineddata
#    vie	Vietnamese	vie.traineddata
#V    yid	Yiddish	yid.traineddata
