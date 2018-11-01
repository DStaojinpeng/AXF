$(function () {
    $("#home").width(innerWidth);

    new Swiper('#topSwiper', {
        effect: 'cube',
        grabCursor: true,
        cube: {
            shadow: true,
            slideShadows: true,
            shadowOffset: 20,
            shadowScale: 0.94
        },
        loop: true,
        pagination: '.swiper-pagination',
        autoplay: 2500,
        speed: 1000,


    });

    new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        spaceBetween: 5,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },

    });


});
