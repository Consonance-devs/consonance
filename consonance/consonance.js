
Result = new Meteor.Collection("results");
Consonance = new Meteor.Collection("Consonance")
Lyrics = new Meteor.Collection("Lyrics")
Alerts = new Meteor.Collection("Alerts");

if (Meteor.isClient) {
  time = null;
  userId = null;

  Session.set("consonating", false);
  Session.set("page", "home");
  Session.set("recording", true);
  Session.set("lyricsDisp", false);
  Session.set("lyrics", 0);

  Meteor.startup(function(){
    window.scroll(0,1);

    Meteor.autosubscribe(function() {
      Alerts.find().observe({
        added: function(item){
          if(item.userId == userId){
            stopFadingLyrics();
            console.log(item);
            console.log("Show lyrics");
            
            var elapsed = new Date() - time;
            var t = elapsed + item.time;
            console.log("Elapsed Time: ", t);
            Lyrics.find({userId: userId}).forEach(function(i){
              if (t >= i.start && t <= i.start + i.time){
                Session.set("lyrics", i.index);
              }
            });
            Session.set("consonating", false);
            Session.set("lyricsDisp", true);

            nextLyrics();
          }
        }
      });
    });

  });

  function nextLyrics(){
    if(Lyrics.findOne({index: Session.get("lyrics"), userId: userId}) ){
      Session.set("lyrics", Session.get("lyrics")+1);
      Meteor.setTimeout(nextLyrics, Lyrics.findOne({index: Session.get("lyrics"), userId: userId}).time );
    }else{
      Session.set("lyricsDisp", false);
      return;
    }
  }

  Template.pagecontent.events({
    'click #showrecordmenu': function(){
      Session.set("recording", true);
    }
  });

  Template.pagecontent.recording = function() {
    return true;
  }
  Template.uploader.lyricsDisp = function() {
    return Session.get("lyricsDisp");
  }

  Template.lyrics.getCurrent = function(){
    return Lyrics.findOne({index: Session.get("lyrics"), userId: userId});
    
  }

  Template.uploader.events({
    'change input': function(e, tmpl){
      Session.set("consonating", true);
      startFadingLyrics();
      startSlideAnimation();
      time = new Date();
      userId = Meteor.default_connection._lastSessionId;

      e.preventDefault();
      var fileinput = tmpl.find('input[type=file]');
      var form = e.currentTarget;
      var file = fileinput.files[0];
      console.log("file: ", file);

      var filename = userId + "\.mp3";
      var directory = "/tmp/";
      Meteor.saveFile(file, filename, directory, 'binary', function(){
        console.log("name: " + userId);
        Meteor.call("uploadFile", directory + filename, userId, function(err, data){
          if(err){
            throw err;
          }else{
          }
        });
      });
      
    }
  });

}

if (Meteor.isServer) {
  Fiber = Npm.require('fibers');
  exec = Npm.require('child_process').exec;
  
  Meteor.startup(function () {
    Lyrics.remove({});
    Alerts.remove({});

    Meteor.methods({
      uploadFile: function(filename, userId){
        Lyrics.remove({userId: userId});
        console.log("Upload Successful");
        var name = "";
        var corr = 0;
        pyWorker(filename, userId);
      }
    });

  });

  function pyWorker(filename, userId){
    Fiber( function(){
      cmd = 'cd ../../../../../classifier; pwd; ' + 'python2 worker.py ' + filename + " " + userId;
      console.log("Start Processing");
      exec(cmd, Meteor.bindEnvironment( function callback(error, stdout, stderr){
        console.log(stderr);
        console.log(stdout);
        var r = stdout.split('\n');
        console.log("result: " + r[r.length-2]);
        v = parseInt(parseFloat(r[r.length-2]));
        
        Alerts.insert({userId: userId, time: v});

        console.log("END");
      }));
    }).run();
  }

}
