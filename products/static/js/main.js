$(document).ready(function() {
    //Obtención de la checkbox
    const colorSwitch = document.querySelector('#switch input[type="checkbox"]');
    function cambiaTema(ev){
        if(ev.target.checked){
            document.documentElement.setAttribute('tema', 'light');
            localStorage.setItem('dark-mode', 'true');     
        } else {
            document.documentElement.setAttribute('tema', 'dark');
            localStorage.setItem('dark-mode', 'false');
        }
        
    }
    colorSwitch.addEventListener('change', cambiaTema);

    //Obtencion de modo actual.
    $(document).ready(function obtenerModo(){
        if(localStorage.getItem('dark-mode') === 'true'){
            document.documentElement.setAttribute('tema', 'light');
            colorSwitch.checked = true;
        } else {
            document.documentElement.setAttribute('tema', 'dark');
            colorSwitch.checked = false;
        }
    });
    
    //Validacion de datos
    $(document).ready(function validarDatos(){
        const loginButton = $("#btn-login").on("click", function(event){
            event.preventDefault();
            var email = $("#email-user").val();
            var password = $("#password-user").val();

            if (email === ""){
                alert("El campo email no puede estar vacio.");
                return;
            };
            if (!email.includes("@")){
                alert("Su email debe contener un @")
                return;
            }
            if (password === ""){
                alert("La contraseña no puede estar vacia.");
                return;
            } else{
                if (password.length < 8){
                    alert("La contraseña debe tener minimo 8 caracteres.")
                    return;
                };
            };
            alert("¡Registro exitoso!")  
        });
    });
});