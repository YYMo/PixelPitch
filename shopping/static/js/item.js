var artist_app = angular.module('item_app', []);

artist_app.controller("itemController", function($scope, $http){

  $scope.loadItemInfo = function(){
    var url = "/get_item_info/?id=" + $scope.item_id;
    $http.get(url).success( function(response){
      console.log(response);
      var item = response;
      $scope.item = item;
      addToContent(item['description']);
    });
  }

  $scope.init = function(id){
    console.log(id);
    $scope.item_id = id;
  }

});

artist_app.controller("trackController", function($scope, $http){
  $scope.trackEvent = function(category, action, label){
    console.log("clikkk");
    ga('send', {
      hitType: 'event',
      eventCategory: category,
      eventAction: action,
      eventLabel: label,
    });
  }

});

function addToContent(html){
  var d = document.getElementById("content");
  d.innerHTML = html;
}

function htmlToElement(html) {
  var template = document.createElement('template');
  template.innerHTML = html;
  return template.content.firstChild;
}

function htmlToElements(html) {
    var template = document.createElement('template');
    template.innerHTML = html;
    return template.content.childNodes;
}
