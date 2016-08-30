var cell_value;
chrome.runtime.onMessage.addListener(function(request, sender) {
  if (request.action == "getSource") {
    message.innerText = request.source;
    cell_value = String(request.source);
  }
});


console.log("inside writeSheet")  

function onWindowLoad() {
  
  var message = document.querySelector('#message');

  
  chrome.tabs.executeScript(null, {
    file: "getPageSource.js"
  }, function() {
    // If you try and inject into an extensions page or the webstore/NTP you'll get an error
    if (chrome.runtime.lastError) {
      message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });
  
  // sheets api starts here
  
}

window.onload = onWindowLoad;



// function getAuth() {
	  
	// console.log("in auth");
    // var access_token;
    // var retry = true;
    // getToken();
    // function getToken() {
		// var ci = chrome.identity;
        // ci.getAuthToken({ interactive: true }, function(token) {
            // if (chrome.runtime.lastError) {
                // console.log(chrome.runtime.lastError);
                // return;
            // }
            // access_token = token;
        // });
    // }

// }



