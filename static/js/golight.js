var golight={};


golight.myStatus = function(success){

    $.ajax("/api2/status", {
            method: "GET", 
            success: function(response){
                success(response);
            }
    });

};



function requestInfo(method, endpoint, parameters, success) {

    parametersString = $.param(parameters);
    $.ajax(endpoint + "?" + parametersString, {
        method: method,
        success: function(response) {
            return success($.parseJSON(response));
        }
    });
}