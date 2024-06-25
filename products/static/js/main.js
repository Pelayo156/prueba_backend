$(document).ready(function() {
    // Creo una "base de datos" local
    const productos = [
        {
            // Productos vista index.html
            id: 1,
            nombre: "Bravery Salmon Adult (4kg) Alimento para perro",
            precio: 26990,
            url_image: "./images/bravery_salmon_adult_perro.jpeg"
        },
        {
            id: 2,
            nombre: "Bravery Chicken Adult (2kg) Alimento para gato",
            precio: 21990,
            url_image: "./images/bravery_chicken_adult_gato.jpeg"
        },
        {
            id: 3,
            nombre: "Fit Formula arena para gato 3.2kg",
            precio: 14990,
            url_image: "./images/fit_formula_arena_gato.jpg"
        },
        {
            id: 4,
            nombre: "Fit Formula Adulto (10kg) Alimento para gato",
            precio: 24792,
            url_image: "./images/fit_formula_adult_gato.jpeg"
        },
        {
            id: 5,
            nombre: "Fit Formula Adulto (20kg) Alimento para perro",
            precio: 37592,
            url_image: "./images/fit_formula_adult_perro.jpeg"
        },
        {
            id: 6,
            nombre: "Bravery Salmon Adult (2kg) Alimento para gato",
            precio: 22990,
            url_image: "./images/bravery_salmon_adult_gato.jpeg"
        },
        {
            id: 7,
            nombre: "Bravery Pork Adult (2kg) Alimento para perro",
            precio: 28990,
            url_image: "./images/bravery_pork_adult_perro.jpeg"
        },
        {
            id: 8,
            nombre: "Premier gatos adultos de pelo largo (7.5kg)",
            precio: 46990,
            url_image: "./images/premier_gatos_pelo_largo.jpeg"
        },
        // Productos vista perro.html
        {
            id: 9,
            nombre: "Fit Formula Adult (4kg) Alimento para perro",
            precio: 26990,
            url_image: "./images/fit_formula_adult_perro.jpeg"
        },
        {
            id: 10,
            nombre: "Fit Formula Adult (2kg) Alimento para perro",
            precio: 16990,
            url_image: "./images/fit_formula_adult_perro.jpeg"
        },
        {
            id: 11,
            nombre: "Bravery Chicken Adult (4kg) Alimento para perro",
            precio: 26990,
            url_image: "./images/bravery_chicken_adult_perro.png"
        },
        {
            id: 12,
            nombre: "Desparasitante Bravecto para perros de entre 20kg-40kg",
            precio: 47990,
            url_image: "./images/desparasitante_bravecto_20kg.png"
        },
        {
            id: 13,
            nombre: "Desparasitante Bravecto para perros de entre 4.5kg-10kg",
            precio: 24990,
            url_image: "./images/desparasitante_bravecto_10kg.png"
        },
        {
            id: 14,
            nombre: "Correa Pepolli Premium talla M",
            precio: 23990,
            url_image: "./images/pepolli_correa_premium_m.png"
        },
        {
            id: 15,
            nombre: "Zeedog arnés ajustable atlanta para perro talla L",
            precio: 31990,
            url_image: "./images/zeedog_arnes_ajustable_atlanta.png"
        },
        {
            id: 16,
            nombre: "Zeedog arnés ajustable atlanta para perro talla L",
            precio: 31990,
            url_image: "./images/zeedog_arnes_ajustable_atlanta.png"
        },
        // Productos vista gato.html
        {
            id: 17,
            nombre: "Taste of the Wild Canyon River (6.6kg) alimento para gato",
            precio: 40493,
            url_image: "./images/taste-of-the-wild-gato.png"
        },
        {
            id: 18,
            nombre: "Fit Formula Adulto (10kg) Alimento para gato",
            precio: 24792,
            url_image: "./images/fit_formula_adult_gato.png"
        },
        {
            id: 19,
            nombre: "Bravery Salmon Adult (4kg) Alimento para gato",
            precio: 26990,
            url_image: "./images/bravery_salmon_adult_gato.png"
        },
        {
            id: 20,
            nombre: "Bravery Chicken Adult (4kg) Alimento para gato",
            precio: 26990,
            url_image: "./images/bravery_chicken_adult_gato.png"
        },
        {
            id: 21,
            nombre: "Olympus Cat Rascador gris & beige",
            precio: 62990,
            url_image: "./images/olympus-cat-rascador-gray-breige.png"
        },
        {
            id: 22,
            nombre: "Collar zeecat para gato con diseño de calaveras",
            precio: 5990,
            url_image: "./images/zeecat_collar_skull_gato.png"
        },
        {
            id: 23,
            nombre: "Fit Formula arena para gato 3.2kg",
            precio: 14990,
            url_image: "./images/fit_formula_arena_gato.png"
        },
        {
            id: 24,
            nombre: "Odour Buster arena para gato 6kg",
            precio: 16990,
            url_image: "./images/odour_buster_arena_gato.png"
        }
    ];

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
            alert("¡Registro exitoso!")  
        });
    });
});