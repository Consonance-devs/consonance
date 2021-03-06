Template.navbar.events({
  'click #consonating': function () {
    console.log('Consonating clicked!')
    Session.set("page", "consonance")
  }
});
  
Template.navbar.events({
  'click #how_to_use': function () {
    console.log('How to use clicked!')
    Session.set("page", "howToUse")
  }
});

Template.navbar.events({
  'click #about': function () {
    console.log('About clicked!')
    Session.set("page", "about")
  }
});

Template.home.events({
  'click #logo': function () {
    console.log('Image clicked!')
    Session.set("page", "consonance")
  }
});

Template.pagecontent.homeDisp = function() {
  return (Session.get("page") == "home");
}

Template.pagecontent.aboutDisp = function() {
  return (Session.get("page") == "about");
}

Template.pagecontent.howToUseDisp = function() {
  return (Session.get("page") == "howToUse");
}

Template.pagecontent.uploadDisp = function() {
  return (Session.get("page") == "consonance");
}

Template.navbar.homeDispNB = function() {
  return (Session.get("page") == "home");
}

Template.navbar.aboutDispNB = function() {
  return (Session.get("page") == "about");
}

Template.navbar.howToUseDispNB = function() {
  return (Session.get("page") == "howToUse");
}

Template.navbar.uploadDispNB = function() {
  return (Session.get("page") == "consonance");
}

Template.uploader.consonatingDisp = function() {
  return Session.get("consonating");
}

$(function() {
  $('#navigation-collapse').on('click', 'li', null, function() {
    $('#navigation-collapse').collapse('hide');
  });
});