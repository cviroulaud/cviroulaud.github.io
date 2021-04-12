/**
* Template Name: Regna - v2.1.0
* Template URL: https://bootstrapmade.com/regna-bootstrap-onepage-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
!(function($) {
  "use strict";

  // Header fixed and Back to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
      $('#header').addClass('header-fixed');
    } else {
      $('.back-to-top').fadeOut('slow');
      $('#header').removeClass('header-fixed');
    }
  });

  $('.back-to-top').click(function() {
    $('html, body').animate({
      scrollTop: 0
    }, 1500, 'easeInOutExpo');
    return false;
  });

  // Initiate superfish on nav menu
  $('.nav-menu').superfish({
    animation: {
      opacity: 'show'
    },
    speed: 400
  });

  // Mobile Navigation
  if ($('#nav-menu-container').length) {
    var $mobile_nav = $('#nav-menu-container').clone().prop({
      id: 'mobile-nav'
    });
    $mobile_nav.find('> ul').attr({
      'class': '',
      'id': ''
    });
    $('body').append($mobile_nav);
    $('body').prepend('<button type="button" id="mobile-nav-toggle"><i class="fa fa-bars"></i></button>');
    $('body').append('<div id="mobile-body-overly"></div>');
    $('#mobile-nav').find('.menu-has-children').prepend('<i class="fa fa-chevron-down"></i>');

    $(document).on('click', '.menu-has-children i', function(e) {
      $(this).next().toggleClass('menu-item-active');
      $(this).nextAll('ul').eq(0).slideToggle();
      $(this).toggleClass("fa-chevron-up fa-chevron-down");
    });

    $(document).on('click', '#mobile-nav-toggle', function(e) {
      $('body').toggleClass('mobile-nav-active');
      $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
      $('#mobile-body-overly').toggle();
    });

    $(document).click(function(e) {
      var container = $("#mobile-nav, #mobile-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('#mobile-body-overly').fadeOut();
        }
      }
    });
  } else if ($("#mobile-nav, #mobile-nav-toggle").length) {
    $("#mobile-nav, #mobile-nav-toggle").hide();
  }
  // Smooth scroll for the navigation menu and links with .scrollto classes
  var scrolltoOffset = $('#header').outerHeight() - 21;
  $(document).on('click', '.nav-menu a, #mobile-nav a, .scrollto', function(e) {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        e.preventDefault();

        var scrollto = target.offset().top - scrolltoOffset;

        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu').length) {
          $('.nav-menu .menu-active').removeClass('menu-active');
          $(this).closest('li').addClass('menu-active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('#mobile-body-overly').fadeOut();
        }
        return false;
      }
    }
  });

  // Activate smooth scroll on page load with hash links in the url
  $(document).ready(function() {
    if (window.location.hash) {
      var initial_nav = window.location.hash;
      if ($(initial_nav).length) {
        var scrollto = $(initial_nav).offset().top - scrolltoOffset;
        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');
      }
    }
  });

  // Navigation active state on scroll
  var nav_sections = $('section');
  var main_nav = $('.nav-menu, #mobile-nav');

  $(window).on('scroll', function() {
    var cur_pos = $(this).scrollTop() + 200;

    nav_sections.each(function() {
      var top = $(this).offset().top,
        bottom = top + $(this).outerHeight();

      if (cur_pos >= top && cur_pos <= bottom) {
        if (cur_pos <= bottom) {
          main_nav.find('li').removeClass('menu-active');
        }
        main_nav.find('a[href="#' + $(this).attr('id') + '"]').parent('li').addClass('menu-active');
      }
      if (cur_pos < 300) {
        $(".nav-menu li:first").addClass('menu-active');
      }
    });
  });

  // Porfolio isotope and filter
  $(window).on('load', function() {
    var portfolioIsotope = $('.portfolio-container').isotope({
      itemSelector: '.portfolio-item',
      layoutMode: 'fitRows'
    });

    $('#portfolio-flters li').on('click', function() {
      $("#portfolio-flters li").removeClass('filter-active');
      $(this).addClass('filter-active');

      portfolioIsotope.isotope({
        filter: $(this).data('filter')
      });
      aos_init();
    });
  });

  // Portfolio details carousel
  $(".portfolio-details-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });

  // Init AOS
  function aos_init() {
    AOS.init({
      duration: 1000,
      once: true
    });
  }
  $(window).on('load', function() {
    aos_init();
  });

  // Initiate venobox (lightbox feature used in portofilo)
  $(document).ready(function() {
    $('.venobox').venobox();
    $('.venobox_custom').venobox({
    framewidth : '400px',                            // default: ''
    frameheight: 'auto',                            // default: ''
    border     : '10px',                             // default: '0'
    bgcolor    : '#eee',                          // default: '#fff'
    numeratio  : true,                               // default: false
    infinigall : true,                               // default: false
});
  });

  // jQuery counterUp
  $('[data-toggle="counter-up"]').counterUp({
    delay: 10,
    time: 1000
  });

    $( document ).ready(function() {
    var ctx = document.getElementById("myChart");
    var ctx2 = document.getElementById("myChart2");
    var ctx3 = document.getElementById("myChart3");
    var ctx4 = document.getElementById("myChart4");
    var ctx5 = document.getElementById("myChart5");
    var ctx6 = document.getElementById("myChart6");

    Chart.helpers.merge(Chart.defaults.global.plugins.datalabels, {
        color: '#fff',
        display: false,
        font: {
            size: 20
        }
    });

    var myChartOps = {
      type: 'doughnut',
      data: { datasets: [{data: [ 95, 5], backgroundColor: ['#9f2064','#eef2f4'], borderWidth: 0 }] },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        cutoutPercentage: 60,
        legend: {display: false},
        animation:{ duration: 2000},
        hover: {mode: null},
        tooltips:{enabled: false, backgroundColor: ['#9f2064','#eef2f4']}
       }
    };

      var myChartOps2 = {
        type: 'bar',
        data: {
          labels: ['IA', 'Architecture', 'Big Data', 'Sécurité'],
          datasets: [{data: [17, 9, 9, 7], backgroundColor: ['#ea524e','#e36c39', '#b24b1f', '#eb4d0a'], borderWidth: 1 ,
          datalabels: {
                  display: true,
                  formatter: function(value, context) {
                        return value + '%';
                    }
              }}] },
        options: {
          scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero:true
                  }
              }]
          },
          responsive: true,
          maintainAspectRatio: true,
          legend:{ display: false },
          animation: {duration: 2000},
          hover: {mode: null},
          tooltips:{ enabled: false, backgroundColor: ['#ea524e','#e36c39', '#b24b1f', '#eb4d0a']}
        }
      };



      var myChartOps3 = {
        type: 'doughnut',
        data: { datasets: [{ data: [71, 29], backgroundColor: [ '#ff8521','#eef2f4'], borderWidth: 0 }]},
        options: {
          animation:{duration: 2000},
          hover: {mode: null},
          legend: {display: false},
          tooltips:{enabled: false, backgroundColor: [ '#ff8521', '#eef2f4']},
          responsive: true,
          maintainAspectRatio: true,
          cutoutPercentage: 60,
        }
      };

      var myChartOps4 = {
        type: 'horizontalBar',
        data: {
          labels: ['CDI', 'Création de poste'],
          datasets: [{data: [83, 66], backgroundColor: ['#5c8ed2','#88cbe7'], borderWidth: 1 ,
          datalabels: {
                  display: true,
                  formatter: function(value, context) {
                        return value + '%';
                    }
              }}] },
        options: {
          scales: {
              xAxes: [{
                  ticks: {
                      beginAtZero:true
                  }
              }]
          },
          responsive: true,
          maintainAspectRatio: true,
          legend:{ display: false },
          animation: {duration: 2000},
          hover: {mode: null},
          tooltips:{ enabled: false, backgroundColor: ['#5c8ed2','#88cbe7']}
        }
      };

      var myChartOps5 = {
        type: 'bar',
        data: {
          labels: [['édition', 'de', 'logiciel'], 'e-commerce', ['banque', 'finance', 'assurance']],
          datasets: [{data: [26, 16, 16], backgroundColor: ['#0ec630','#10ac2d', '#5cbd6e'], borderWidth: 1 ,
          datalabels: {
                  display: true,
                  formatter: function(value, context) {
                        return value + '%';
                    }
              }}] },
        options: {
          scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero:true
                  }
              }]
          },
          responsive: true,
          maintainAspectRatio: true,
          legend:{ display: false },
          animation: {duration: 2000},
          hover: {mode: null},
          tooltips:{ enabled: false, backgroundColor: ['#0ec630','#10ac2d', '#5cbd6e']}
        }
      };

      var myChartOps6 = {
        type: 'line',
        data: {
          labels: [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019],
          datasets: [{data: [ 25600, 27790,30460,36870,31660,34410,37280,47590,50470,55980,58790],backgroundColor: ['#b75cbd']}  ] },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          cutoutPercentage: 60,
          legend: {display: false},
          animation:{ duration: 2000},
          hover: {mode: null},
          tooltips:{enabled: false}
         }
      };

      var myChart;
      var myChart2;
      var myChart3;
      var myChart4;
      var myChart5;
      var myChart6;


      var makePercentage = function(thischart){
            Chart.pluginService.register({
          beforeDraw: function(thischart) {
            var width = thischart.chart.width,
                height = thischart.chart.height,
                ctx = thischart.chart.ctx,
                type = thischart.config.type;

            if (type == 'doughnut')
            {
              var percent = Math.round((thischart.config.data.datasets[0].data[0] * 100) /
                            (thischart.config.data.datasets[0].data[0] +
                            thischart.config.data.datasets[0].data[1]));
              var oldFill = ctx.fillStyle;
              var fontSize = ((height - thischart.chartArea.top) / 90).toFixed(2);

              ctx.restore();
              ctx.font = fontSize + "em sans-serif";
              ctx.textBaseline = "middle"

              var text = percent + "%",
                  textX = Math.round((width - ctx.measureText(text).width) / 2),
                  textY = (height + thischart.chartArea.top) / 2;

              ctx.fillStyle = thischart.config.data.datasets[0].backgroundColor[0];
              ctx.fillText(text, textX, textY);
              ctx.fillStyle = oldFill;
              ctx.save();
            }
          }
        });
      }

      function draw1(){
        myChart = new Chart(ctx, myChartOps)
       makePercentage(myChart)
     }
     function draw2(){
        myChart2 = new Chart(ctx2, myChartOps2)
       makePercentage(myChart2)
     }
     function draw3(){
        myChart3 = new Chart(ctx3, myChartOps3)
        makePercentage(myChart3)
      }
      function draw4(){
         myChart4 = new Chart(ctx4, myChartOps4)
         makePercentage(myChart4)
       }
       function draw5(){
          myChart5 = new Chart(ctx5, myChartOps5)
          makePercentage(myChart5)
        }
        function draw6(){
           myChart6 = new Chart(ctx6, myChartOps6)
           makePercentage(myChart6)
         }

    function renderCharts(){
      draw1()
      draw2()
      draw3()
      draw4()
      draw5()
      draw6()
    }

    // Animate on scroll

      var scrolloptions = [{selector: '.card1', offset:50,callback:draw1},
                            {selector: '.card2', offset:50,callback:draw2},
                            {selector: '.card3', offset:50,callback:draw3},
                          {selector: '.card4', offset:50,callback:draw4},
                        {selector: '.card5', offset:50,callback:draw5},
                      {selector: '.card6', offset:50,callback:draw6}];      Materialize.scrollFire(scrolloptions);

      $(".card1").click( function(){
        myChart.destroy()
        myChart = new Chart(ctx, myChartOps);
        }
      )
      $(".card2").click( function(){
        myChart2.destroy()
        myChart2 = new Chart(ctx2, myChartOps2);
        }
      )
      $(".card3").click( function(){
        myChart3.destroy()
        myChart3 = new Chart(ctx3, myChartOps3)
        }
      )
      $(".card4").click( function(){
        myChart4.destroy()
        myChart4 = new Chart(ctx4, myChartOps4)
        }
      )
      $(".card5").click( function(){
        myChart5.destroy()
        myChart5 = new Chart(ctx5, myChartOps5)
        }
      )
      $(".card6").click( function(){
        myChart6.destroy()
        myChart6 = new Chart(ctx6, myChartOps6)
        }
      )
    });
})(jQuery);
