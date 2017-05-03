$(document).ready(function(){
  setInterval(function(){
    getData();
  }, 1000);
});

function getData(){
  $.getJSON('/data', function(data){
    console.log('data from server');
  });
}
