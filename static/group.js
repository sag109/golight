function putGroup(){
    alert("called method");
    var groupNameIn = document.getElementById('group_name');
    if(groupNameIn){
        var groupName = groupNameIn.value;
    var xmlHttp = createXmlHttp();
    xmlHttp.onreadystatechange = function() {
      if(request.readyState==4 && request.status==200){
      document.getElementById('group_name').value=""; 
      alert("I state changed");
    }else if(request.readyState==4){
      alert("something went wrong");
    }
    };
    var paramString = 'groupName=' + escape(groupName);
    xmlHttp.open("GET", '/', true); // true is for async communication
    xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttp.send(paramString);
    alert("I hit the end");
  }
}

function createXmlHttp() {
  var xmlhttp;
  if (window.XMLHttpRequest) {
    xmlhttp = new XMLHttpRequest();
  } else {
    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
  }
  if (!(xmlhttp)) {
    alert("Your browser does not support AJAX!");
  }
  return xmlhttp;
}