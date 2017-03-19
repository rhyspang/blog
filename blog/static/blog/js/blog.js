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



    var backButton = $('.back-to-top');
    backButton.on('click', function () {
        $('html, body').animate({
            scrollTop:0
        }, 800)
    });

    $(window).on('scroll', function () {
        if ($(window).scrollTop() > $(window).height()) {
            backButton.fadeIn();
        }else {
            backButton.fadeOut();
        }
    });

    $(window).trigger('scroll');
});

