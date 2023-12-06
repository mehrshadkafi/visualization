var map;
var initialMarker;
var finalMarker;
var marker;
var initialLat = 44;
var initialLon = -68;
var finalLat = 44.5;
var finalLon = -69;

function initMap() {
  map = L.map('map').setView([initialLat, initialLon], 10);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: 'Map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  var imageUrl = '/home/mehr/Desktop/geo_generators_visualization/js/3_custom_arrow/arrow1.png';

  initialMarker = L.circleMarker([initialLat, initialLon], {
    color: 'blue',
    fillColor: 'blue',
    fillOpacity: 1,
    radius: 8
  }).addTo(map);

  finalMarker = L.circleMarker([finalLat, finalLon], {
    color: 'red',
    fillColor: 'red',
    fillOpacity: 1,
    radius: 8
  }).addTo(map);

  var polyline = L.polyline([
    [initialLat, initialLon],
    [finalLat, finalLon]
  ], { color: 'blue' }).addTo(map);

  marker = L.marker([initialLat, initialLon], {
    icon: L.icon({
      iconUrl: imageUrl,
      iconSize: [40, 40],
      iconAnchor: [20, 20]
    }),
    rotationAngle: calculateAngle(initialLat, initialLon, finalLat, finalLon)
  }).addTo(map);

  var angle = calculateAngle(initialLat, initialLon, finalLat, finalLon);
  document.getElementById('angleDisplay').innerText = 'Angle: ' + angle.toFixed(2) + ' degrees';

  moveMarker();
}

