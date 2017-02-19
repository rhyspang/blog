/**
 * Created by rhys on 17-2-17.
 */

$(document).ready(function(){
    // add bootstrap responsive class
    $("div img").addClass('img-responsive');
    $("table").addClass("table")
    $("table").wrap('<div class="table-responsive"></div>')
    $("img").wrap(function () {
        return '<a href=' + $(this)[0].src + ' data-lightbox="image-1" ></a>';
    });


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

