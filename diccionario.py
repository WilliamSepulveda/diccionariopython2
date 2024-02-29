menu = dict({
    "Panaderia":{
        "Producto": list([
            {"nombre": "Pan de trigo", "valor": 2500},
            {"nombre": "Pan de centeno", "valor": 1500},
            {"nombre":"Pan de espelta", "valor": 4000},
            {"nombre":"Pan de maíz", "valor": 6000},
            {"nombre": "Pan germinado", "valor" : 1500}              
        ]),
       "promociones": list([                      
            {"indice": 0, "nombre": 'Descuento del 4% en la compra de 4', "unidades": 4, "descuento": 0.04},
            {"indice": 3, "nombre": 'Descuento del 17% en la compra de 3', "unidades":3, "descuento": 0.17},,
            {"indice": 0, "nombre": 'Descuento del 7% en la compra de 6', "unidades ":6, "descuento": 0.07}         
    },    
    "tortas": {
        "produto_3": list([
            {"nombre": "Pan de trigo", "valor": 2500},
            {"nombre": "torta de centeno", "valor": 1500},
            {"nombre":"torta de espelta", "valor": 4000},
            {"nombre":"torta de maíz", "valor": 6000},
            {"nombre": "torta germinado", "valor" : 1500}
        ])
    } 
})                 

print("seleccione la categoria")


listaCategoria = menu.keys()
listaCategoria = list(listaCategoria)
for i, val in enumerate(listaCategoria):

    print(f"{i}.{val}")
    opcionCategoria = int(input())
    datosCategoria = menu.get(listaCategoria[opcionCategoria])
    productosCategoria = datosCategoria.get["producto"]

print(f"seleccione el producto de la categoria{listaCategoria[opcionCategoria]}")
for i, val in enumerate(productosCategoria):
    print(f"{i},{val}")
opcionproducto = int(input())



if(len(promocionproducto) == 0):
    producto = datosCategoria.get('producto')[opcionproducto]
    nombreProducto = producto.get("nombre")
    productoValor = producto.get("valor")
    cantidad = int(input(f"usuario cuantos{producto} desea:"))
    valorAPagar = cantidad * productoValor
    print(f"usuario su producto{nombreProducto} tiene un valor de $ {productoValor} la cantidad solicitada es de {cantidad} que da un total a cancelar de {valorAPagar} ")
    dinero = int(input("ingrese la cantidad de dinero que tienes"))
    if(dinero >= valorAPagar):
        vueltos = dinero - valorAPagar
        print(f"usuario sus vueltos son {vueltos} agradezco su compra")
    else:
        print(f"usuario el monto es menor al valor total, necesitas mas dinero")
else:
    print(f"sesleccione una promocion del producto{datosCategoria.get('producto')[opcionproducto]}")
    for i, val in enumerate(promocionproducto):
        print(f"{i}.{val}")
    print(f"{len(promocionproducto)}. salir")
    opcionPromocion = int(input())
    if (opcionPromocion != 2)
     

    






