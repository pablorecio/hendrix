$(function () {

    function convertToSlug(text)
    {
        return text
            .toLowerCase()
            .replace(/[^\w ]+/g,'')
            .replace(/ +/g,'-');
    }

    window.chart = new Highcharts.Chart({

        chart: {
            renderTo: 'skills-graph',
            polar: true,
            type: 'line'
        },

        colors: ["#CBE86B"],

        title: {
            text: ''
        },

        pane: {
            size: '80%'
        },

        xAxis: {
            categories: ['Python', 'GAE', 'Javascript',
                    'Big Data', 'UNIX systems', 'Open Source', 'Git', 'Django'],
            tickmarkPlacement: 'on',
            lineWidth: 0
        },

        yAxis: {
            gridLineInterpolation: 'polygon',
            lineWidth: 0,
            tickInterval: 10,
            min: 0,
            max: 10,
            labels: {
               enabled: false
           }
        },

        plotOptions: {
            line: {
                marker: {
                    enabled: false
                },
                point: {
                    events: {
                        mouseOver: function() {
                            $(".skill-" + convertToSlug(this.category)).addClass("hovered-skill");
                        },
                        mouseOut: function() {
                            $(".skill-" + convertToSlug(this.category)).removeClass("hovered-skill");
                        }
                    }
                }
            }
        },

        legend: {
            enabled: false
        },

        tooltip: {
            enabled: false
        },

        credits: {
            enabled: false
        },

        series: [{
            name: 'Skills',
            data: [9, 7, 6, 5, 7, 7, 9, 10]
        }]
    });
});
