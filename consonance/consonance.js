
Result = new Meteor.Collection("results");
Consonance = new Meteor.Collection("Consonance")
Lyrics = new Meteor.Collection("Lyrics")
Alerts = new Meteor.Collection("Alerts");

if (Meteor.isClient) {

  Session.set("recording", true);
  Session.set("lyricsDisp", false);
  Session.set("lyrics", 0);

  Meteor.startup(function(){
    window.scroll(0,1);
    var curlyrics = 0;

    Meteor.autosubscribe(function() {
      Alerts.find().observe({
        added: function(item){ 
          console.log("Show lyrics");
          nextLyrics();
        }
      });
    });

  });

  function nextLyrics(){
    if(Lyrics.findOne({index: Session.get("lyrics")}) ){
      Session.set("lyrics", Session.get("lyrics")+1);
      Meteor.setTimeout(nextLyrics, Lyrics.findOne({index: Session.get("lyrics")}).time );
      //console.log( Lyrics.findOne({index: Session.get("lyrics")}) );
    }else{
      //Session.set("lyricsDisp", false);
      console.log("empty");
      //return;
      //Meteor.setTimeout(nextLyrics, 1000);
    }
  }

  Template.pagecontent.events({
    'click #showrecordmenu': function(){
      Session.set("recording", true);
    }
  });

  Template.navbar.events({
    'click #consonating': function () {
      console.log('Consonating clicked!')
    }
  });
    
  Template.navbar.events({
    'click #how_to_use': function () {
      console.log('How to use clicked!')
    }
  });

  Template.navbar.events({
    'click #about': function () {
      console.log('About clicked!')
    }
  });

  Template.pagecontent.recording = function() {
    //return Session.get("recording");
    return true;
  }
  Template.pagecontent.lyricsDisp = function() {
    return Session.get("lyricsDisp");
  }

  Template.lyrics.getCurrent = function(){
    return Lyrics.findOne({index: Session.get("lyrics")});
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
            Session.set("lyrics", data);
            Session.set("lyricsDisp", true);
            console.log("lyrics: ");
            //Meteor.setInterval(derpfunc, 10000);
            //console.log(Lyrics.findOne({index: data}))
            /*Meteor.setTimeout(function (){
              var f = Lyrics.findOne({index: data});
              console.log(f):
              var t = f.time;
              Meteor.setTimeout(nextLyrics, t);
            }, 5000);*/

          }
        });
      });
      
    }
  });

}

if (Meteor.isServer) {
  Fiber = Npm.require('fibers');
  Meteor.startup(function () {
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
        Lyrics.remove({userid: userId});
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
            
            /*Lyrics.find({}, {"index": 1}).forEach(function(i){
              console.log(i);
            });*/

            Meteor.publish("alerts", function(){
              Alerts.find();
            });
            Alerts.remove({});
            Alerts.insert({message: "Some message to show on every client.", userId: userId});

            console.log("END");
          }));
        }).run();
        /*console.log(name, corr);
        Consonance.find({}).forEach(function(i){
          console.log(i);
        });*/
        return 1
      }
    });

  });

}
