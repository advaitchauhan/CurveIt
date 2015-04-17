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

$(function makechart() { 
	$('#container').highcharts({
        chart: {
        	backgroundColor: 'rgba(255, 255, 255, 0.1)',
            type: 'column'
        },
        // title: {
        //     text: plotTitle,
        //     style: {
        //             color: "#FFFFFF"
        //     }
        // },
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

            }
        },
        yAxis: {
        	title: {
        		text: "Numbers",
                style: {
                    color: "#FFFFFF"
                }
        	},
            labels: {
                style: {
                    color: "#FFFFFF",
                }

            }
        },
        plotOptions: {
			column: {
    			pointPadding: 0,
    			borderWidth: 0.5,
                groupPadding: 0,
                color: 'rgb(255, 154, 51)',
                color: 'rgba(255, 154, 101, 0.7)',
                borderColor: "#000000"
			}
		},
		legend: {
			enabled: false
		},
        
        credits: {
            enabled: false
        },

		tooltip: {
			pointFormat: 'Count: <b>{point.y}</b><br/>'
		},
        series: [{
        	name: plotTitle, 
        	data: _numGrades
        }]
    });
});