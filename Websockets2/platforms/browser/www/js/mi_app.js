var mi_app = {

  // Application Constructor
  initialize: function() {
    var IP = "0.0.0.0";
    var PORT = "0000";

    document.addEventListener('DOMContentLoaded', function() {
      mi_app.bindEvents();
    }, false);
  },

  bindEvents: function() {

    var botonOpciones = document.querySelector('#boton-opciones');
    var botonAceptarOpciones = document.querySelector('#botonAceptarOpciones');
    var botonGaleria = document.querySelector('#boton-galeria');
    var botonCamara = document.querySelector('#boton-camara');
    var botonInformacion = document.querySelector('#boton-info');
    var botonCerrarInfo = document.querySelector('#botonCerrarInfo');

    botonOpciones.addEventListener('click', function() {
      document.getElementById('popover').style.visibility = 'visible';
      document.getElementById('mask-popover').style.visibility = 'visible';
    });

    botonAceptarOpciones.addEventListener('click', function() {
      var modal = document.getElementById('pantalla-carga');
      modal.show();
      setTimeout(function(){
        mi_app.cerrarPantallaCarga();
      }, 5000);
      miWebSocket.setParametros();
    });

    botonGaleria.addEventListener('click', function() {
      miWebSocket.sendImageGallery();
    });

    botonCamara.addEventListener('click', function() {
      miWebSocket.sendImageCamera();
    });

    botonInformacion.addEventListener('click', function() {
      document.getElementById('info-popover').style.visibility = 'visible';
      document.getElementById('info-mask-popover').style.visibility = 'visible';
    });

    botonCerrarInfo.addEventListener('click', function() {
      document.getElementById('info-popover').style.visibility = 'hidden';
      document.getElementById('info-mask-popover').style.visibility = 'hidden';
    });

  },

  cerrarPantallaCarga: function() {
    var modal = document.getElementById('pantalla-carga');
    modal.hide();
  }

};
