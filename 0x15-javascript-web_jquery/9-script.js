// Queries an API for wind speed in SF and replaces the text of the
// div#sf_wind_speed tag with the speed

let url = 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json';
$.get(url, function (data) {
  let wind = data.query.results.channel.wind.speed;
  $('div#sf_wind_speed').text(wind);
});
