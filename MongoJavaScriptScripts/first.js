db = db.getSiblingDB('testing');
db.getCollectionNames();


function playerFunction () {	
	return db.player.find({ first_name: 'Jimmy', last_name: 'Carter' }).toArray()[0];	
	// return { 
	// 	// player.first_name,
	// 	// player.last_name
	// 	db.player.find({ first_name: 'Jimmy', last_name: 'Carter' }).toArray()[0].first_name,
	// 	db.player.find({ first_name: 'Jimmy', last_name: 'Carter' }).toArray()[0].last_name
	// };
}

print("--------- First Mongo SCRIPT File --------------");

var jimmy = playerFunction();
print("Players name: " + jimmy.first_name, jimmy.last_name);

function printPlayer(player) {
	var first = player.first_name;
	var last = player.last_name;
	var seasons = player.seasons;

	print("\n---------- PRINT STATISTICS FOR PLAYER ----------\n");

	print("Name: " + first + " " + last);
	print("Seasons: \n");

	for (var i = 0; i < seasons.length; i++) {
		print("\tyear: " + seasons[i].year);
		print("\tpoints: " + seasons[i].points);
		print("\trebounds: " + seasons[i].rebounds);
		print("\tminutes: " + seasons[i].minutes);
		print("\tposition: " + seasons[i].position + "\n");
	}
}

printPlayer(jimmy);


var jsonJimmy = JSON.parse(jimmy);
// var prettyJsonJimmy = JSON.stringify(jsonJimmy, null, 2);

// print(prettyJsonJimmy);