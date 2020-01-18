$( document ).on( 'ready', () => {
    // pulse
    $( 'a[href="#crap-gui"]' ).on( 'click', function ( e ) {
        console.log( e );

        setTimeout( () => {
            $( '#crap-gui' ).css( 'background-color', 'rgba(#a5c0cd, 0.1)' ); // variable $color-secondary
            setTimeout( () => {
                $( '#crap-gui' ).css( 'background-color', 'transparent' ); // original background-color
            }, 1500 );
        }, 750 );
        e.preventDefault();
    } );
} );