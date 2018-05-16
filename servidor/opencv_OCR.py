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
#    afr	Afrikaans	afr.traineddata
#    amh	Amharic	amh.traineddata
#    ara	Arabic	ara.traineddata
#    asm	Assamese	asm.traineddata
#    aze	Azerbaijani	aze.traineddata
#    aze_cyrl	Azerbaijani - Cyrillic	aze_cyrl.traineddata
#    bel	Belarusian	bel.traineddata
#    ben	Bengali	ben.traineddata
#    bod	Tibetan	bod.traineddata
#    bos	Bosnian	bos.traineddata
#    bul	Bulgarian	bul.traineddata
#    cat	Catalan; Valencian	cat.traineddata
#    ceb	Cebuano	ceb.traineddata
#    ces	Czech	ces.traineddata
#    chi_sim	Chinese - Simplified	chi_sim.traineddata
#    chi_tra	Chinese - Traditional	chi_tra.traineddata
#    chr	Cherokee	chr.traineddata
#    cym	Welsh	cym.traineddata
#    dan	Danish	dan.traineddata
#    deu	German	deu.traineddata
#    dzo	Dzongkha	dzo.traineddata
#    ell	Greek, Modern (1453-)	ell.traineddata
#    eng	English	eng.traineddata
#    enm	English, Middle (1100-1500)	enm.traineddata
#    epo	Esperanto	epo.traineddata
#    est	Estonian	est.traineddata
#    eus	Basque	eus.traineddata
#    fas	Persian	fas.traineddata
#    fin	Finnish	fin.traineddata
#    fra	French	fra.traineddata
#    frk	Frankish	frk.traineddata
#    frm	French, Middle (ca. 1400-1600)	frm.traineddata
#    gle	Irish	gle.traineddata
#    glg	Galician	glg.traineddata
#    grc	Greek, Ancient (-1453)	grc.traineddata
#    guj	Gujarati	guj.traineddata
#    hat	Haitian; Haitian Creole	hat.traineddata
#    heb	Hebrew	heb.traineddata
#    hin	Hindi	hin.traineddata
#    hrv	Croatian	hrv.traineddata
#    hun	Hungarian	hun.traineddata
#    iku	Inuktitut	iku.traineddata
#    ind	Indonesian	ind.traineddata
#    isl	Icelandic	isl.traineddata
#    ita	Italian	ita.traineddata
#    ita_old	Italian - Old	ita_old.traineddata
#    jav	Javanese	jav.traineddata
#    jpn	Japanese	jpn.traineddata
#    kan	Kannada	kan.traineddata
#    kat	Georgian	kat.traineddata
#    kat_old	Georgian - Old	kat_old.traineddata
#    kaz	Kazakh	kaz.traineddata
#    khm	Central Khmer	khm.traineddata
#    kir	Kirghiz; Kyrgyz	kir.traineddata
#    kor	Korean	kor.traineddata
#    kur	Kurdish	kur.traineddata
#    lao	Lao	lao.traineddata
#    lat	Latin	lat.traineddata
#    lav	Latvian	lav.traineddata
#    lit	Lithuanian	lit.traineddata
#    mal	Malayalam	mal.traineddata
#    mar	Marathi	mar.traineddata
#    mkd	Macedonian	mkd.traineddata
#    mlt	Maltese	mlt.traineddata
#    msa	Malay	msa.traineddata
#    mya	Burmese	mya.traineddata
#    nep	Nepali	nep.traineddata
#    nld	Dutch; Flemish	nld.traineddata
#    nor	Norwegian	nor.traineddata
#    ori	Oriya	ori.traineddata
#    pan	Panjabi; Punjabi	pan.traineddata
#    pol	Polish	pol.traineddata
#    por	Portuguese	por.traineddata
#    pus	Pushto; Pashto	pus.traineddata
#    ron	Romanian; Moldavian; Moldovan	ron.traineddata
#    rus	Russian	rus.traineddata
#    san	Sanskrit	san.traineddata
#    sin	Sinhala; Sinhalese	sin.traineddata
#    slk	Slovak	slk.traineddata
#    slv	Slovenian	slv.traineddata
#    spa	Spanish; Castilian	spa.traineddata
#    spa_old	Spanish; Castilian - Old	spa_old.traineddata
#    sqi	Albanian	sqi.traineddata
#    srp	Serbian	srp.traineddata
#    srp_latn	Serbian - Latin	srp_latn.traineddata
#    swa	Swahili	swa.traineddata
#    swe	Swedish	swe.traineddata
#    syr	Syriac	syr.traineddata
#    tam	Tamil	tam.traineddata
#    tel	Telugu	tel.traineddata
#    tgk	Tajik	tgk.traineddata
#    tgl	Tagalog	tgl.traineddata
#    tha	Thai	tha.traineddata
#    tir	Tigrinya	tir.traineddata
#    tur	Turkish	tur.traineddata
#    uig	Uighur; Uyghur	uig.traineddata
#    ukr	Ukrainian	ukr.traineddata
#    urd	Urdu	urd.traineddata
#    uzb	Uzbek	uzb.traineddata
#    uzb_cyrl	Uzbek - Cyrillic	uzb_cyrl.traineddata
#    vie	Vietnamese	vie.traineddata
#    yid	Yiddish	yid.traineddata
