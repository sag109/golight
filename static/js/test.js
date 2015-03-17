$(document).ready(function(){
    $("#sendRequest").click(function(){
        var reqEndpoint = $("#endpoint").val();
		var reqMethod = $("#method").val();
		var paramString = $("#parameters").val();
		var valueString = $("#values").val();
		
		var params = paramString.split(" ");
		var vals = valueString.split(" ");
		
		reqData = "";
		for(var i=0; i<params.length; i++){
			reqData += params[i];
			reqData += "=";
			reqData += vals[i];
			reqData += "&"
		}
		
		$.ajax({
			method: reqMethod,
			url: reqEndpoint,
			data: reqData,
			success: function(msg) {
				$("#replyData").html(msg);
			}
		});
    });
});