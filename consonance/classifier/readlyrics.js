



if(Meteor.isServer){
	fs = Npm.require('fs');

	function open(filename){
		console.log("running");
		fs.readFile(filename, 'utf8', function(err, data){
			console.log(data)
		});


	}

}