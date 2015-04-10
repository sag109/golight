function getResult(searched){
        
        if(searched == 0)
        {
            var toFill = requestInfo("get", "search/friends","",function(users){
                fill(users);//calls function to fill page with friends
            })
        }
        else
        {
            var toFill = requestInfo("get", "search/friends","",function(groups){
                fill(groups);//calls function to fill page with groups
            })
        }        

}
function fill(info){
    var resultsElement = document.getElementById("searchResults");

    var fillString = "<ul>";
    for(var i=0; i<info.length; i++){
        fillString += "<li>"+info[i]+"</li>";//should only be one type of data        
        console.log("on "+ info[i]);
    }
    fillString+= "</ul>";
    console.log("why no work? "+ fillString);
    resultsElement.innerHTML = fillString;
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