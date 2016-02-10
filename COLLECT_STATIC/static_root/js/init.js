/*


*/
// <script>
    $( document ).ready(function(){
        $('.slider').slider({full_width: true, indicators: false, height: '61vh'});
        $('.materialboxed').materialbox();
        $('#textarea1').trigger('autoresize');
        $('.button-collapse').sideNav();
        $('.parallax').parallax();
    });
//  </script>
//  <script>
    $( document ).ready(function(){
        //Sort random function
        function random(owlSelector){
            owlSelector.children().sort(function(){
                return Math.round(Math.random()) - 0.5;
            }).each(function(){
                $(this).appendTo(owlSelector);
            });
        }
        $("#owl-demo").owlCarousel({
            lazyLoad: true,
            pagination: false,
            navigation: true,
            navigationText: [
                "<i class='icon-chevron-left icon-white'></i>",
                "<i class='icon-chevron-right icon-white'></i>"
               ],
            beforeInit : function(elem){
                //Parameter elem pointing to $("#owl-demo")
                random(elem);
            }
        });
    });
// </script>
// <script>
    function initMap() {
      var usRoadMapType = new google.maps.StyledMapType([
        {
            "featureType": "landscape",
            "stylers": [{
                "saturation": -100
            }, {
                "lightness": 65
            }, {
                "visibility": "on"
            }]
        }, {
            "featureType": "poi",
            "stylers": [{
                "saturation": -100
            }, {
                "lightness": 51
            }, {
                "visibility": "simplified"
            }]
        }, {
            "featureType": "road.highway",
            "stylers": [{
                "saturation": -100
            }, {
                "visibility": "simplified"
            }]
        }, {
            "featureType": "road.arterial",
            "stylers": [{
                "saturation": -100
            }, {
                "lightness": 30
            }, {
                "visibility": "on"
            }]
        }, {
            "featureType": "road.local",
            "stylers": [{
                "saturation": -100
            }, {
                "lightness": 40
            }, {
                "visibility": "on"
            }]
        }, {
            "featureType": "transit",
            "stylers": [{
                "saturation": -100
            }, {
                "visibility": "simplified"
            }]
        }, {
            "featureType": "administrative.province",
            "stylers": [{
                "visibility": "off"
            }]
        }, {
            "featureType": "water",
            "elementType": "labels",
            "stylers": [{
                "visibility": "on"
            }, {
                "lightness": -25
            }, {
                "saturation": -100
            }]
        }, {
            "featureType": "water",
            "elementType": "geometry",
            "stylers": [{
                "hue": "#ffff00"
            }, {
                "lightness": -25
            }, {
                "saturation": -97
            }]
        }], {name: 'Tequisquiapan, Queretaro'});

        var map = new google.maps.Map(document.getElementById('mapa'), {
            zoom: 10,
            center: {lat: 20.522731, lng: -99.891585},
            mapTypeControlOptions: {
              mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'usroadatlas']
            }
        });
        var marker = new google.maps.Marker({
            position: map.center,
            map: map,
            title: 'Tequisquiapan, Queretaro'
        });

      map.mapTypes.set('usroadatlas', usRoadMapType);
      map.setMapTypeId('usroadatlas');
    }
    google.maps.event.addDomListener(window, 'load', initMap);
//  </script>