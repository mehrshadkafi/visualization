var map = L.map('map').setView([44.7, -68], 10);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 18,
}).addTo(map);

var p0 = [44.7, -68];
var p1 = [44.9, -69];

var line = L.polyline([p0, p1], { color: 'red' }).addTo(map);

var arrowIcon = L.icon({
  iconUrl: '/home/mehr/Desktop/geo_generators_visualization/js/3_custom_arrow/arrow1.png', // Replace with your file path
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
});

var arrowMarker = L.marker(p0, { icon: arrowIcon }).addTo(map);

// Circular markers at p0 and p1
var p0Marker = L.circleMarker(p0, { radius: 6, color: 'blue' }).addTo(map);
var p1Marker = L.circleMarker(p1, { radius: 6, color: 'green' }).addTo(map);

// Function to calculate the rotation angle between two points
function getRotationAngle(start, end) {
  var x = end[0] - start[0];
  var y = end[1] - start[1];
  return (Math.atan2(y, x) * 180) / Math.PI;
}

function startAnimation() {
  var duration = 3000; // Duration in milliseconds
  var startTime = performance.now();

  function animate() {
    var currentTime = performance.now();
    var elapsedTime = currentTime - startTime;
    var newPosition = calculatePosition(p0, p1, elapsedTime, duration);
    arrowMarker.setLatLng(newPosition);

    // Update rotation angle based on new position
    arrowMarker.setRotationAngle(getRotationAngle(newPosition, p1));

    if (elapsedTime < duration) {
      requestAnimationFrame(animate);
    }
  }

  requestAnimationFrame(animate);
}

function calculatePosition(start, end, elapsedTime, duration) {
  if (elapsedTime >= duration) {
    return end; // Ensure the position stops at p1
  }

  var lat = start[0] + (end[0] - start[0]) * (elapsedTime / duration);
  var lng = start[1] + (end[1] - start[1]) * (elapsedTime / duration);
  return [lat, lng];
}

startAnimation(); // Start the animation

