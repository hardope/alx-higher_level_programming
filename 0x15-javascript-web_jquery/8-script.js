// Queries an API and fetches all movie titles then inserts them
// into the UL#list_movies tag

let url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  let films = data.results;
  for (let film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
