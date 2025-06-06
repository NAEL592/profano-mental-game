## Test items and inventory demonstration

init python:
    ## Create some test items
    test_document1 = Item(
        "Diario Antiguo", 
        "documentos", 
        "Un diario desgastado con páginas amarillentas. Las palabras parecen moverse cuando no las miras directamente. Contiene entradas que hablan de rituales prohibidos y susurros en la oscuridad."
    )
    
    test_document2 = Item(
        "Carta Manchada de Sangre", 
        "documentos", 
        "Una carta escrita con prisa. Las manchas de sangre hacen difícil leer algunas partes, pero puedes distinguir: 'No confíes en nadie... los muros tienen ojos...'"
    )
    
    test_usable1 = Item(
        "Jeringa Misteriosa", 
        "usables", 
        "Una jeringa llena de un líquido púrpura que brilla tenuemente. La etiqueta está parcialmente borrada, pero alcanzas a leer: 'Dosis única - Efectos irreversibles'."
    )
    
    test_usable2 = Item(
        "Llave Oxidada", 
        "usables", 
        "Una llave antigua cubierta de óxido. Tiene grabados símbolos extraños que parecen cambiar cuando parpadeas. Emite un calor antinatural al tacto."
    )
    
    test_misc1 = Item(
        "Fotografía Borrosa", 
        "miscelaneos", 
        "Una fotografía en blanco y negro. Las figuras están distorsionadas, pero puedes ver lo que parece ser un ritual. En el reverso dice: 'Todos pagamos el precio'."
    )
    
    test_misc2 = Item(
        "Muñeca Rota", 
        "miscelaneos", 
        "Una muñeca de porcelana con la cara agrietada. Sus ojos parecen seguirte cuando te mueves. A veces, juras escuchar susurros proviniendo de ella."
    )
    
    test_important1 = Item(
        "Medallón de Control Mental", 
        "importantes", 
        "Un medallón que pulsa con una energía oscura. Dicen que quien lo porta puede doblar la voluntad de otros, pero a un terrible costo. Las voces en tu cabeza se vuelven más fuertes cuando lo tocas."
    )
    
    test_important2 = Item(
        "Libro de los Condenados", 
        "importantes", 
        "Un grimorio encuadernado en lo que parece ser piel humana. Sus páginas contienen conocimiento prohibido sobre la manipulación de mentes y almas. Leerlo demasiado tiempo causa pesadillas vívidas."
    )

## Test label to demonstrate inventory
label test_inventory:
    "Añadiendo items de prueba al inventario..."
    
    $ inventory.add_item(test_document1)
    $ inventory.add_item(test_document2)
    $ inventory.add_item(test_usable1)
    $ inventory.add_item(test_usable2)
    $ inventory.add_item(test_misc1)
    $ inventory.add_item(test_misc2)
    $ inventory.add_item(test_important1)
    $ inventory.add_item(test_important2)
    
    "Items añadidos. Abriendo inventario..."
    
    call show_inventory
    
    "Has cerrado el inventario."
    
    return