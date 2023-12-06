var map;
var initialMarker;
var finalMarker;
var marker;
var steps = 100;
var stepIndex = 0;
var loopCounter = 0;
var forward = true;

function initMap() {
  map = L.map('map').setView([0, 0], 10); // Default view, will be updated later

  // Load the Excel file using SheetJS
  var file = 'results_short.xlsx'; // Adjust the file name/path as needed

  // Read the Excel file
  fetch(file)
    .then(response => response.arrayBuffer())
    .then(buffer => {
      var data = new Uint8Array(buffer);
      var workbook = XLSX.read(data, { type: 'array' });

      // Assuming lineflows is the first sheet
      var sheetName = workbook.SheetNames[4];
      var worksheet = workbook.Sheets[sheetName];

      // Get the cell values for initial and final points
      var initialLatCell = worksheet['J2'];
      var initialLonCell = worksheet['K2'];
      var finalLatCell = worksheet['S2'];
      var finalLonCell = worksheet['T2'];

      var initialLat = parseFloat(initialLatCell.v);
      var initialLon = parseFloat(initialLonCell.v);
      var finalLat = parseFloat(finalLatCell.v);
      var finalLon = parseFloat(finalLonCell.v);

      // Set the map view to initial point
      map.setView([initialLat, initialLon], 10);

      // Initialize markers and other map settings with these coordinates...
      // For example:
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

      var imageUrl = '/home/mehr/Desktop/geo_generators_visualization/js/3_custom_arrow/arrow1.png';

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

      moveMarker(); // Start moving the marker
    })
    .catch(error => {
      console.error('Error fetching the file:', error);
    });
}

// Function to calculate angle between two points
function calculateAngle(lat1, lon1, lat2, lon2) {
  var angle = -Math.atan2(lat2 - lat1, lon2 - lon1) * (180 / Math.PI);
  return angle >= 0 ? angle : 360 + angle;
}

// Rest of the original code for moveMarker function and other functionalities...

