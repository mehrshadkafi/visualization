function calculateAngle(lat1, lon1, lat2, lon2) {
  var angle = -Math.atan2(lat2 - lat1, lon2 - lon1) * (180 / Math.PI);
  return angle >= 0 ? angle : (360 + angle);
}

