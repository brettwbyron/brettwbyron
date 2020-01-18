function animateLines(elem) {
    // Go!
    elem.attr({strokeDashoffset: 0});
}

window.onload = function() {
    var s = Snap('svg.logo-animation');
    var capital = s.select('#capital');
    var capLen = capital.getTotalLength();
    var stem = s.select('#stem');
    var bowl = s.select('#bowl');

    this.setTimeout(() => {
        animateLines(capital);
        animateLines(stem);
        animateLines(bowl);
    }, 1000);
}



// plane flying globe example thing
// window.onload = function () {
//     var g = Snap();
//     g.attr( {
//         viewBox: [ 0, 0, 800, 600 ]
//     } );

//     Snap.load( "map.svg", function ( f ) {
//         function getShift( dot ) {
//             return "t" + ( 400 - dot.x ) + "," + ( 300 - dot.y );
//         }
//         var gr = f.select( "g" ),
//             wrd = f.select( "#world" ).attr( {
//                 fill: "#fff"
//             } ),
//             syd = f.select( "#sydney" ).attr( {
//                 fill: "red"
//             } ),
//             msk = f.select( "#san_francisco" ).attr( {
//                 fill: "red"
//             } ),
//             pth = f.select( "#flight" ),
//             pln = f.select( "#plane" ),
//             top = g.g();
//         top.attr( {
//             mask: g.rect( 100, 0, 600, 600 ).attr( {
//                 fill: "r(.5,.5,.25)#fff-#000"
//             } )
//         } );
//         top.add( gr );
//         var click = top.text( 410, 310, "click!" ).attr( {
//             font: "20px Source Sans Pro, sans-serif",
//             fill: "#fff"
//         } );
//         pth.attr( {
//             display: "none"
//         } );
//         pln = gr.g( pln, pln.clone() );
//         pln.attr( {
//             display: "none"
//         } );
//         pln[ 0 ].attr( {
//             stroke: "#fff",
//             strokeWidth: 2
//         } );
//         gr.attr( {
//             transform: getShift( {
//                 x: syd.attr( "cx" ),
//                 y: syd.attr( "cy" )
//             } )
//         } );
//         var flight = gr.path().attr( {
//             fill: "none",
//             stroke: "red",
//             strokeWidth: 3,
//             strokeDasharray: "5 3"
//         } ).insertBefore( pln );
//         window.onclick = function () {
//             pln.attr( {
//                 display: ""
//             } );
//             click.attr( {
//                 display: "none"
//             } );
//             var flag,
//                 len = Snap.path.getTotalLength( pth.attr( "d" ) );
//             Snap.animate( 0, len, function ( l ) {
//                 // Safari bug workaround: forcing redraw
//                 g.attr( {
//                     width: 100 + ( flag = !flag ? 1e-5 : 0 ) + "%"
//                 } );
//                 //
//                 var dot = pth.getPointAtLength( l );
//                 flight.attr( {
//                     d: pth.getSubpath( 0, l )
//                 } );
//                 pln.attr( {
//                     transform: "t" + [ dot.x, dot.y ] +
//                         "r" + ( dot.alpha - 90 )
//                 } );
//                 gr.attr( {
//                     transform: getShift( dot )
//                 } );
//             }, 10000 );
//         };
//     } );
// };