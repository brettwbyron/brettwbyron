window.onload = function() {
    var g = Snap();
    g.attr({
        viewBox: [0, 0, 228.7, 300]
    })

    Snap.load("../images/logo.svg", function(f) {
        var path = f.select("#capital");
        var flag = Snap.path.getTotalLength( path.attr( "d" ) );
        // var len = Snap.animate( 0, len, function ( l ) {
            // g.attr({width: 100 + ( flag = !flag ? 1e-5 : 0 ) + "%"});
            // var dot = path.getPointAtLength( l );
        // });
    });
}