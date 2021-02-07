$(document).on('ready', function() {
    var frames = 20;
    var position;

    for (var i = 1; i < frames; i++) {
        var frame = document.createElement('div');
        frame.id = i;
        frame.classList.add('animoji-frame');
        frame.style.backgroundImage = "url('https://brettwbyron.github.io/assets/images/animoji/" + i + ".png'";
        $('#animoji').append(frame);
    }

    // animoji hover
    var interval;

    $('#animoji').on( "mouseenter touchstart", ( e ) => {
        clearInterval(interval);
        setTimeout( () => {
            position = 1;
            interval = setInterval( () => {
                var el = $('#' + position);

                if (position > frames) {
                    clearInterval(interval);
                } else {
                    if (position > 20) {position = 20;}
                    el.css('opacity','1');
                    el.css("backgroundImage", "https://brettwbyron.github.io/assets/images/animoji/" + i + ".png");
                    position++;
                }
            }, 10 );
        }, 100 );
    } );
    $('#animoji').on( "mouseout touchend", ( e ) => {
        clearInterval(interval);
        interval = setInterval( () => {
            position--;
            var el = $('#' + position);

            if (position === 1) {
                clearInterval(interval);
            } else {
                if (position > 20) {position = 20;}
                el.css('opacity','0');
            }
        }, 10 );
    } );
});