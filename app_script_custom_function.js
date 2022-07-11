/**
 * Returns the WKT for the given WKB hex.
 *
 * @param {string} input - string of WKB hex.
 * @return String in WKT.
 * @customfunction
 */
function WKTFROMWKB(text) {

  var url = "https://converter-wkb-wkt.herokuapp.com/get-wkt-from-wkb"

  // Make a POST request with a JSON payload.
  var data = {
    "wkb_hex":text
  };
  var options = {
    'method' : 'post',
    'contentType': 'application/json',
    // Convert the JavaScript object to a JSON string.
    'payload' : JSON.stringify(data)
  };
  var wkt  = JSON.parse(UrlFetchApp.fetch(url, options).getContentText());

  return wkt
}
