var miWebSocket = {

  // Application Constructor
  initialize: function() {
    var IP = "0.0.0.0"
    var PORT = "0000"
    var ws = null

    this.bindEvents();
  },
  // Bind Event Listeners
  //
  // Bind any events that are required on startup. Common events are:
  // 'load', 'deviceready', 'offline', and 'online'.
  bindEvents: function() {
    document.addEventListener('deviceready', this.init, false);
  },

  init: function() {
    console.log("init() llamado");
    IP = "10.82.145.181"
    PORT = "9797"
    document.querySelector('#mostrarDatos').innerHTML = "Preparado para conectar en ws://" + IP + ':' + PORT;
  },

  doConnect: function() {
    ws = new WebSocket('ws://' + IP + ':' + PORT);
    //Definimos las funciones del WebSocket
    console.log(IP);
    console.log(PORT);
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
    document.querySelector('#mostrarDatos').innerHTML = "Socket conectado con exito";
  },

  onClose: function(evt) {
    console.log("Cerramos socket");
    console.log(evt.data);
    document.querySelector('#mostrarDatos').innerHTML = "Cerrando socket...";
  },

  onMessage: function(evt) {
    document.querySelector('#mostrarDatos').innerHTML = evt.data;
  },

  onError: function(evt) {
    console.log("Error");
    console.log(evt.data);
    document.querySelector('#mostrarDatos').innerHTML = "Error de socket";
    ws.close();
  },

  doSend: function(message) {
    ws.send(message);
  },

  sendText: function() {
    var lan_s = document.getElementById('lang_src').value;
    var lan_d = document.getElementById('lang_dest').value;
    document.querySelector('#mostrarDatos').innerHTML = "Idioma establecido";
    miWebSocket.doSend(lan_s + '_' + lan_d);
  },

  sendImage: function() {
    var opciones_foto = {
      quality: 60,
      sourceType: Camera.PictureSourceType.CAMERA,
      destinationType: Camera.DestinationType.DATA_URL, //Base64
      encodingType: 0, //JPEG
      targetWidth: 1500,
      targetHeight: 1125,
      correctOrientation: true,
      cameraDirection: 1
    };

    navigator.camera.getPicture(function(imageData) {
      ws.send("Enviando imagen...");
      ws.send(imageData);
    }, function() {
      document.querySelector('#mostrarDatos').innerHTML = "¡Error al tomar la foto!";
    }, opciones_foto);
  },

  setIPPORT: function() {
    IP = document.getElementById('IP_setter').value;
    PORT = document.getElementById('PORT_setter').value;
    console.log(IP);
    console.log(PORT);
    document.querySelector('#mostrarDatos').innerHTML = "IP y puerto aceptados";
  },

  doDisconnect: function() {
    ws.close();
  }

};
