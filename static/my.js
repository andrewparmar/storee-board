$(document).ready(function(){
    

    console.log("this is a test");

    $(".hanging-close, .modal-backdrop, .modal").click(function () {
        $("#trailer-video-container").empty();
    });

    // $(".movie-tile").click(function () {
    //     var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    //     var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    //     $("#trailer-video-container").empty().append($("<iframe></iframe>", {
    //       'id': 'trailer-video',
    //       'type': 'text-html',
    //       'src': sourceUrl,
    //       console.log(sourceUrl)
    //       'frameborder': 0
    //     }));
    // });

    $(".movie-tile").click(function () {
         $(this).css("color","red");
    });

    $('.movie-tile').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
    });

});