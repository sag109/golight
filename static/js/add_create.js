$("#join").onclick(function(){
	requestInfo("post", "group/user", {
		groupName:$("#join_group_name").html()
	},
	function(){window.location.replace="/"})
});

$("#create").onclick(function(){
	requestInfo("post", "group/", {
		groupName:$("#create_group_name").html()
		groupBlurb:$("#create_group_blurb").html()
	},
	function(){window.location.replace="/"})
});

function requestInfo(method, endpoint, parameters, success) {
	parametersString = $.param(parameters);
	$.ajax(endpoint + "?" + parameters, {
		method: method,
		success: function(response) {
			return success($.parseJSON(response));
		}
	});
}