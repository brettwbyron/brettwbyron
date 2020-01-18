$( document ).on( 'ready', () => {
    // Scroll Animation Example script
    var headerHeight = $('.page-header').outerHeight();

    var $sectionLTR = $( '#scrollAnimationLTR #mask' );
    var topLTR = $sectionLTR.offset().top;
    var startLTR = headerHeight + 120;
    var endLTR = topLTR;

    var $sectionRTL = $( '#scrollAnimationRTL #mask' );
    var topRTL = $sectionRTL.offset().top;
    var startRTL = $(window).height() + headerHeight + 120;
    var endRTL = topRTL;

    var prevSt = 0;

    $('#scrollAnimationLTR #topPosition').text(topLTR);
    $('#startPositionLTR').text(startLTR + 'px');
    $('.start-data-ltr').css({'top':startLTR + 'px'});
    $('#endPositionLTR').text(endLTR + 'px');
    $('.end-data-ltr').css({'top':endLTR + 'px'});
    $('#scrollAnimationLTR #maskData').text('ratio = ( 0 - ' + startLTR + ' ) / ( ' + endLTR + ' - ' + startLTR + ' ) ');
    $('#scrollAnimationLTR #leftData').text('0%');

    $('#scrollAnimationRTL #topPosition').text(topRTL);
    $('#startPositionRTL').text(startRTL + 'px');
    $('.start-data-rtl').css({'top':startRTL + 'px'});
    $('#endPositionRTL').text(endRTL + 'px');
    $('.end-data-rtl').css({'top':endRTL + 'px'});
    $('#scrollAnimationRTL #maskData').text('ratio = ( 0 - ' + startRTL + ' ) / ( ' + endRTL + ' - ' + startRTL + ' ) ');
    $('#scrollAnimationRTL #rightData').text('0%');

    $( window ).scroll( function () {
        var st = $( this ).scrollTop();
        var ratioLTR = (( st - startLTR ) / ( endLTR - startLTR )).toFixed(2);
        var ratioRTL = (( st - startRTL ) / ( endRTL - startRTL )).toFixed(2);

        // show scroll data in scroll data section
        $('#scrollPosition').text(st);

        var scrollDown = prevSt <= st;

        if ( scrollDown ) { // if scrolling down
            // if scroll position >= start position
            if ( st >= startLTR && ratioLTR <= 1.1 ) {
                $sectionLTR.css( {
                    'left': ( ratioLTR * 100 ) + "%"
                } );
            }
            if ( st >= startRTL && ratioRTL <= 1.1 ) {
                $sectionRTL.css( {
                    'right': ( ratioRTL * 100 ) + "%"
                } );
            }
        } else { // else scrolling up
            if ( ratioLTR >= 0 ) {
                $sectionLTR.css( {
                    'left': ( ratioLTR * 100 ) + "%"
                } );
            }
            if ( ratioRTL >= 0 ) {
                $sectionRTL.css( {
                    'right': ( ratioRTL * 100 ) + "%"
                } );
            }
        }

        if ( st == 0 ) { // if at top of page make sure everything is reset
            $sectionLTR.css( {
                'left': '0%'
            } );
            $sectionRTL.css( {
                'right': '0%'
            } );
        }

        if ( st <= startLTR ) {
            $('#scrollAnimationLTR #maskData').text('ratio = ( ' + st + ' - ' + startLTR + ' ) / ( ' + endLTR + ' - ' + startLTR + ' ) = ' + 0);
            $('#leftData').text('0%');
        } else if (st >= endLTR) {
            $('#scrollAnimationLTR #maskData').text('ratio = ( ' + st + ' - ' + startLTR + ' ) / ( ' + endLTR + ' - ' + startLTR + ' ) = ' + 1);
            $('#leftData').text('100%');
        } else {
            $('#scrollAnimationLTR #maskData').text('ratio = ( ' + st + ' - ' + startLTR + ' ) / ( ' + endLTR + ' - ' + startLTR + ' ) = ' + ratioLTR);
            $('#leftData').text(ratioLTR * 100 + '%');
        }

        if ( st <= startRTL ) {
            $('#scrollAnimationRTL #maskData').text('ratio = ( ' + st + ' - ' + startRTL + ' ) / ( ' + endRTL + ' - ' + startRTL + ' ) = ' + 0);
            $('#rightData').text('0%');
        } else if (st >= endRTL) {
            $('#scrollAnimationRTL #maskData').text('ratio = ( ' + st + ' - ' + startRTL + ' ) / ( ' + endRTL + ' - ' + startRTL + ' ) = ' + 1);
            $('#rightData').text('100%');
        } else {
            $('#scrollAnimationRTL #maskData').text('ratio = ( ' + st + ' - ' + startRTL + ' ) / ( ' + endRTL + ' - ' + startRTL + ' ) = ' + ratioRTL);
            $('#rightData').text(ratioRTL * 100 + '%');
        }

        prevSt = st;
    } );
});