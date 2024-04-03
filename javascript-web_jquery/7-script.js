$(document).ready(function() {
    $.ajax({
      url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
      method: 'GET',
      success: function(response) {
        $('#character').text(response.name);
      },
      error: function(xhr, status, error) {
        $('#character').text('Error fetching character name.');
      }
    });
  });
