$( document ).on( 'ready', () => {
    // background follow mouse
    const els = document.querySelectorAll( "ul.examples li" );

    els.forEach( el => {
        el.addEventListener( "mousemove", ( e ) => {
            el.style.backgroundPositionX = ( e.offsetX / el.parentElement.clientWidth ) * 100 + "%";
            el.style.backgroundPositionY = ( e.offsetY / el.parentElement.clientHeight ) * 100 + "%";
        } );
    } );
} );