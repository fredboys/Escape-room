// This function initialize the Google maps API and sets the Cluster to my desired coordinates
function initMap() {

    var map = new Map(document.getElementById("map"), {
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
      return new markers({
        position: location,
        label: label
      });
    });

    var markerCluster = new markerCluster(map, markers, {
      imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
    });
  }
