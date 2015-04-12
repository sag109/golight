var allNonFriendUsers;
var allGroups;
var globalGroupName;

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
                            "<table class=\"table table-hover\">"+
                                fillFromFriends+
                            "</table>"+
                    "</div><br>"+
                "</div><div class=\"col-lg-10 col-lg-offset-1\">"+
                    "<div class=\"panel panel-default\">"+
                      "<!-- Default panel contents -->"+
                        "<div class=\"panel-heading\">Groups- click a group to join</div>"+

                      "<!-- Table -->"+
                            "<table class=\"table table-hover\">"+
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
            fillString += "<tr><td><span class=\"glyphicon glyphicon-th-list\" aria-hidden=\"true\"></span>&nbsp&nbsp";
            fillString += "<span id=\"group"+i+"\" onclick=\"joinGroupBar(this)\">"+allGroups[i].name+"</span></td><td>"+allGroups[i].blurb;
            fillString += "</td><td id=\""+allGroups[i].name+"\"></td></tr>";//should only be one type of data        
        }
        //console.log("on "+ info[i].email);
    }
    //fillString+= "</ul>";
    return fillString;
    //console.log("why no work? "+ fillString);
    //resultsElement.innerHTML = fillString;
}

function joinGroupBar(groupElement){

    var groupName = groupElement.innerHTML;
    var joinElement = document.getElementById(groupName);
    globalGroupName = groupName;
    var barText = "<span class=\"col-lg-6\"><span class=\"input-group\"><input type=\"text\" id=\"join_blurb\" class=\"form-control\" placeholder=\"Set blurb in group\" aria-describedby=\"basic-addon1\"><span class=\"input-group-btn\"><button onclick=\"joinGroupWithBlurb(&quot "+groupName+"&quot);\" class=\"btn btn-default\" type=\"button\">Join</button></span></span></span>"
    joinElement.innerHTML =barText;
    console.log(barText);
}

function joinGroupWithBlurb(groupName){
    console.log("called joinGroupWithBlurb");
    var name = groupName.substring(1);
    console.log("name is "+name);
    var status =0;//doesn't matter anyway
    var blurb = document.getElementById("join_blurb").value;
    if(blurb)
    {
        console.log("why nnot making request");
        var info = {"groupName":name,"status":status,"blurb":blurb};
        var createGroup = requestInfo('post','group/user',info, function(response) {
            if(response.success === false){
                //document.getElementById('message').innerHTML = response.error;
                console.log(response.error);
            }
            else
            {
                console.log("successfullll");
                // document.getElementById('message').innerHTML = "You joined the group!";
            }
            
        }); 
    }
    else
        document.getElementById("join_blurb").value = "Enter a blurb first";
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

