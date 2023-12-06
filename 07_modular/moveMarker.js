var steps = 100;
var stepIndex = 0;
var loopCounter = 0;
var forward = true;

function moveMarker() {
  var latStep = forward ? (finalLat - initialLat) / steps : (initialLat - finalLat) / steps;
  var lonStep = forward ? (finalLon - initialLon) / steps : (initialLon - finalLon) / steps;

  var moveInterval = setInterval(function () {
    if (stepIndex >= steps) {
      clearInterval(moveInterval);
      stepIndex = 0;
      loopCounter++;

//      if (loopCounter >= 2) {
 //       loopCounter = 0;
   //     forward = !forward;
     // }

      moveMarker();
      return;
    }

    var newLat = forward ? (initialLat + latStep * stepIndex) : (finalLat + latStep * stepIndex);
    var newLon = forward ? (initialLon + lonStep * stepIndex) : (finalLon + lonStep * stepIndex);

    marker.setLatLng([newLat, newLon]);
    marker.setRotationAngle(calculateAngle(newLat, newLon, finalLat, finalLon));
    marker.update();
    map.panTo([newLat, newLon]);

    stepIndex++;
  }, 50);
}

