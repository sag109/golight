function addFriend() {
    var newFriend = document.getElementById("new_friend").value;
    document.getElementById("new_friend").value = "";
    
    var info = {"email":newFriend};
    var putUser = requestInfo('post','friend',info, function(response) {
        if(response.success === false){
            document.getElementById('message').innerHTML = response.error;
            console.log(response.error);
        }
        else
            document.getElementById('message').innerHTML = "";
    }); 
    
}

function removeFriend() {
    var oldFriend = document.getElementById("old_friend").value;
    document.getElementById("old_friend").value = "";
    
    var info = {"email":oldFriend};
    var putUser = requestInfo('delete','friend',info, function(response) {
        if(response.success === false){
            document.getElementById('message').innerHTML = response.error;
            console.log(response.error);
        }
        else
            document.getElementById('message').innerHTML = "";
    });
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