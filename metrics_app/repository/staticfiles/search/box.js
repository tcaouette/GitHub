const box = document.getElementById("box");

//pos.forEach(element => {cell.innerText = (element)});
function makebox(rows, cols) {
	box.style.setProperty('--grid-rows', rows);
	box.style.setProperty('--grid-cols', cols);
	
	for (i =0; i<(rows * cols); i++) {
		let cell = document.createElement("div");
		box.appendChild(cell).className = "grid-box";
		let input = document.createElement("input");
		input.type ="submit";
		input.name ="context"+1;
		box.appendChild(input);
	
		
	};
};
makebox(x,x);


function addids(pos_id){
	document.querySelectorAll('.grid-box').forEach((item,i) =>{
		item.setAttribute("id",pos_id[i]);

});
		

}
addids(pos_id);		


function addlabels(pos,pos_id) {
	document.querySelectorAll('.grid-box').forEach((el,i) =>{
		console.log(el,pos[i])
		if(pos_id.includes(el.id)){	
			el.textContent = pos_id[i];
		} else {
			el.textContent = "Empty";
		}
	});


}
addlabels(pos,pos_id);






