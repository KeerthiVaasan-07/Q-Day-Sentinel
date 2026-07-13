document.getElementById("uploadForm").addEventListener("submit", async function(e){

e.preventDefault();

const file=document.getElementById("file").files[0];

let formData=new FormData();

formData.append("file",file);

const response=await fetch("/scan",{

method:"POST",
body:formData

});

const data=await response.json();

let html="";

html+="<h2>Results</h2>";

html+="<table>";

html+="<tr>";

html+="<th>Issue</th>";

html+="<th>Severity</th>";

html+="<th>Recommendation</th>";

html+="</tr>";

data.forEach(v=>{

let rec="";

switch(v.issue){

case "RSA-2048":
rec="CRYSTALS-Kyber";
break;

case "RSA-1024":
rec="CRYSTALS-Kyber";
break;

case "AES-CBC":
rec="AES-256-GCM";
break;

case "SHA-1":
rec="SHA-3";
break;

default:
rec="None";

}

html+=`

<tr>

<td>${v.issue}</td>

<td>${v.severity}</td>

<td>${rec}</td>

</tr>

`;

});

html+="</table>";

document.getElementById("result").innerHTML=html;

});
