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
        	backgroundColor: '#000000',
            type: 'column'
        },
        title: {
            text: plotTitle
        },
        xAxis: {
        	categories: _grades,
        	title: {
        		text: "Grades",
        		color: '#00CCFF'
        	}
        },
        yAxis: {
        	title: {
        		text: "Numbers"
        	}
        },
        plotOptions: {
			column: {
    			pointPadding: 0,
    			borderWidth: 0.5,
                groupPadding: 0,
                borderColor: "#000000"
			}
		},
		legend: {
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