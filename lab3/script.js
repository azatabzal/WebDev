function checkForm(el){
	var lol = document.getElementById('lol');
	var name = el.name.value;

	var label = document.createElement("label");
	label.innerHTML = name;
	label.className = "container";
	label.id = "texted";


	var check = document.createElement("input");
	check.type = "checkbox";
	check.className = "checkbox";
	check.id = "myCheck";
	check.onclick = myFunction;

	var button = document.createElement("button");
	button.className = "btned";
	button.onclick = funcDelete;

	var oImg = document.createElement("img");
	oImg.className = "imged";
	oImg.src = "delete.png";

	var span = document.createElement("span");
	span.className = "checkmark";

	lol.appendChild(label);
	label.appendChild(check);
	label.appendChild(button);
	button.appendChild(oImg);
	label.appendChild(span);
	return false;
}

function myFunction() {
	var checkBox = document.getElementsByClassName("checkbox");
	var lab = document.getElementsByClassName("container");
	for (var i = checkBox.length - 1; i >= 0; i--) {
		if (checkBox[i].checked == true){
			lab[i].style.textDecoration = "line-through";
		}
		else{
			lab[i].style.textDecoration = "none";
		}
	}
}


function funcDelete() {
	var desc = document.getElementById("texted");
	desc.remove();
}