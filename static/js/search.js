function getResult(searched){
        console.log("sfakdhfjkekaewfjaerjio");
        var endpoint = "";
        if(searched == 0)
        {
            endpoint = "/search/friends";
            /*var toFill = requestInfo("get", "search/friends","",function(users){
                console.log("plz do something");
                fill(users);//calls function to fill page with friends
            })*/
        }
        else
        {
            endpoint = "/search/groups"
           /* var toFill = requestInfo("get", "search/groups","",function(groups){
                fill(groups);//calls function to fill page with groups
            })*/
        }  

        var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4) {
        console.log("recieved");
        console.log(JSON.parse(xmlHttp.responseText));
        if(searched ==0)
            fill(JSON.parse(xmlHttp.responseText));
        else
            fillGroups(JSON.parse(xmlHttp.responseText));
      }
    }
    
    xmlHttp.open("GET", endpoint, true); // true is for async communication
    xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttp.send();      
    console.log("sent");

}
function fill(info){
    var resultsElement = document.getElementById("searchResults");

    var fillString = "<ul>";
    for(var i=0; i<info.length; i++){
        fillString += "<li>"+info[i].email+"</li>";//should only be one type of data        
        console.log("on "+ info[i].email);
    }
    fillString+= "</ul>";
    console.log("why no work? "+ fillString);
    resultsElement.innerHTML = fillString;
}

function fillGroups(info){
    var resultsElement = document.getElementById("searchResults");

    var fillString = "<ul>";
    for(var i=0; i<info.length; i++){
        fillString += "<li>"+info[i].name+"&nbsp&nbsp&nbsp&nbsp&nbsp"+info[i].blurb+"</li>";//should only be one type of data        
        //console.log("on "+ info[i].email);
    }
    fillString+= "</ul>";
    console.log("why no work? "+ fillString);
    resultsElement.innerHTML = fillString;
}