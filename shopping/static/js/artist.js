var artist_app = angular.module('artist_app', []);

artist_app.controller("artistController", function($scope, $http){

  $scope.loadArtistInfo = function(){
    var url = "/artists_profile/?id=" + $scope.artist_id;
    $http.get(url).success( function(response) {
      $scope.students = "a";
      console.log(response);
      var artist = response;
      $scope.artist = artist;
      addToContent(artist['description']);

    });
  }

  $scope.init = function(id){
    console.log(id);
    $scope.artist_id = id;
  }

});

function addToContent(html){
  var d = document.getElementById("content");
  d.innerHTML = html;
}