$(document).ready(function() {
	
	$("#sendRequest").click(function() {
		var method = $("#method").val();
		var endpoint = $("#endpoint").val();
		var parametersString = $("#parameters").val();
		var parametersObj = $.parseJSON(parametersString);
		var parameters = $.param(parametersObj);
		
		$.ajax(endpoint + "?" + parameters, {
			method: method,
			success: function(response) {
				$("#response").html(response);
			},
			error: function(xmlthing, status, thirdThing) {
				$("#response").html(status + "\n" + thirdThing);
			}
		});
	});
	
});