$(window).on("load", function() {
    // Interactive Map
    jQuery('object.svg').each(function(){
        var $img = jQuery(this);
        var imgID = $img.attr('id');
        var imgClass = $img.attr('class');
        var imgURL = $img.attr('src');

        jQuery.get("../assets/images/north-america.svg", function(data) {
            // Get the SVG tag, ignore the rest
            var $svg = jQuery(data).find('svg');

            // Add replaced image's ID to the new SVG
            if(typeof imgID !== 'undefined') {
                $svg = $svg.attr('id', imgID);
            }

            // Remove any invalid XML tags as per http://validator.w3.org
            $svg = $svg.removeAttr('xmlns:a');

            // Replace image with new SVG
            $img.replaceWith($svg);

            // Highlight US with blue
            [...$('[id*="US-"]')].forEach(child => {
                child.addEventListener('mouseover', (e) => {
                    console.log(e);
                    child.style.transition = 'all 0.5s ease';
                    child.style.fill = '#a5c0cd';
                });
                child.addEventListener('mouseout', (e) => {
                    console.log(e);
                    child.style.fill = 'black';
                });
                child.addEventListener('click', (e) => {
                    alert('You can make clicking the element with [id="' + child.id + '"] do whatever you want! :)');
                });
            });
            // Hightlight Canada with yellow
            [...$('[id*="CA-"]')].forEach(child => {
                child.addEventListener('mouseover', (e) => {
                    console.log(e);
                    child.style.transition = 'all 0.5s ease';
                    child.style.fill = '#fff200';
                });
                child.addEventListener('mouseout', (e) => {
                    console.log(e);
                    child.style.fill = 'black';
                });
                child.addEventListener('click', (e) => {
                    alert('You can make clicking the element with [id="' + child.id + '"] do whatever you want! :)');
                });
            });
            // Highlight Mexico with red
            [...$('[id*="MX-"]')].forEach(child => {
                child.addEventListener('mouseover', (e) => {
                    console.log(e);
                    child.style.transition = 'all 0.5s ease';
                    child.style.fill = '#de8e8b';
                });
                child.addEventListener('mouseout', (e) => {
                    console.log(e);
                    child.style.fill = 'black';
                });
                child.addEventListener('click', (e) => {
                    alert('You can make clicking the element with [id="' + child.id + '"] do whatever you want! :)');
                });
            });
        }, 'xml');
    });
});