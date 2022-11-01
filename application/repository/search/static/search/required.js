function checkRequired() {
var array =[]
var unarray=[]
var volume= []
var checkboxes = document.querySelectorAll('input[type=checkbox]:checked');

for (var i =0; i < checkboxes.length; i++){

	array.push(checkboxes[i].value);
}
console.log(array);


for (var j=0; j < array.length; j++){
	console.log("v_"+array[j])
	if (document.getElementById(array[j]).checked==true){
	 document.getElementById("s_"+array[j]).setAttribute("required","");
	 document.getElementById("v_"+array[j]).setAttribute("required","");
	 document.getElementById("d_"+array[j]).setAttribute("required","");
	 document.getElementById("b_"+array[j]).setAttribute("required","");
	 document.getElementById("c_"+array[j]).setAttribute("required","");
	 document.getElementById("f_"+array[j]).setAttribute("required","");
}
	
}

var unchecked = document.querySelectorAll('input[type=checkbox]:not(:checked)');
for (var k=0; k < unchecked.length; k++){
	unarray.push(unchecked[k].value);

}

console.log(unarray)
for (var t=0; t<unarray.length;t++){

	if (document.getElementById(unarray[t]).checked==false){
	 document.getElementById("s_"+unarray[t]).removeAttribute("required");
	 document.getElementById("v_"+unarray[t]).removeAttribute("required");
	 document.getElementById("d_"+unarray[t]).removeAttribute("required");
	 document.getElementById("b_"+unarray[t]).removeAttribute("required");
	 document.getElementById("c_"+unarray[t]).removeAttribute("required");
	 document.getElementById("f_"+unarray[t]).removeAttribute("required");
}

}

}



