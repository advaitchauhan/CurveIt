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

var GradeSum = 0;
GradeSum = 4*_numGrades[0] + 4*_numGrades[1] + 3.7*_numGrades[2] + 3.3*_numGrades[3] + 3*_numGrades[4] + 2.7*_numGrades[5] + 2.3*_numGrades[6] + 2*_numGrades[7] + 1.7*_numGrades[8] + 1*_numGrades[9];

var testA = 0;
testA = _numGrades[1];

var GradeTot = 0
for (var i=0; i < 11; i++) {
    GradeTot += _numGrades[i]
};

if (GradeTot == 0) {
    var AverageGrade = 0;
}
else {
    var AverageGrade = GradeSum/GradeTot;
}

var AvgLetGrade = '';

if (AverageGrade > 3.85) AvgLetGrade = 'A';
else if (AverageGrade > 3.5) AvgLetGrade = 'A-';
else if (AverageGrade > 3.15) AvgLetGrade = 'B+';
else if (AverageGrade > 2.85) AvgLetGrade = 'B';
else if (AverageGrade > 2.5) AvgLetGrade = 'B-';
else if (AverageGrade > 2.15) AvgLetGrade = 'C+';
else if (AverageGrade > 1.85) AvgLetGrade = 'C';
else if (AverageGrade > 1.5) AvgLetGrade = 'C-';
else if (AverageGrade > .5) AvgLetGrade = 'D';
else AvgLetGrade = 'F';

var maxpcnt = 0;

for (var i=0; i < _numGrades.length; i++) {
    if (dataSum == 0) {
        maxpcnt = 0;
    }
    else if ((_numGrades[i]/dataSum) > maxpcnt) {
        maxpcnt = _numGrades[i]/dataSum;
    }
};


var tickpos = [];

if (maxpcnt > .50) {tickpos = [0* dataSum, .2*dataSum, .4*dataSum, .6*dataSum, .8*dataSum, 1*dataSum];}
else if (maxpcnt > .25) {tickpos = [0*dataSum, .1*dataSum, .2*dataSum, .3*dataSum, .4*dataSum, .5*dataSum];}
else if (maxpcnt > 0) {tickpos = [0*dataSum, .05*dataSum, .1*dataSum, .15*dataSum, .2*dataSum, .25*dataSum];}
else {tickpos = [0]}


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
             text: 'Average Grade: ' + AvgLetGrade + ' (' + AverageGrade.toFixed(2) + ')' + ' for ' + dataSum + ' Grades Entered' ,
            style: {
                     color: "#FFFFFF",
                     fontSize: '26px'
             }
        },
        xAxis: {
        	categories: _grades,
        	title: {
        		text: "Grade",
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
                    if (dataSum == 0) {
                        var pcnt = 0;
                    }
                    else {
                        var pcnt = (this.value / dataSum) * 100;
                    }
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
                colorByPoint: true,
    			pointPadding: 0,
    			borderWidth: 0.5,
                groupPadding: 0,
                // colors: ['rgba(230, 91, 5, 0.6)','rgba(20, 91, 5, 0.6)']
                borderColor: "#000000"
			}
		},
        colors: ['rgba(230, 91, 5, 0.6', 'rgba(230, 91, 5, 0.6',
             'rgba(230, 91, 5, 0.6', 'rgba(230, 91, 5, 0.6',
                 'rgba(230, 91, 5, 0.6', 'rgba(230, 91, 5, 0.6',
                     'rgba(230, 91, 5, 0.6', 'rgba(230, 91, 5, 0.6',
                         'rgba(230, 91, 5, 0.6', 'rgba(230, 91, 5, 0.6',
                             'rgba(230, 91, 5, 0.6', '#FFFFFF',],
		legend: {
			enabled: false
		},
        
        credits: {
            enabled: false
        },

        tooltip: {
            formatter: function () {
                if (dataSum == 0) {
                    var pcnt = 0;
                }
                else {
                    var pcnt = (this.y / dataSum) * 100;
                }
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