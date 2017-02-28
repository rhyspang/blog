/**
 * Created by rhys on 17-2-17.
 */

$(document).ready(function(){
    // add bootstrap responsive class
    $("img").addClass('img-responsive');
    $("img").removeAttr("style");
    $("img").wrap(function () {
        return '<a href=' + $(this)[0].src + ' data-lightbox="image-1" ></a>';
    });

    $("table").addClass("table");
    $("table").removeAttr("style");
    $("table").wrap('<div class="table-responsive"></div>')



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

