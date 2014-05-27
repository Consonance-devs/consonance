
Result = new Meteor.Collection("results");
Consonance = new Meteor.Collection("Consonance")
Lyrics = new Meteor.Collection("Lyrics")

if (Meteor.isClient) {

  Session.set("recording", true);

  Meteor.startup(function(){
    window.scroll(0,1);
    var curlyrics = 0;
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
      var userId = Meteor.default_connection._lastSessionId;

      e.preventDefault();
      var fileinput = tmpl.find('input[type=file]');
      var form = e.currentTarget;
      var file = fileinput.files[0];
      console.log("file: ", file);
      

      var filename = userId + "\.mp3";
      var directory = "/tmp/"
      Meteor.saveFile(file, filename, directory, 'binary', function(){
        console.log("name: " + userId);
        Meteor.call("uploadFile", directory + filename, userId, function(err, data){
          if(err){
            throw err;
          }else{
            console.log(data);
            curlyrics = data;
          }
        });
      });
      
    }
  });

}

if (Meteor.isServer) {
  Fiber = Npm.require('fibers');
  Meteor.startup(function () {

    Result.remove({});
    Lyrics.remove({});
    
    /*Result.insert({result: "asdasd"});
    var traceResults = function(){
      var r = Result.find();
      console.log("Results:");
      r.forEach(function(entry){
        console.log("- " + entry.result);
      });
    }*/

    var exec = Npm.require('child_process').exec;

    Meteor.methods({
      uploadFile: function(filename, userId){
        console.log("Upload Successful");
        var name = "";
        var corr = 0;
        Fiber( function(){
          cmd = 'cd ../../../../../classifier; pwd; ' + 'python2 worker.py ' + filename + " " + userId;
          //console.log("cmd", cmd);
          console.log("Start Processing");
          exec(cmd, Meteor.bindEnvironment( function callback(error, stdout, stderr){
            console.log(stderr);
            console.log(stdout);
            var r = stdout.split('\n');
            //name = r[r.length-1];
            //corr = int(r[r.length-2]);
            
            Lyrics.find({}, {"order": 1}).forEach(function(i){
              console.log(i);
            });


          }));
        }).run();
        /*console.log(name, corr);
        Consonance.find({}).forEach(function(i){
          console.log(i);
        });*/
        return 3
      }
    });

  });

}
