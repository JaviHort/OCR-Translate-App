# OCR-Translate-App
Proyecto de prácticas de la asignatura Inteligencia Ambiental.

Practice project for the subject Ubiquitous Computing

## ¿Qué es?
Aplicación para Android, iOS y Windows Phone con servidor en Python. Mediante este software, puede obtenerse el texto de una imagen traducido a casi cualquier lenguaje.

## What is it?
Android, iOS and Windows Phone application with Python server. Through this software, you can get the text from an image and translate it to almost every language.

## Servidor / Server (Debian Based Distributions)

### Instalar librerías / Packages installation
Bajo el entorno Python2.7; es necesario tener instalado la herramienta **`pip`**.

Under environment Python2.7; it is necessary to have the tool **`pip`**.

```
$ sudo apt-get install python-pip
```

Instalar las siguientes librerías:

Install the following packages:

```
$ pip install tesserocr
$ pip install opencv-python
$ pip install googletrans
```

## Aplicación móvil / Mobile Application

Para instalar la aplicación móvil, simplemente hay que entrar en la carpeta **`Client Application`**, escanear con el móvil el código QR y se descargará automáticamente.

For installing the app, you have to enter the folder **`Client Application`**, scan the QR code with your mobile phone, and download begins automatically.
