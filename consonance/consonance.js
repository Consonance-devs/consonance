
Result = new Meteor.Collection("results");
Consonance = new Meteor.Collection("Consonance")
Lyrics = new Meteor.Collection("Lyrics")
Alerts = new Meteor.Collection("Alerts");

if (Meteor.isClient) {
  time = null;
  userId = null;

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
            console.log(item);
            console.log("Show lyrics");
            
            var elapsed = new Date() - time;
            var t = elapsed + item.time;
            console.log("Elapsed Time: ", t);
            Lyrics.find({userId: userId}).forEach(function(i){
              //console.log(i);
              if (t >= i.start && t <= i.start + i.time){
                Session.set("lyrics", i.index);
              }
            });
            Session.set("lyricsDisp", true);

            nextLyrics();
          }
        }
      });
    });

  });

  function nextLyrics(){
    if(Lyrics.findOne({index: Session.get("lyrics"), userId: userId}) ){
      console.log("derpbug");
      Session.set("lyrics", Session.get("lyrics")+1);
      Meteor.setTimeout(nextLyrics, Lyrics.findOne({index: Session.get("lyrics"), userId: userId}).time );
      //console.log( Lyrics.findOne({index: Session.get("lyrics")}) );
    }else{
      Session.set("lyricsDisp", false);
      return;
      //Meteor.setTimeout(nextLyrics, 1000);
    }
  }

  Template.pagecontent.events({
    'click #showrecordmenu': function(){
      Session.set("recording", true);
    }
  });

  Template.pagecontent.recording = function() {
    //return Session.get("recording");
    return true;
  }
  Template.uploader.lyricsDisp = function() {
    return Session.get("lyricsDisp");
  }

  Template.lyrics.getCurrent = function(){
    return Lyrics.findOne({index: Session.get("lyrics")});
    
  }

  Template.uploader.events({
    'change input': function(e, tmpl){
      Session.set("consonating", true);
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
        //console.log(name, corr);
      }
    });

  });

  function pyWorker(filename, userId){
    Fiber( function(){
      cmd = 'cd ../../../../../classifier; pwd; ' + 'python2 worker.py ' + filename + " " + userId;
      //console.log("cmd", cmd);
      console.log("Start Processing");
      exec(cmd, Meteor.bindEnvironment( function callback(error, stdout, stderr){
        console.log(stderr);
        console.log(stdout);
        var r = stdout.split('\n');
        console.log("result: " + r[r.length-2]);
        v = parseInt(parseFloat(r[r.length-2]));
        //name = r[r.length-1];
        //corr = int(r[r.length-2]);

        /*Meteor.publish("alerts", function(){
          Alerts.find();
        });*/
        //Alerts.remove({userId: userId});
        Alerts.insert({userId: userId, time: v});

        console.log("END");
      }));
    }).run();
  }

}
