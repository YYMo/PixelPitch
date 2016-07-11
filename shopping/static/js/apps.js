var app = angular.module("app", []);

app.controller("artistListController", function($scope, $http){

  var url = "/artists_list/";
  $scope.artists = []
  $http.get(url).success( function(response) {
    $scope.students = "a";
    console.log(response);
    var artists = response['artists'];
    $scope.artists = artists;
  });
});