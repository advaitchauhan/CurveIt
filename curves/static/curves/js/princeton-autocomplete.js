$(function(){
  var princeton = ['Rosen', 'Kernighan', 'Specter', 'Hoffman', 'Steinberg', 'Weinstein', 'Goldman', 'Wang', 'Albari', 'Gosse', 'Bhat', 'Okafor', 'Chauhan'];

  // setup autocomplete function pulling from currencies[] array
  $('#autocomplete').autocomplete({
    lookup: princeton
  });
  
});