var statusValue=-1;

function setStatusValue(val){
    statusValue=val;
    console.log("statusValue is "+statusValue);
}
function joinGroup() {
    var name = document.getElementById("join_group_name").value;
    var blurb = document.getElementById("join_blurb").value;
    
    var info = {"groupName":name,"status":0,"blurb":blurb};
    var createGroup = requestInfo('post','group/user',info, function(response) {
        if(response.success === false){
            document.getElementById('message').innerHTML = response.error;
            console.log(response.error);
        }
        else
            document.getElementById('message').innerHTML = "You joined the group!";
            
    }); 
    
            document.getElementById("join_group_name").value = "";
            document.getElementById("join_status").value = "";
            document.getElementById("join_blurb").value = "";

}

function createGroup() {
    var crName = document.getElementById("create_group_name").value;
    var crBlurb = document.getElementById("create_group_blurb").value;
    crName = crName.split(" ").join("_");
    console.log(crName +"crName");
    var info = {"groupName":crName,"blurb":crBlurb};
    var createGroup = requestInfo('post','group',info, function(response) {
        if(response.success === false){
            document.getElementById('message').innerHTML = response.error;
            console.log(response.error);
        }
        else
            document.getElementById('message').innerHTML = "Group created!";
    }); 
    
    document.getElementById("create_group_name").value = "";
    document.getElementById("create_group_blurb").value = "";

}

function requestInfo(method, endpoint, parameters, success) {
	parametersString = $.param(parameters);
	$.ajax(endpoint + "?" + parametersString, {
		method: method,
		success: function(response) {
			return success($.parseJSON(response));
		}
	});
}

