/**
 * Created by rhys on 17-2-17.
 */

$(document).ready(function(){
    // add bootstrap responsive class
    $(".entrybox img").addClass('img-responsive');
    $(".entrybox img").removeAttr("style");
    $(".entrybox img").wrap(function () {
        return '<a href=' + $(this)[0].src + ' data-lightbox="image-1" ></a>';
    });

    $(".entrybox table").addClass("table");
    $(".entrybox table").removeAttr("style");
    $(".entrybox table").wrap('<div class="table-responsive"></div>')

    var backButton = $('#backTop'),
        scrollbar = $('html, body'),
        win = $(window);

    backButton.on('click', function () {
        if (win.scrollTop() !== 0 && !scrollbar.is(':animated')) {
            scrollbar.animate({
                scrollTop:0
            }, 800)
        }
    });

    win.on('scroll', function () {
        if (win.scrollTop() > win.height()) {
            backButton.fadeIn();
        }else {
            backButton.fadeOut();
        }
    });

    $(window).trigger('scroll');

});

