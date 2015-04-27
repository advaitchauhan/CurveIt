var _grades = [];
var _numGrades1 = [];
var _numGrades2 = [];
var plotTitle = "";
var _pctGrades1 = [];
var _pctGrades2 = [];
//var Class1name = "";
//var Class2name = "";

//Class1name = document.getElementById('Class1').value;

//Class2name = document.getElementById('Class2').value;


$('.title').each(function(index){
	plotTitle = $(this).text();
});
// Add each grade element to list
$('._grade1').each(function(index){
	_grades.push($(this).text());
});

// Add each numGrade element to list
$('._numGrade1').each(function(index){
	_numGrades1.push(parseInt($(this).text()));
});

$('._numGrade2').each(function(index){
    _numGrades2.push(parseInt($(this).text()));
});


var Class1dataSum = 0;
for (var i=0; i < _numGrades1.length; i++) {
    Class1dataSum += _numGrades1[i]
};

var Class2dataSum = 0;
for (var i=0; i < _numGrades2.length; i++) {
    Class2dataSum += _numGrades2[i]
};

for (var i=0; i < _numGrades1.length; i++) {
    _pctGrades1.push(parseFloat(_numGrades1[i] / Class1dataSum *100))
};

for (var i=0; i < _numGrades2.length; i++) {
    _pctGrades2.push(parseFloat(_numGrades2[i] / Class2dataSum *100))
};



$(function makechart() { 
	$('#container').highcharts({
        chart: {
        	backgroundColor: 'rgba(255, 255, 255, 0.1)',
            type: 'column'
        },
         title: {
             text: plotTitle,
            style: {
                     color: "#FFFFFF"
             }
        },
        xAxis: {
            categories: _grades,
        	title: {
        		text: "Grades",
                lineColor: "#FFFFFF",
                style: {
                    color: "#FFFFFF"
                }   
        	},
            labels: {
                style: {
                    color: "#FFFFFF"
                }

            },
            reversed: true
        },
        yAxis: {
        	title: {
        		text: "Percent",
                style: {
                    color: "#FFFFFF"
                        }
        	       },
            labels: {
                formatter: function() {    
                    var pcnt = this.value;
                    return Highcharts.numberFormat(pcnt) + '%';
                    }   
                }   
                    /*style: {
                        color: "#FFFFFF"
                    }*/
        },
        
        plotOptions: {
			column: {
    			pointPadding: 0,
    			borderWidth: 0.5,
                groupPadding: 0,
                // color: 'rgb(255, 154, 51)',
                color: 'rgba(230, 91, 5, 0.6)',
                borderColor: "#000000"
			},
		},
		legend: {
			enabled: false
		},
        
        credits: {
            enabled: false
        },

        /*tooltip: {
            formatter: function() {    
                    var pcnt = this.y;
                    return Highcharts.numberFormat(pcnt) + '%';
                    }   
                },*/

		legend: {
            enabled: true,
            itemStyle: {
                color: '#FFFFFF',
                }
        },

        tooltip: {
            formatter: function () {
                var output;
                if (this.series.name == Class1name) {
                    ouput = parseInt((this.y/100 * Class1dataSum));
                    return 'Count: ' + ouput + '<br>' + 'Percent: ' + Highcharts.numberFormat(this.y) + '%';
                }
                else if (this.series.name == Class2name) {
                    output = parseInt((this.y/100 * Class2dataSum));
                    return 'Count: ' + output + '<br>' + 'Percent: ' + Highcharts.numberFormat(this.y) + '%';
                }
                
            }
			//pointFormat: 'Count: <b>output</b><br/>'
		},
        series: [{
            name: Class2name,
            color: 'rgba(255, 255, 255, 0.6)',
            data: _pctGrades2
            
        },
        {
        	name: Class1name, 
            color: 'rgba(230, 91, 5, 0.6)',
        	data: _pctGrades1
        }

        ]
        

    });
});