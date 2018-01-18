"use strict";
$(function(){

	$(".toggler").on("click",function(e){
		e.preventDefault();
		$(this).siblings().find(".toggled").slideUp();
		$(this).find(".toggled").slideToggle();
	});

	$(".rslides-top").responsiveSlides({
		nav:true,
		prevText:"<i class='zmdi zmdi-chevron-left zmdi-hc-3x'></i>",
		nextText:"<i class='zmdi zmdi-chevron-right zmdi-hc-3x'></i>"
	});

	$(".slick-featured").slick({
		slidesToShow: 4,
		slidesToScroll: 1,
		prevArrow: "<i class='zmdi zmdi-chevron-left zmdi-hc-lg'></i>",
		nextArrow: "<i class='zmdi zmdi-chevron-right zmdi-hc-lg'></i>",
		responsive: [
   		{
			breakpoint: 992,
			settings: {
				slidesToShow: 2
			}
		},
		{
			breakpoint: 768,
			settings: {
				slidesToShow: 1
			}
		}]
	});
	
	$(".slick-detail").slick({
		slidesToShow: 3,
		slidesToScroll: 1,
		vertical: true,
		draggable:false,
		prevArrow: "<i class='zmdi zmdi-chevron-up zmdi-hc-lg'></i>",
		nextArrow: "<i class='zmdi zmdi-chevron-down zmdi-hc-lg'></i>"
	});

	$('.slick-sayings').slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: false,
		fade: true,
		asNavFor: '.slick-people',
		arrows: true,
		prevArrow:"<i class='zmdi zmdi-chevron-left zmdi-hc-lg'></i>",
		nextArrow:"<i class='zmdi zmdi-chevron-right zmdi-hc-lg'></i>"
	});

	$('.slick-people').slick({
		slidesToShow: 3,
		slidesToScroll: 1,
		asNavFor: '.slick-sayings',
		centerMode: true,
		focusOnSelect: true
	});

	$(".slick-blog").slick({
		slidesToShow: 3,
		slidesToScroll: 1,
		prevArrow: "<i class='zmdi zmdi-chevron-left zmdi-hc-lg'></i>",
		nextArrow: "<i class='zmdi zmdi-chevron-right zmdi-hc-lg'></i>",
		responsive: [
   		{
			breakpoint: 992,
			settings: {
				slidesToShow: 2
			}
		},
		{
			breakpoint: 768,
			settings: {
				slidesToShow: 1
			}
		}]
	});
	
	$(".partners-slick").slick({
		slidesToShow: 5,
		slidesToScroll: 1,
		prevArrow: "<i class='zmdi zmdi-chevron-left zmdi-hc-lg'></i>",
		nextArrow: "<i class='zmdi zmdi-chevron-right zmdi-hc-lg'></i>",
		responsive: [
   		{
			breakpoint: 992,
			settings: {
				slidesToShow: 3
			}
		},
		{
			breakpoint: 768,
			settings: {
				slidesToShow: 1
			}
		}]		
	});

	$(".option-title").on("click", function(e){
		e.preventDefault();
		var $parent = $(this).parent();
		$parent.addClass("opened");
		$parent.siblings().removeClass("opened");
	});

	var $slider = $("#slider-range");
	var $amount = $("#amount");
	
	$slider.slider({
      range: true,
      min: 100,
      max: 400,
      values: [ 100, 350 ],
      slide: function( event, ui ) {
        $amount.html( "$" + ui.values[ 0 ] + ".00 - $" + ui.values[ 1 ] + ".00" );
      }
    });

    $amount.html( "$" + $slider.slider( "values", 0 ) +
      ".00 - $" + $slider.slider( "values", 1 ) + ".00" );

	$(".quantity-spinner a.minus").on("click", function(e){
		var elem = $(this).parent().find("span");
		var value = parseInt(elem.html(),10);
		if(value>1){
			value--;
			elem.html(value<10?"0"+value:value); 
			}
		e.preventDefault();
	});


	$(".quantity-spinner a.plus").on("click", function(e){
		var elem = $(this).parent().find("span");
		var value = parseInt(elem.html(),10);
		value++;
		elem.html(value<10?"0"+value:value); 
		e.preventDefault();
	});

	$(".sandwitch").on("click",function(e){
		e.preventDefault();
		$(".navigation ul").slideToggle();
	})
});