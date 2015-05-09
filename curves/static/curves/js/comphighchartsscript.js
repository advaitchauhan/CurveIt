var _grades = [];
var _numGrades1 = [];
var _numGrades2 = [];

var _shortgrades = ["A", "B", "C", "D", "F", "P"];
var _shortnumGrades1 = [0, 0, 0, 0, 0, 0];
var _shortnumGrades2 = [0, 0, 0, 0, 0, 0,];

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

_shortnumGrades1[0] = _numGrades1[0] + _numGrades1[1] + _numGrades1[2];
_shortnumGrades1[1] = _numGrades1[3] + _numGrades1[4] + _numGrades1[5];
_shortnumGrades1[2] = _numGrades1[6] + _numGrades1[7] + _numGrades1[8];
_shortnumGrades1[3] = _numGrades1[9]
_shortnumGrades1[4] = _numGrades1[10]
_shortnumGrades1[5] = _numGrades1[11]

_shortnumGrades2[0] = _numGrades2[0] + _numGrades2[1] + _numGrades2[2];
_shortnumGrades2[1] = _numGrades2[3] + _numGrades2[4] + _numGrades2[5];
_shortnumGrades2[2] = _numGrades2[6] + _numGrades2[7] + _numGrades2[8];
_shortnumGrades2[3] = _numGrades2[9]
_shortnumGrades2[4] = _numGrades2[10]
_shortnumGrades2[5] = _numGrades2[11]

console.log('made it here')

var Class1dataSum = 0;
for (var i=0; i < _numGrades1.length; i++) {
    Class1dataSum += _numGrades1[i]
};

var Class2dataSum = 0;
for (var i=0; i < _numGrades2.length; i++) {
    Class2dataSum += _numGrades2[i]
};

for (var i=0; i < _shortnumGrades1.length; i++) {
    _pctGrades1.push(parseFloat(_shortnumGrades1[i] / Class1dataSum *100))
};

for (var i=0; i < _shortnumGrades2.length; i++) {
    _pctGrades2.push(parseFloat(_shortnumGrades2[i] / Class2dataSum *100))
};


// Calculate the average GPA for Class 1 and Class 2
var GradeSum1 = 0;
GradeSum1 = 4*_numGrades1[0] + 4*_numGrades1[1] + 3.7*_numGrades1[2] + 3.3*_numGrades1[3] + 3*_numGrades1[4] + 2.7*_numGrades1[5] + 2.3*_numGrades1[6] + 2*_numGrades1[7] + 1.7*_numGrades1[8] + 1*_numGrades1[9];

var GradeTot1 = 0
for (var i=0; i < 11; i++) {
    GradeTot1 += _numGrades1[i]
};
 
var AverageGrade1 = GradeSum1/GradeTot1;

var AvgLetGrade1 = '';

if (AverageGrade1 > 3.85) AvgLetGrade1 = 'A';
else if (AverageGrade1 > 3.5) AvgLetGrade1 = 'A-';
else if (AverageGrade1 > 3.15) AvgLetGrade1 = 'B+';
else if (AverageGrade1 > 2.85) AvgLetGrade1 = 'B';
else if (AverageGrade1 > 2.5) AvgLetGrade1 = 'B-';
else if (AverageGrade1 > 2.15) AvgLetGrade1 = 'C+';
else if (AverageGrade1 > 1.85) AvgLetGrade1 = 'C';
else if (AverageGrade1 > 1.5) AvgLetGrade1 = 'C-';
else if (AverageGrade1 > .5) AvgLetGrade1 = 'D';
else AvgLetGrade1 = 'F';

var GradeSum2 = 0;
GradeSum2 = 4*_numGrades2[0] + 4*_numGrades2[1] + 3.7*_numGrades2[2] + 3.3*_numGrades2[3] + 3*_numGrades2[4] + 2.7*_numGrades2[5] + 2.3*_numGrades2[6] + 2*_numGrades2[7] + 1.7*_numGrades2[8] + 1*_numGrades2[9];

var GradeTot2 = 0
for (var i=0; i < 11; i++) {
    GradeTot2 += _numGrades2[i]
};
 
var AverageGrade2 = GradeSum2/GradeTot2;

var AvgLetGrade2 = '';

if (AverageGrade2 > 3.85) AvgLetGrade2 = 'A';
else if (AverageGrade2 > 3.5) AvgLetGrade2 = 'A-';
else if (AverageGrade2 > 3.15) AvgLetGrade2 = 'B+';
else if (AverageGrade2 > 2.85) AvgLetGrade2 = 'B';
else if (AverageGrade2 > 2.5) AvgLetGrade2 = 'B-';
else if (AverageGrade2 > 2.15) AvgLetGrade2 = 'C+';
else if (AverageGrade2 > 1.85) AvgLetGrade2 = 'C';
else if (AverageGrade2 > 1.5) AvgLetGrade2 = 'C-';
else if (AverageGrade2 > .5) AvgLetGrade2 = 'D';
else AvgLetGrade2 = 'F';

var maxpcnt = 0;

// calculate maxpcnt: the highest percentage that any single numGrades element composes
if (Class1dataSum == 0) {
    maxpcnt = 0;
}
else {
    for (var i = 0; i < _shortnumGrades1.length; i++) {
        if ((_shortnumGrades1[i]/Class1dataSum) > maxpcnt) {
            maxpcnt = _shortnumGrades1[i]/Class1dataSum;
        }
    }
}

// calculate maxpcnt: the highest percentage that any single numGrades element composes
if (Class2dataSum != 0) {
    for (var i = 0; i < _shortnumGrades2.length; i++) {
        if ((_shortnumGrades2[i]/Class2dataSum) > maxpcnt) {
            maxpcnt = _shortnumGrades2[i]/Class2dataSum;
        }
    }
}


var tickpos = [];
dataSum = Math.max(Class1dataSum, Class2dataSum);

if (maxpcnt > .50) {tickpos = [0, 20, 40, 60, 80, 100];}
else if (maxpcnt > .25) {tickpos = [0, 10, 20, 30, 40, 50];}
else if (maxpcnt > .0) {tickpos = [0, 5, 10, 15, 20, 25];}
else {tickpos = [0];}



$(function makechart() { 
	$('#container').highcharts({
        chart: {
        	backgroundColor: 'rgba(255, 255, 255, 0.1)',
            type: 'column',
            style: {
                fontFamily: 'Raleway',
                fontSize: '24px'
            }
        },
         title: {
            text: Class1name + ' (Average Grade ' + AverageGrade1.toFixed(2) + ', ' + AvgLetGrade1 + ') vs. ' + Class2name + ' (Average Grade ' +  AverageGrade2.toFixed(2) + ', ' + AvgLetGrade2 + ')' ,
            style: {
                     color: "#FFFFFF",
                     fontSize: '26px'
             }
        },
        xAxis: {
            categories: _shortgrades,
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
                    var pcnt = this.value;
                    return pcnt.toFixed(0) + '%';
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
                groupPadding: 0.1,
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
                fontSize: '16px',
                }
        },

        tooltip: {
            formatter: function () {
                var output;
                if (this.series.name == Class1name) {
                    ouput = parseInt((this.y/100 * Class1dataSum));
                    return this.series.name + ' ' + this.x + 'count: ' + ouput + '<br>' + 'Percent: ' + Highcharts.numberFormat(this.y) + '%';
                }
                else if (this.series.name == Class2name) {
                    output = parseInt((this.y/100 * Class2dataSum));
                    return this.series.name + ' ' + this.x + ' count: ' + output + '<br>' + 'Percent: ' + Highcharts.numberFormat(this.y) + '%';
                }
            },

            style: {
                fontSize: '16px'
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