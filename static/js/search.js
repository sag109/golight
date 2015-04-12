var allNonFriendUsers;
var allGroups;

$(document).ready(function() {
    //get friends
    getFriends();
    //get groups
    getGroups();
    //storeeee
});

function listAll(){
    var resultsElement = document.getElementById("searchResults");
    var fillFromFriends =fill();
    var fillFromGroup = fillGroups();
    resultsElement.innerHTML = "<div class=\"col-lg-10 col-lg-offset-1\">"+
                    "<div class=\"panel panel-default\">"+
                      "<!-- Default panel contents -->"+
                        "<div class=\"panel-heading\">Friends</div>"+

                      "<!-- Table -->"+
                            "<table class=\"table\">"+
                                fillFromFriends+
                            "</table>"+
                    "</div><br>"+
                "</div><div class=\"col-lg-10 col-lg-offset-1\">"+
                    "<div class=\"panel panel-default\">"+
                      "<!-- Default panel contents -->"+
                        "<div class=\"panel-heading\">Groups</div>"+

                      "<!-- Table -->"+
                            "<table class=\"table\">"+
                                fillFromGroup+
                            "</table>"+
                    "</div>"+
                "</div>";
    
}
function getFriends(){
        var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4) {
            allNonFriendUsers = JSON.parse(xmlHttp.responseText);
      }
    }
    
    xmlHttp.open("GET", "/search/friends", true); // true is for async communication
    xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttp.send(); 
    console.log("getFriends");     

}

function getGroups(){
        var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4) {
            allGroups = JSON.parse(xmlHttp.responseText);
      }
    }
    
    xmlHttp.open("GET", "/search/groups", true); // true is for async communication
    xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttp.send();      
    console.log("getGroups");

}
function fill(){
    var resultsElement = document.getElementById("searchResults");
    var searchText = document.getElementById("searchText").value;
    var noText = false;
    if(!searchText)
        noText = true;
    else
        searchText = searchText.toLowerCase()

    var fillString="";
    for(var i=0; i<allNonFriendUsers.length; i++){
        //console.log(info[i].email.indexOf());
        var email = allNonFriendUsers[i].email.toLowerCase();
        var name = allNonFriendUsers[i].name.toLowerCase();
        //console.log("email is "+email);
        //console.log("name is "+name);
        //console.log("searchText is "+searchText);
        if((email.indexOf(searchText)>-1) || (name.indexOf(searchText)>-1)|| noText)
        {
            fillString += "<tr><td><span class=\"glyphicon glyphicon-user\" aria-hidden=\"true\"></span>&nbsp&nbsp"+allNonFriendUsers[i].name+"</td></tr>";//should only be one type of data        
            //console.log("on "+ info[i].email);
        }
    }
    //fillString+= "</ul>";
    return fillString;
    //console.log("why no work? "+ fillString);
    //resultsElement.innerHTML = fillString;
}

function fillGroups(){
    var resultsElement = document.getElementById("searchResults");
    var searchText = document.getElementById("searchText").value;
    var noText = false;
    if(!searchText)
        noText = true;
    else
        searchText = searchText.toLowerCase();
    var fillString = "";
    for(var i=0; i<allGroups.length; i++){
        if(allGroups[i].name.toLowerCase().indexOf(searchText)>-1 || noText)
        {
            fillString += "<tr><td><span class=\"glyphicon glyphicon-th-list\" aria-hidden=\"true\"></span>&nbsp&nbsp"+allGroups[i].name+"</td><td>"+allGroups[i].blurb+"</td></tr>";//should only be one type of data        
        }
        //console.log("on "+ info[i].email);
    }
    //fillString+= "</ul>";
    return fillString;
    //console.log("why no work? "+ fillString);
    //resultsElement.innerHTML = fillString;
}