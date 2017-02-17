/**
 * Created by rhys on 17-2-17.
 */
var test = [];

$(document).ready(function(){
    $("div img").addClass('img-responsive');
    $("table").addClass("table")
    $("table").wrap('<div class="table-responsive"></div>')
    $("img").wrap(function () {
        test.push($(this));
        return '<a href=' + $(this)[0].src + ' data-lightbox="image-1" ></a>';
    });

});

