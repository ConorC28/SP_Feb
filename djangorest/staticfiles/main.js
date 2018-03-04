$(window).scroll(function() {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      if (scrollTop < 100) {
            $('div.BodyContainer').addClass('active').stop(true, true).fadeIn();
      }
      else {
            
			$('div.BodyContainer.active').removeClass('active').stop(true, true).fadeOut();
      }
});