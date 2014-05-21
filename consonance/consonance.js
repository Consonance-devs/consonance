
Result = new Meteor.Collection("results");

if (Meteor.isClient) {

  Session.set("recording", true);

  Meteor.startup(function(){
    window.scroll(0,1);
  });

  Template.pagecontent.events({
    'click #showrecordmenu': function(){
      Session.set("recording", true);
    }

  });

  Template.recordbuttons.events({
    'click input': function () {
      // template data, if any, is available in 'this'
      if (typeof console !== 'undefined')
        console.log("You pressed the button");
    }
  });
  Template.pagecontent.recording = function() {
    //return Session.get("recording");
    return true;
  }

  Template.uploader.events({
    'submit form': function(e, tmpl){
      
      e.preventDefault();
      var fileinput = tmpl.find('input[type=file]');
      var form = e.currentTarget;
      var file = fileinput.files[0];
      console.log(file);
      

      var userId = Meteor.default_connection._lastSessionId;
      Meteor.saveFile(file, userId + "\.mp3", "/tmp/");
      console.log("name: " + userId);
      Meteor.call("uploadFile", userId, function(err){
        if(err){
          throw err;
        }
      });
      
    }
  });

}

if (Meteor.isServer) {
  Fiber = Npm.require('fibers');
  Meteor.startup(function () {
    Result.remove({});
    Result.insert({result: "asdasd"});
    
    var traceResults = function(){
      var r = Result.find();
      console.log("Results:");
      r.forEach(function(entry){
        console.log("- " + entry.result);
      });
    }

    var exec = Npm.require('child_process').exec;
    /*Fiber( function(){
      exec('cd ../../../../../classifier; python2 main.py', Meteor.bindEnvironment( function callback(error, stdout, stderr){
        Result.insert({result: stdout});
        Result.insert({result: stderr});
        traceResults();
      }));
    }).run();*/

    Meteor.methods({
      uploadFile: function(userid){
        console.log("Upload Successful");
        Fiber( function(){
          exec('ls ../../../../../public', Meteor.bindEnvironment( function callback(error, stdout, stderr){
            console.log(stdout);
          }));
        }).run();

      }
    });

  });

}
