$(function(){
  var princeton = 
  [
	  {value: 'Rosen',		 data: {cat: 'Professor'}},
	  {value: 'Kernighan',  data: {cat: 'Professor'}},
	  {value: 'Specter', 	data: {cat: 'Professor'}} ,
	  {value: 'Hoffman', 	data: {cat: 'Student'}},
	  {value: 'Steinberg', data: {cat: 'Professor'}},
	  {value: 'Weinstein', data: {cat: 'Professor'}} ,
	  {value: 'Goldman', 	data: {cat: 'Professor'}},
	  {value: 'Wang', 		data: {cat: 'Student'}},
	  {value: 'Albari',		 data: {cat: 'Student'}},
	  {value: 'Gosse', 		data: {cat: 'Student'}},
	  {value: 'Bhat', 		data: {cat: 'Student'}},
	  {value: 'Okafor',		 data: {cat: 'Student'}},
	  {value: 'Chauhan', 	data: {cat: 'Student'}}
  ]

  // setup autocomplete function pulling from currencies[] array
  $('#autocomplete').autocomplete({
    lookup: princeton,
    groupby: 'cat'
  });
  
});