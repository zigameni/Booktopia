var multipleCardCarousel = document.querySelector(
    "#carouselExampleControls"
);
if (window.matchMedia("(min-width: 768px)").matches) {
    var carousel = new bootstrap.Carousel(multipleCardCarousel, {
        interval: false,
    });
    var carouselWidth = $(".carousel-inner")[0].scrollWidth;
    var cardWidth = $(".carousel-item").width();
    var scrollPosition = 0;
    $("#carouselExampleControls .carousel-control-next").on("click", function () {
        if (scrollPosition < carouselWidth - cardWidth * 4) {
            scrollPosition += cardWidth;
            $("#carouselExampleControls .carousel-inner").animate(
                { scrollLeft: scrollPosition },
                600
            );
            if(scrollPosition==1024){
                scrollPosition = -256;
            }
            //console.log(scrollPosition);
        }
    });
    $("#carouselExampleControls .carousel-control-prev").on("click", function () {
        if (scrollPosition > 0) {
            scrollPosition -= cardWidth;
            $("#carouselExampleControls .carousel-inner").animate(
                { scrollLeft: scrollPosition },
                600
            );
            //console.log(scrollPosition);
        }
    });
} else {
    $(multipleCardCarousel).addClass("slide");
}