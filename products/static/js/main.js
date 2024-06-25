$(document).ready(function() {
    // Creo una lista para guardar los productos que van a estar en el carrito de compra.
    let productos_carrito = [];

    if (localStorage.getItem("productos_carrito")) {
        productos_carrito = JSON.parse(localStorage.getItem("productos_carrito"));
    }

    // Función para hacer las plantillas de todos los productos que fueron agregados al carrito de compras.
    function templateProductos(lista_productos) {
        let templates = [];

        lista_productos.forEach(producto => {
            // Creo una plantilla para agregar el html al carrito de compras.
            templates.push(
                `
                <div class="container producto-carrito">
                    <div class="row">
                        <div class="col-2">
                            <img src="${producto.url_image}" alt="" class="img-carrito">
                        </div>
                        <div class="col-6 text-left">
                            <p>Nombre: ${producto.nombre}</p>
                            <p>Precio: $${producto.precio}</p>
                        </div>
                    </div>
                </div>
                `
            );
        });
        return templates;
    }

    function obtenerTotalCompra(lista_productos) {
        let total_compra = 0;

        lista_productos.forEach(producto => total_compra += producto.precio);
        return total_compra;
    }

    // Evento para obtener id del producto que escoge el usuario.
    $(".mas-vendido").submit(function(event) {
        event.preventDefault();

        // Obtengo el producto seleccionado y lo guardo en la lista de productos del carrito de compras.
        productos.forEach(producto => {
            if(producto.id == $(this).find('input[name=product_id]').val()) {
                productos_carrito.push(producto);
            }
        });

        // Almaceno los productos escogidos al localstorage.
       if(localStorage.getItem("productos_carrito")) {
            localStorage.removeItem("productos_carrito");
            
            localStorage.setItem("productos_carrito", JSON.stringify(productos_carrito));
            alert("Producto agregado al carrito!");
       } else {
            localStorage.setItem("productos_carrito", JSON.stringify(productos_carrito));
            alert("Producto agregado al carrito!");
       }

       let productos_ls = JSON.parse(localStorage.getItem("productos_carrito"));
       console.log(productos_ls);
    });

    $(document).ready(function cargarProductos() {
        if(localStorage.getItem("productos_carrito")) {
            if(document.querySelector("#body-carrito")) {
                let html_carrito = document.querySelector("#body-carrito");
                html_carrito.innerHTML = "<h1>Mi compra</h1>";

                let productos_ls = JSON.parse(localStorage.getItem("productos_carrito"));
                templateProductos(productos_ls).forEach(template_producto => {
                    html_carrito.innerHTML += template_producto;
                })
                html_carrito.innerHTML += `
                    <div class="container">
                        <div class="row justify-content-end">
                            <div class="col-4 text-left">
                                <h3 style="text-decoration: underline;">Detalle</h3>
                                <h4 class="detalle-compra">Total productos: ${productos_ls.length}</h4>
                                <h4 class="detalle-compra">Total compra: $${obtenerTotalCompra(productos_ls)}</h4>
                            </div>
                        </div>
                    </div>
                `;
            }
        }
    });

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
            alert("¡Inicio exitoso!")  
        });
    });
});