function XMLHttpRequestInGet(){
    //------------ using pure javascript---------------//
    var xhr = new XMLHttpRequest();
      xhr.open('GET', '/send_Request');
      xhr.onload = function() {
          if (xhr.status === 200) {
             callback(xhr.responseText)
          }
          else {
              alert('Request failed.  Returned status of ' + status)
          }
          function callback(result){
             alert(result+' is done!')
          }
      };
      xhr.send(); 
  }