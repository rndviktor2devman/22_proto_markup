$.getJSON('https://api.sypexgeo.net').done(function (location){
   var city = location['city']['name_ru'];
   var country = location['country']['name_ru'];
   $.notify(
       {
           icon: 'glyphicon glyphicon-globe',
           title: city + ', ' + country,
           message: 'Угадали,'
       },
       {
           type: 'info',
           allow_dismis: true,
           placement: {
               from: 'top',
               align: 'left'
           },
           offset: {x: 30, y: 60},
           position: 'absolute',
           mouse_over: 'pause',
           delay: 5000,
           icon_type: 'class',
           template:   '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
								  '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
								  '<span data-notify="icon"></span> ' +
								  '<span data-notify="title">Ваш регион: <b>{1}</b></span> ' +
								  '<div class="text-center"><span data-notify="message">{2}</span></div>' +
								  '<div class="text-center">'+
							    '<a class="btn btn-info btn-sm" data-notify="dismiss">ДА</a>' +
							    '<span>&nbsp;</span>' +
							    '<a class="btn btn-info btn-sm" data-notify="dismiss" id="button_error_region">НЕТ</a>' +
								  '</div>'+
                                '</div>'
       }
   )
});

$('.carousel').carousel({interval: 3000});
