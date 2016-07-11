var artist_app = angular.module('item_app', []);

artist_app.controller("itemController", function($scope, $http){

  $scope.loadItemInfo = function(){
    var url = "/get_item_info/?id=" + $scope.item_id;
    $http.get(url).success( function(response){
      console.log(response);
      var item = response;
      $scope.item = item;

    });
  }

  $scope.init = function(id){
    console.log(id);
    $scope.item_id = id;
  }

});