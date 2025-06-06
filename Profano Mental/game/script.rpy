# Profano Mental - Main Script

# Declara los personajes
define narrator = Character(None, kind=nvl)
define unknown = Character("???", color="#ff0000")

# El juego comienza aquí
label start:
    
    scene black
    with fade
    
    narrator "La oscuridad te envuelve..."
    narrator "No recuerdas cómo llegaste aquí."
    narrator "Solo sabes que algo no está bien."
    
    nvl clear
    
    unknown "Bienvenido al experimento."
    
    menu:
        "¿Qué está pasando?":
            unknown "Pronto lo descubrirás... si sobrevives."
            
        "¿Quién eres?":
            unknown "Eso no importa ahora. Lo que importa es lo que encontrarás."
    
    "De repente, sientes algo en tu bolsillo..."
    
    # Añadir algunos items iniciales
    $ inventory.add_item(test_document1)
    $ inventory.add_item(test_usable1)
    
    "Has encontrado un {b}Diario Antiguo{/b} y una {b}Jeringa Misteriosa{/b}."
    
    menu:
        "Revisar inventario":
            call show_inventory
            
        "Continuar explorando":
            pass
    
    "El juego continúa..."
    
    # Menu de prueba para el inventario
    menu test_menu:
        "Opciones de prueba:"
        
        "Abrir inventario":
            call show_inventory
            jump test_menu
            
        "Añadir más items":
            call test_inventory
            jump test_menu
            
        "Continuar":
            pass
    
    "Fin de la demo."
    
    return
