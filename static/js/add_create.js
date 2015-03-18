$("#join").click(function(){
	requestInfo("post", "group/user", {
		groupName:$("#join_group_name").val()
	},
	function(){window.location.replace="/"})
});

$("#create").click(function(){
	$("#create_group_name").val("It works!!!");
	$("#create_group_blurb").val("It works!!!");
	requestInfo("post", "group/", {
		groupName:$("#create_group_name").val(),
		blurb:$("#create_group_blurb").val()
	},
	function(){window.location.href="/"})
});

function requestInfo(method, endpoint, parameters, success) {
	parametersString = $.param(parameters);
	$.ajax(endpoint + "?" + parametersString, {
		method: method,
		success: function(response) {
			return success($.parseJSON(response));
		}
	});
}