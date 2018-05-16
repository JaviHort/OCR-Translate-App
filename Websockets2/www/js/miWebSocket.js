var miWebSocket = {

  // Application Constructor
  initialize: function() {
    IP = "0.0.0.0";
    PORT = "0000";
    ws = null;
    estadoWebSocket = "desconectado"
    lan_s = "";
    lan_d = "";
  },

  doConnect: function() {

    ws = new WebSocket('ws://' + IP + ':' + PORT);
    //Definimos las funciones del WebSocket
    ws.onopen = function(evt) {
      miWebSocket.onOpen(evt)
    };
    ws.onclose = function(evt) {
      miWebSocket.onClose(evt)
    };
    ws.onmessage = function(evt) {
      miWebSocket.onMessage(evt)
    };
    ws.onerror = function(evt) {
      miWebSocket.onError(evt)
    };
  },

  onOpen: function(evt) {
    estadoWebSocket = "conectado";
    miWebSocket.sendIdiomas();
    ons.notification.alert('Conexión establecida con: (' + IP + ' : ' +  PORT + ')');
  },

  onClose: function(evt) {
    estadoWebSocket = "desconectado";
    mi_app.cerrarPantallaCarga();
    lan_s = "";
    lan_d = "";
    document.querySelector('#titulo-traduccion').innerHTML = 'Traduciendo ("origen" a "destino"):';
    document.querySelector('#texto-traduccion').innerHTML = "";
    document.getElementById('popover').style.visibility = 'visible';
    document.getElementById('mask-popover').style.visibility = 'visible';
    document.getElementById('barra-carga').style.visibility = "hidden";
  },

  onMessage: function(evt) {
    document.querySelector('#texto-traduccion').innerHTML = evt.data;
    document.getElementById('barra-carga').style.visibility = "hidden";
  },

  onError: function(evt) {
    estadoWebSocket = "desconectado";
    ons.notification.alert('Error de conexión con el IP/PUERTO asignado.');
    mi_app.cerrarPantallaCarga();
  },

  doSend: function(message) {
    ws.send(message);
  },

  sendIdiomas: function() {
    if ((lan_s != document.getElementById('lang_src').value) || (lan_d != document.getElementById('lang_dest').value)) {
      lan_s = document.getElementById('lang_src').value;
      lan_d = document.getElementById('lang_dest').value;
      miWebSocket.doSend(lan_s + ';' + lan_d);
      document.querySelector('#titulo-traduccion').innerHTML = 'Traduciendo ("' + lan_s + '" a "' + lan_d + '"):';
      document.querySelector('#texto-traduccion').innerHTML = "";
      document.getElementById('encuadre').style.backgroundImage = "url('img/image.png')";
    }
    mi_app.cerrarPantallaCarga();
    document.getElementById('popover').style.visibility = 'hidden';
    document.getElementById('mask-popover').style.visibility = 'hidden';
  },

  sendImageCamera: function() {
    var opciones_foto = {
      quality: 100,
      sourceType: Camera.PictureSourceType.CAMERA,
      destinationType: Camera.DestinationType.DATA_URL, //Base64
      encodingType: 0, //JPEG
      targetWidth: 3400,
      targetHeight: 2550,
      correctOrientation: true,
      cameraDirection: 1
    };

    navigator.camera.getPicture(function(imageData) {
      ws.send("Enviando imagen...");
      ws.send(imageData);
      document.querySelector('#texto-traduccion').innerHTML = "";
      document.getElementById('encuadre').style.backgroundImage = "url('data:image/png;base64," + imageData + "')";
      document.getElementById('barra-carga').style.visibility = "visible";
    }, function() {

    }, opciones_foto);
  },

  sendImageGallery: function() {
    var opciones_foto = {
      quality: 100,
      sourceType: Camera.PictureSourceType.PHOTOLIBRARY,
      destinationType: Camera.DestinationType.DATA_URL, //Base64
      encodingType: 0, //JPEG
      targetWidth: 3400,
      targetHeight: 2550,
      correctOrientation: true,
      cameraDirection: 1
    };

    navigator.camera.getPicture(function(imageData) {
      ws.send("Enviando imagen...");
      ws.send(imageData);
      document.querySelector('#texto-traduccion').innerHTML = "";
      document.getElementById('encuadre').style.backgroundImage = "url('data:image/png;base64," + imageData + "')";
      document.getElementById('barra-carga').style.visibility = "visible";
    }, function() {

    }, opciones_foto);
  },

  doDisconnect: function() {
    estadoWebSocket = "desconectado";
    ws.close();
  },

  setParametros: function() {
    //Comprobamos si hemos seleccionado otra IP y/o Puerto
    if ((estadoWebSocket == "conectado") && ((document.getElementById('IP_setter').value != IP) || (document.getElementById('PORT_setter').value != PORT))) {
      miWebSocket.doDisconnect();
    }

    //Comprobamos que tenemos el socket desconectado
    if (estadoWebSocket == "desconectado") {
      IP = document.getElementById('IP_setter').value;
      PORT = document.getElementById('PORT_setter').value;
      try {
        miWebSocket.doConnect();
      } catch (err) {
        //Block of code to handle errors
        ons.notification.alert('IP o PUERTO no válidos.');
        mi_app.cerrarPantallaCarga();
      }
    } else {
      miWebSocket.sendIdiomas();
    }
  }

};
