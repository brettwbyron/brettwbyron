var margin = 40,
    width = 960 - margin * 2,
    height = 500 - margin * 2;
var x = d3.scale.ordinal()
    .domain(d3.range(40))
    .rangePoints([width, 0]);
var y = d3.scale.ordinal()
    .domain(d3.range(40))
    .rangePoints([0, height]);
var z = d3.scale.linear()
    .domain([0, 10, 20, 30, 40])
    .range([d3.rgb('#fcffd9'), d3.rgb('#eac1c8'), d3.rgb('#e2a3c3'), d3.rgb('#31355f'), d3.rgb('#011933')]);
var svg = d3.select('#construction')
    .append("svg")
    .attr("width", width + margin * 2)
    .attr("height", height + margin * 2)
    .append("g")
    .attr("transform", "translate(" + margin + "," + margin + ")");
svg.selectAll("circle")
    .data(y.domain())
    .enter()
    .append("circle")
    .attr("r", 12)
    .attr("cx", 0)
    .attr("cy", height)
    .style("fill", function (d) {
        return z(d);
    })
    .style("stroke", function (d) {
        return z(40 - d);
    })
    .transition()
    .duration(2000)
    .ease("linear")
    .delay(function (d) {
        return d * 300;
    })
    .each(slide);

function slide() {
    var circle = d3.select(this);
    (function repeat() {
        circle = circle.transition()
            .attr("r", 12)
            .attr("cx", 0)
            .attr("cy", 0)
            .transition()
            .attr("r", 25)
            .attr("cx", width / 2)
            .attr("cy", (height / 2) - 40)
            .transition()
            .attr("r", 12)
            .attr("cx", width)
            .attr("cy", 0)
            .transition()
            .attr("r", 12)
            .attr("cx", width)
            .attr("cy", height)
            .transition()
            .attr("r", 25)
            .attr("cx", width / 2)
            .attr("cy", (height / 2) + 40)
            .transition()
            .attr("r", 12)
            .attr("cx", 0)
            .attr("cy", height)
            .each("end", repeat);
    })();
}
svg.append("text")
    .style("fill", "black")
    .attr("y", height / 2)
    .attr("x", width / 2)
    .style("text-decoration", "underline")
    .attr("text-anchor", "middle")
    .text("UNDER CONSTRUCTION");