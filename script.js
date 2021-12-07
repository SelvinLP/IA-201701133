/**
 * Selvin Lisandro Aragón Pérez
 * 201701133
 */
function reflex_agent(location, state){
	if (state=="DIRTY") return "CLEAN";
	else if (location=="A") return "RIGHT";
	else if (location=="B") return "LEFT";
}

function test(states){
	   var location = states[0];
	   document.getElementById("log").innerHTML+="<br>Location: ".concat(location).concat(" | Status: ").concat(states[1]+"-"+states[2])
	   var state = states[0] == "A" ? states[1] : states[2];
	   
	   //Limpieza
	   if(states[2] == "CLEAN" && states[1] == "CLEAN"){
		   console.log(states[0]);
		   if(states[0] != "B") return;
		   else { var states = ["B","DIRTY","DIRTY"]; test(states); }
			
		return;
	  	}
	   var action_result = reflex_agent(location, state);

	   document.getElementById("log").innerHTML+="  ---- Location: ".concat(location).concat(" | Action: ").concat(action_result);
	   if (action_result == "CLEAN"){
		 if (location == "A") states[1] = "CLEAN";
		  else if (location == "B") states[2] = "CLEAN";
		  //Validacion para que solo este en los 8 estados
	   }
	   else if (action_result == "RIGHT") states[0] = "B";
	   else if (action_result == "LEFT") states[0] = "A";
	   
 setTimeout(
	 function(){ 
		 test(states); 
		}, 1000);
}

var states = ["A","DIRTY","DIRTY"];
test(states);