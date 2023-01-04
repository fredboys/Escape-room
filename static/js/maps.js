function initMap() {

    var map = new google.maps.Map(document.getElementById("map"), {
      zoom: 15,
      center: {
        lat: 51.509865,
        lng: -0.118092
      }
    });

    var label = "Escape Room";

    var locations = [{
        lat: 51.509865,
        lng: -0.118092
      },
    ];

    var markers = locations.map(function (location, i) {
      return new google.maps.Marker({
        position: location,
        label: label
      });
    });

    var markerCluster = new MarkerClusterer(map, markers, {
      imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
    });
  }
