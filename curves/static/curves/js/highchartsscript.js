var _grades = [];
var _numGrades = [];
var plotTitle = "";
$('.title').each(function(index){
	plotTitle = $(this).text();
});
// Add each grade element to list
$('._grade').each(function(index){
	_grades.push($(this).text());
});
// Add each numGrade element to list
$('._numGrade').each(function(index){
	_numGrades.push(parseInt($(this).text()));
});

var dataSum = 0;
for (var i=0; i < _numGrades.length; i++) {
    dataSum += _numGrades[i]
};

var maxpcnt = 0;

for (var i=0; i < _numGrades.length; i++) {
    if ((_numGrades[i]/dataSum) > maxpcnt) {
        maxpcnt = _numGrades[i]/dataSum;
    }
};

var tickpos = [];

if (maxpcnt > 50) {tickpos = [.2*dataSum, .4*dataSum, .6*dataSum, .8*dataSum, 1*dataSum];}
else if (maxpcnt > 25) {tickpos = [.1*dataSum, .2*dataSum, .3*dataSum, .4*dataSum, .5*dataSum];}
else {tickpos = [.05*dataSum, .1*dataSum, .15*dataSum, .2*dataSum, .25*dataSum];}


$(function makechart() { 
	$('#container').highcharts({
        chart: {
        	backgroundColor: 'rgba(255, 255, 255, 0.1)',
            type: 'column',
            style: {
                fontFamily: 'dense',
                fontSize: '24px'
            }
        },
         title: {
             text: 'Total Grades Entered: ' + dataSum,
            style: {
                     color: "#FFFFFF",
                     fontSize: '26px'
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
                    color: "#FFFFFF",
                    fontSize: '16px'
                }

            },
            reversed: true
        },
        yAxis: {

            title: {
        		text: "Percent",
                style: {
                    color: "#FFFFFF",
                }
        	},
            labels: {
                formatter: function() {
                    var pcnt = (this.value / dataSum) * 100;
                    return pcnt.toFixed(0) + ' %';
                },
                style: {
                    color: "#FFFFFF",
                    fontSize: '16px'
                }

            },

            tickPositions: tickpos,
        },
        plotOptions: {
			column: {
    			pointPadding: 0,
    			borderWidth: 0.5,
                groupPadding: 0,
                // color: 'rgb(255, 154, 51)',
                color: 'rgba(230, 91, 5, 0.6)',
                borderColor: "#000000"
			}
		},
		legend: {
			enabled: false
		},
        
        credits: {
            enabled: false
        },

		//tooltip: {
		//	pointFormat: 'Count: <b>{point.y}</b><br/>'
		//},

        tooltip: {
            formatter: function () {
               var pcnt = (this.y / dataSum) * 100;
                    return this.x + ' count: ' + this.y + '<br>' + 'Percent: ' + Highcharts.numberFormat(pcnt) + '%';
                },
                style: {
                    fontSize: '16px'
                }
        },

        series: [{
        	name: plotTitle, 
        	data: _numGrades
        }]
    });
});