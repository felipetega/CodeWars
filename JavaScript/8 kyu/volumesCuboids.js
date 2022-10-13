function findDifference(a, b) {
  var totalA = a[0] * a[1] * a[2]
  var totalB = b[0] * b[1] * b[2]
  if (totalA > totalB) {
    return totalA - totalB
  } else {
    return totalB - totalA
  }
}
