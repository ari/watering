$( ".btn-success" ).click(function() {
   $.get( "function/on.py", function( data ) {
      $( ".result" ).html( data ).show();
   });
});

$( ".btn-danger" ).click(function() {
   $.get( "function/off.py", function( data ) {
      $( ".result" ).html( data ).show();
   });
});
