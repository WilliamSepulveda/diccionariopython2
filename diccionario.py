menu = dict({
    "Panaderia":({
        "Producto":list([
            {"nombre": "Pan de trigo", "valor": 2500},
            {"nombre": "Pan de centeno", "valor": 1500},
            {"nombre":"Pan de espelta", "valor": 4000},
            {"nombre":"Pan de maíz", "valor": 6000},
            {"nombre": "Pan germinado", "valor" : 1500}              
        ]),
       "promociones": list([           
            {"indice": 0, "nombre": 'Descuento del 4% en la compra de 4', "unidades": 4, "descuento": 0.04},
            {"indice": 3, "nombre": 'Descuento del 17% en la compra de 3', "unidades":3, "descuento": 0.17},
            {"indice": 0, "nombre": 'Descuento del 7% en la compra de 6', "unidades ":6, "descuento": 0.07}])
    }),
                   
        
    "tortas":{
        "produto_3": list([
            {"nombre": "Pan de trigo", "valor": 2500},
            {"nombre": "torta de centeno", "valor": 1500},
            {"nombre":"torta de espelta", "valor": 4000},
            {"nombre":"torta de maíz", "valor": 6000},
            {"nombre": "torta germinado", "valor" : 1500}])
    }
    } 
)                 
print("seleccione la categoria")
listaCategoria = menu.keys()
listaCategoria = list(listaCategoria)
for i, val in enumerate(listaCategoria):
    print(f"{i}.{val}")
opcionCategoria = int(input())
datosCategoria = menu.get(listaCategoria[opcionCategoria])
productosCategoria = datosCategoria['Producto']

print(f"seleccione el producto de la categoria{listaCategoria[opcionCategoria]}")
for i, val in enumerate(productosCategoria):
    print(f"{i}.{val}")
opcionproducto = int(input())

# 
datosCategoria = menu.get(listaCategoria[opcionCategoria])
promocionesProducto = datosCategoria.get("promociones")
promocionProducto = list()     
for val in promocionesProducto:
        if(val.get("indice") == opcionproducto):
            promocionProducto .append(val)          

if(len(promocionProducto) == 0):
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
    print(f"seleccione una promocion del producto{datosCategoria.get('producto')[opcionproducto]}")
    for i, val in enumerate(promocionProducto):
        print(f"{i}.{val}")
    print(f"{len(promocionProducto)}. salir")
    opcionPromocion = int(input())
    if (opcionPromocion != 2):
        producto = datosCategoria.get('producto')[opcionproducto]
        nombreProducto = producto.get("nombre")
        productoValor = producto.get("valor")

        nombrepromocion = promocionProducto[opcionPromocion].get("nombre")
        descuentopromocion = promocionProducto[opcionPromocion].get("descuento")
        unidadespromocion = promocionProducto[opcionPromocion].get("unidades")



        valorAPagar = productoValor -((unidadespromocion * productoValor) * descuentopromocion)
        print(f"{nombrepromocion} del producto {datosCategoria.get['producto']}")
        dinero = int(input("ingrese la cantidad de dinero que tienes diponible para la compra"))
        if(dinero>= valorAPagar):
          vueltos = dinero - valorAPagar
          print(f"el costo a cancelar es de {valorAPagar} de la promocion {promocionProducto[opcionPromocion]}") 
          print(f"usuario su cambio es de {vueltos}, agradezco su compra que  vuelva pronto")
        else:
            print(f"usuario no tienes suficiente dinero, necesitas mas billete")
    else:
       producto = datosCategoria.get("producto")[opcionproducto]
       nombreProducto = producto.get("nombre")
       productoValor = producto.get("valor")
       cantidad = int(f"usuario cuantos{producto} desea adquirir")

        



     

    






