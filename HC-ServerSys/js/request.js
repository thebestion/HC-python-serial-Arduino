

function request(url, method, data, callback) {
	var http = new XMLHttpRequest;
	if (!http)
		return false;
	var _data;
	if (data != null && typeof data == "object") {
		_data = [];
		for (var i in data)
			_data.push(i + "=" + data[i]);
		_data = _data.join("&");
	} else {
		_data = data;
	}
	method = method.toUpperCase();
	if (method == "POST") {
		http.open(method, url, true);
		http.setRequestHeader("Method", "POST "+url+" HTTP/1.1");
		http.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	} else {
		if (_data)
			url += (url.indexOf("?") == -1 ? "?" : "&") + _data;
		_data = "";
		//alert(url);
		http.open(method, url, true);
	}
	if (callback)
		http.onreadystatechange = function() {
			if (http.readyState == 4) {
				http.onreadystatechange = function(){};
				callback(http, data);
			}
		};
	http.send(_data);
	return http;
}



function receiveIt (http, data) {
	var char = data["s"].split("/")[0];
	//alert(char);
	if (http.status == 200)		
		if(http.responseText=="1"){
			document.getElementById(char).src="images/on.png";
			//alert(char + " - on");
		}else{
			document.getElementById(char).src="images/off.png";
			//alert(char + " - off");
		}
	else
		alert ('Request failed.');
	}
	
	function ac(letter){
  		currentvalue = document.getElementById(letter).src.split("images/")[1].split(".")[0];
  		//alert(currentvalue);
  		if(currentvalue == "off"){
    		document.getElementById(letter).src="images/on.png";
    		var quest = letter + "/on/light";		
    		//alert(quest);
    		var out = request('request.php', 'GET', {s: quest}, function(){ alert(http.responseText); } );
  		}else{
   			document.getElementById(letter).src="images/off.png";
    		var quest = letter + "/off/light";
    		//alert(quest);
   			var out = request('request.php', 'GET', {s: quest}, function(){ if (http.status == 200){ var outtext = http.responseText; } } );   			
  		}
	}