//despliega el input de la seccion "contactar por"
function revisaCheck(element){
    // Contar cuántos checkboxes están seleccionados.
    let count = 0;
    let checkboxes = document.querySelectorAll('.contact input[type="checkbox"]');

    // Contar los checkboxes marcados.
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            count++;
        }
    });

    // Si ya se han seleccionado 5, deshabilitar los demás checkboxes.
    if (count >= 5) {
        checkboxes.forEach(checkbox => {
            if (!checkbox.checked) {
                checkbox.disabled = true; // Deshabilitar checkboxes no seleccionados.
            }
        });
    } else {
        // Habilitar todos los checkboxes si hay menos de 5 seleccionados.
        checkboxes.forEach(checkbox => {
            checkbox.disabled = false;
        });
    }
    
    //Desplegamos los inputs de texto.
    if (element.checked) {
      document.getElementById(element.name).style.display = "block";

    } else {
       document.getElementById(element.name).style.display = "none";
    }
}

function revisaCheck_2(element) {
    let otroTextField = document.getElementById("otro-text");

    if (element.id === "tema-otro" && element.checked) {
        // Si "Otro" está marcado, mostrar el campo de texto
        otroTextField.style.display = "block";
    } else if (element.id === "tema-otro" && !element.checked) {
        // Si "Otro" no está marcado, ocultar el campo de texto
        otroTextField.style.display = "none";
    }
}


//valida nombre
const validateName = (name) => {
    if(!name) return false;
    let lengthValid = name.trim().length >= 3 && name.trim().length <= 200;
    
    return lengthValid;
}

//valida la id o url de la opcion marcada en "contactar por"
const validateId = (id) =>{
    if(!id) return true;
    let lengthValid = id.trim().length >= 4 && id.trim().length <= 50;

    return lengthValid;
}

//valida sector
const validateSector = (sector) => {
    let lengthValid = sector.trim().length <= 100; 
    return lengthValid;
}
 
//valida email
const validateEmail = (email) => {
if (!email) return false;
let lengthValid = email.length > 10;

// validamos el formato
let re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
let formatValid = re.test(email);

// devolvemos la lógica AND de las validaciones.
return lengthValid && formatValid;
};

//valida el numero telefonico
const validatePhoneNumber = (phoneNumber) => {
if (!phoneNumber) return true;
// validación de formato
let re = /^\+\d{11}$/;
let re2=/^9\d{8}$/;

// devolvemos la validación.
return re.test(phoneNumber) || re2.test(phoneNumber);
};

//valida la cantidad de documento seleccionado
const validateFiles = () => {
    const fileInputs = document.querySelectorAll(".foto-input");
    if (fileInputs.length === 0) return false;

    let count = 0;
    let typeValid = true;

    for (const input of fileInputs) {
        if (input.files.length > 0) {
            count++;
            const file = input.files[0];
            let fileFamily = file.type.split("/")[0];
            typeValid &&= fileFamily === "image" || file.type === "application/pdf";
        }
    }

    return count >= 1 && count <= 5 && typeValid;
};

//valida selector de region y comuna
const validateSelect = (select) => {
if(!select) return false;
return true
}

const validateTemas = () => {
    // Obtener todas las casillas de "temas"
    let temas = document.querySelectorAll('.tema input[type="checkbox"]');
    let atLeastOneChecked = false;
    let otherChecked = document.getElementById("tema-otro").checked;
    let otroText = document.getElementById("otro-text").value;

    // Verificar si al menos una casilla está marcada
    temas.forEach(checkbox => {
        if (checkbox.checked) {
            atLeastOneChecked = true;
        }
    });

    // Si no se ha marcado ninguna casilla
    if (!atLeastOneChecked) {
        return "Debes seleccionar al menos un tema.";
    }
    
    // Validar el campo de texto si "Otro" está marcado
    if (otherChecked) {
        if (otroText.trim().length < 3 || otroText.trim().length > 15) {
            return "El texto en 'Otro' debe tener entre 3 y 15 caracteres.";
        }
    }
    // Si todo está bien
    return null;
}

const validateContact = () => {
    //creamos una lista vacia para guardar los errores.
    let errors = [];
    
    //tomamos los id de las checkbox y de los inputs de la seccion "contactar por"
    let wCh = document.getElementById("contact-w").checked;
    let wIn = document.getElementById("whatsapp").value;

    let iCh = document.getElementById("contact-i").checked;
    let iIn = document.getElementById("instagram").value;

    let tCh = document.getElementById("contact-t").checked;
    let tIn = document.getElementById("telegram").value;

    let xCh = document.getElementById("contact-x").checked;
    let xIn = document.getElementById("x").value;

    let tiCh = document.getElementById("contact-ti").checked;
    let tiIn = document.getElementById("tiktok").value;

    let oCh = document.getElementById("contact-otro").checked;
    let oIn = document.getElementById("otro").value;

    //vemos cada caso de manera individual y lo guardamos en la lista de errores.
    if (wCh) {
        if (wIn.trim().length < 4 || wIn.trim().length > 50) {
            errors.push("El id o url en 'Whatsapp' debe tener entre 4 y 50 caracteres.");
        }
    }
    
    if (iCh) {
        if (iIn.trim().length < 4 || iIn.trim().length > 50) {
            errors.push("El id o url en 'Instagram' debe tenre entre 4 y 50 caracteres.");
        }
    }
 
    if (tCh) {
        if (tIn.trim().length < 4 || tIn.trim().length > 50) {
            errors.push("El id o url en 'Telegram' debe tener entre 4 y 50 caracteres.");
        }
    }

    if (xCh) {
        if (xIn.trim().length < 4 || xIn.trim().length > 50) {
            errors.push("El id o url en 'X' debe tener entre 4 y 50 caracteres.");
        }
    }
    if (tiCh) {
        if (tiIn.trim().length < 4 || tiIn.trim().length > 50) {
            errors.push("El id o url en 'Tiktok' debe tener entre 4 y 50 caracteres.");
        }
    }
    if (oCh) {
        if (oIn.trim().length < 4 || oIn.trim().length > 50) {
            errors.push("Por favor ingrese un medio de contacto.");
        }
    }

    return errors;
}



const validateForm = () => {
    let myForm = document.forms["myform"];
    
    // datos organizador
    let name = myForm["nombre"].value;
    let email = myForm["email"].value;
    let phoneNumber = myForm["phone"].value;
    let contactErrors = validateContact();

    // datos del lugar
    let region = myForm["select-region"].value;
    let comuna = myForm["select-comuna"].value;
    let sector = myForm["sector"].value;

    // fechas y descripción
    let inicio = myForm["inicio"].value;
    let fin = myForm["fin"].value;
    let files = validateFiles();
    let temasError = validateTemas();

    let invalidInputs = [];
    let isValid = true;

    const setInvalidInput = (inputName) => {
        invalidInputs.push(inputName);
        isValid &&= false;
    };

    // Validaciones de organizador
    if (!validateName(name)) setInvalidInput("Nombre Inválido");
    if (!validateEmail(email)) setInvalidInput("Email Inválido");
    if (!validatePhoneNumber(phoneNumber)) setInvalidInput("Número Inválido");
    if (contactErrors.length > 0) contactErrors.forEach(err => setInvalidInput(err));

    // Validación lugar
    if (!validateSelect(region)) setInvalidInput("Región Inválida");
    if (!validateSelect(comuna)) setInvalidInput("Comuna Inválida");
    if (!validateSector(sector)) setInvalidInput("Error en Sector: Máximo de 100 Caracteres");

    // Validación de fechas
    if (!inicio || isNaN(new Date(inicio).getTime())) {
        setInvalidInput("Fecha de inicio inválida");
    }

    if (fin) {
        const startDate = new Date(inicio);
        const endDate = new Date(fin);

        if (isNaN(endDate.getTime()) || endDate <= startDate) {
            setInvalidInput("La fecha de término debe ser mayor que la fecha de inicio");
        }
    }

    // Validación de archivos
    if (!files) setInvalidInput("Cantidad de Fotos Insuficientes.");

    // Validación de temas
    if (temasError) setInvalidInput(temasError);

    // Mostrar mensajes
  let validationBox = document.getElementById("val-box");
  let validationMessageElem = document.getElementById("val-msg");
  let validationListElem = document.getElementById("val-list");

  let errorBox = document.getElementById("err-box");
  let errorMessageElem = document.getElementById("err-msg");
  let errorListElem = document.getElementById("err-list");
 
  if (!isValid) {
    errorListElem.textContent = "";
    // agregar elementos inválidos al elemento val-list.
    for (input of invalidInputs) {
      let listElement = document.createElement("li");
      listElement.innerText = input;
      errorListElem.append(listElement);
    }
    // establecer val-msg
    errorMessageElem.innerText = "Los siguientes campos son inválidos:";

    // aplicar estilos de error
    errorBox.style.backgroundColor = "#ffdddd";
    errorBox.style.borderLeftColor = "#f44336";

    // hacer visible el mensaje de validación
    errorBox.hidden = false;
  } else {
    // Ocultar el formulario
    myForm.style.display = "none";

    // establecer mensaje de éxito
    errorListElem.textContent = "";
    errorBox.hidden = true;
    validationMessageElem.innerText = "¿Está seguro que desea agregar esta actividad?";
    validationListElem.textContent = "";

    // aplicar estilos de éxito
    validationBox.style.backgroundColor = "#ddffdd";
    validationBox.style.borderLeftColor = "#4CAF50";

    // Agregar botones para enviar el formulario o volver
    let submitButton = document.createElement("button");
    submitButton.innerText = "Sí, estoy seguro";
    submitButton.style.marginRight = "30px";
    submitButton.addEventListener("click", () => {
        // Oculta la caja de validación y el formulario si estaban visibles
        validationBox.hidden = true;
        myForm.style.display = "none";
    
        // Crear el mensaje de agradecimiento
        let message = document.createElement("p");
        message.innerText = "Hemos recibido su información, muchas gracias y suerte en su actividad";
        message.style.fontWeight = "bold";
        message.style.marginTop = "20px";
    
        // Crear el botón para volver a la portada
        let homeButton = document.createElement("button");
        homeButton.innerText = "Página Principal";
        homeButton.style.marginTop = "10px";
        homeButton.addEventListener("click", () => {
            window.location.href = "../index.html"; // Cambia esto por la URL de tu portada
        });
    
        // Agrega los elementos al DOM (puede ser dentro de validationBox u otro contenedor)
        validationBox.innerHTML = ""; // Limpia el contenido previo
        validationBox.appendChild(message);
        validationBox.appendChild(homeButton);
        validationBox.hidden = false;
    });

    let backButton = document.createElement("button");
    backButton.innerText = "No, no estoy seguro, quiero volver al formulario";
    backButton.addEventListener("click", () => {
      // Mostrar el formulario nuevamente
      myForm.style.display = "block";
      validationBox.hidden = true;
    });

    validationListElem.appendChild(submitButton);
    validationListElem.appendChild(backButton);

    // hacer visible el mensaje de validación
    validationBox.hidden = false;
  }
};


window.addEventListener("DOMContentLoaded", () => {
    const inicioInput = document.getElementById("inicio");
    const finInput = document.getElementById("fin");

    // Obtener la fecha actual
    const now = new Date();
    const threeHoursLater = new Date(now.getTime() + 3 * 60 * 60 * 1000);

    const toDatetimeLocal = (date) => {
        const pad = (n) => n.toString().padStart(2, "0");
        return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}T${pad(date.getHours())}:${pad(date.getMinutes())}`;
    };

    inicioInput.value = toDatetimeLocal(now);
    finInput.value = toDatetimeLocal(threeHoursLater);
});


let addFileBtn = document.getElementById("add-file");
let fileContainer = document.getElementById("file-container");

addFileBtn.addEventListener("click", () => {
    const fileInputs = document.querySelectorAll(".foto-input");
    if (fileInputs.length >= 5) {
        return;
    }

    const newInput = document.createElement("input");
    newInput.type = "file";
    newInput.name = "foto";
    newInput.className = "foto-input";
    newInput.accept = "image/*,.pdf";

    const br = document.createElement("br");

    fileContainer.insertBefore(newInput, addFileBtn);
    fileContainer.insertBefore(br, addFileBtn);
});

let submitBtn = document.getElementById("submit-btn");
submitBtn.addEventListener("click", validateForm);