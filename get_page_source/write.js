
      var CLIENT_ID = '973704012693-r4s3j3tbnfrl2v7l64semk0bgevmk321.apps.googleusercontent.com';

      var SCOPES = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://docs.google.com/feeds"];
  
      /**
       * Check if current user has authorized this application.
       */
      function checkAuth() {
        console.log("inside checkAuth")  
        gapi.auth.authorize(
        
          {
            'client_id': CLIENT_ID,
            'scope': SCOPES.join(' '),
            'immediate': true
          }, handleAuthResult);
      }

      /**
       * Handle response from authorization server.
       *
       * @param {Object} authResult Authorization result.
       */
      function handleAuthResult(authResult) {
        var authorizeDiv = document.getElementById('authorize-div');
        if (authResult && !authResult.error) {
          // Hide auth UI, then load client library.
          authorizeDiv.style.display = 'none';
          loadSheetsApi();
        } else {
          // Show auth UI, allowing the user to initiate authorization by
          // clicking authorize button.
          authorizeDiv.style.display = 'inline';
        }
      }

      /**
       * Initiate auth flow in response to user clicking authorize button.
       *
       * @param {Event} event Button click event.
       */
      function handleAuthClick(event) {
        gapi.auth.authorize(
          {client_id: CLIENT_ID, scope: SCOPES, immediate: false},
          handleAuthResult);
        return false;
      }

      /**
       * Load Sheets API client library.
       */
      function loadSheetsApi() {
        var discoveryUrl =
            'https://sheets.googleapis.com/$discovery/rest?version=v4';
            
        gapi.client.load(discoveryUrl).then(listMajors);
      }

	function listMajors() {
        var request = gapi.client.sheets.spreadsheets.values.update({
          spreadsheetId: '1sBiMqhB6Ay866mYxUnyj4ysChSP-ySWrOYcZ8w9BGP8',
          range: 'Sheet1!A3:D3',
          majorDimension: 'ROWS',
          valueInputOption: 'USER_ENTERED',
          values: [[cell_value]],
        });
        request.then(function(response){
		console.log("success!")
		});
        
        console.log("inside listMajors")
      }

function onloadcomplete_test(func){
    var oldOnLoad = window.onload;
    if(typeof window.onload != 'function'){
        window.onload = func
        } else {
            window.onload = function (){
                oldOnLoad();
                func();
            }
        }
    }        
	
    onloadcomplete_test(function(){
    console.log('inside onloadcomplete_test');    
    
    document.getElementById('button').addEventListener('click', checkAuth);
	document.getElementById('authorize-button').addEventListener('click', handleAuthClick);
    // alert('window loaded');
});

// window.onload = onloadcomplete_test;

// function onloadcomplete_test(){
	// document.getElementById('button').addEventListener('click', checkAuth);
	// document.getElementById('authorize-button').addEventListener('click', handleAuthClick);
    // console.log("success!");
// }

// window.onload = onloadcomplete_test;



