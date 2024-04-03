$(document).ready(function() {
    $.ajax({
      url: 'https://swapi-api.hbtn.io/api/films/?format=json',
      method: 'GET',
      success: function(response) {
        var movies = response.results;
        movies.forEach(function(movie) {
          $('#list_movies').append('<li>' + movie.title + '</li>');
        });
      },
      error: function(xhr, status, error) {
        $('#list_movies').append('<li>Error fetching movies.</li>');
      }
    });
  });
