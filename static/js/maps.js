// This function initialize the Google maps API and sets the Cluster to my desired coordinates
function initMap() {

  const room = { lat: 51.509865, lng: -0.118092 };

  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: room
  });

  const marker = new google.maps.Marker({
    position: room,
    map: map,
  });
}

  window.initMap = initMap;
