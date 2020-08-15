function XMLHttpRequestInGet(){
    //------------ using jQuery---------------//
    // $.ajax('/send_Request', {
    $.ajax({
        url: 'http://127.0.0.1:8000/app/send_Request',
      data: {
          id: 'some-unique-id'
      }
    })
    .then(
        function success(name) {
            alert(name+' is done!');
        },
  
        function fail(data, status) {
            alert('Request failed.  Returned status of ' + status);
        }
    )
}