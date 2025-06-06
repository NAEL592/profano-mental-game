## Inventory System for Profano Mental
## Based on the provided sketch design

init python:
    ## Add keybinding for inventory (I key)
    config.keymap['inventory'] = ['K_i', 'alt_K_i']
    
init python:
    class Item:
        def __init__(self, name, category, description, icon=None):
            self.name = name
            self.category = category  # "documentos", "usables", "miscelaneos", "importantes"
            self.description = description
            self.icon = icon  # Path to item icon image
            
    class Inventory:
        def __init__(self):
            self.items = []
            self.current_category = "documentos"
            self.selected_item = None
            
        def add_item(self, item):
            if item not in self.items:
                self.items.append(item)
                return True
            return False
            
        def remove_item(self, item):
            if item in self.items:
                self.items.remove(item)
                return True
            return False
            
        def get_items_by_category(self, category):
            return [item for item in self.items if item.category == category]

## Initialize the inventory
default inventory = Inventory()

## Define the inventory screen
screen inventory():
    tag menu
    modal True
    
    ## Background
    add "gui/overlay/game_menu.png"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1600
        ysize 900
        
        vbox:
            ## Header - Categories
            frame:
                xfill True
                ysize 80
                background "#222222"
                
                text "CATEGORIAS DE ITEM" xalign 0.5 yalign 0.5 size 30 color "#FFFFFF"
            
            ## Category Tabs
            hbox:
                xfill True
                ysize 60
                spacing 0
                
                textbutton "DOCUMENTOS":
                    xsize 400
                    ysize 60
                    text_size 20
                    text_xalign 0.5
                    text_yalign 0.5
                    background "#333333" if inventory.current_category == "documentos" else "#555555"
                    hover_background "#444444"
                    action SetField(inventory, "current_category", "documentos")
                    
                textbutton "USABLES":
                    xsize 400
                    ysize 60
                    text_size 20
                    text_xalign 0.5
                    text_yalign 0.5
                    background "#333333" if inventory.current_category == "usables" else "#555555"
                    hover_background "#444444"
                    action SetField(inventory, "current_category", "usables")
                    
                textbutton "MISCELANEOS":
                    xsize 400
                    ysize 60
                    text_size 20
                    text_xalign 0.5
                    text_yalign 0.5
                    background "#333333" if inventory.current_category == "miscelaneos" else "#555555"
                    hover_background "#444444"
                    action SetField(inventory, "current_category", "miscelaneos")
                    
                textbutton "IMPORTANTES":
                    xsize 400
                    ysize 60
                    text_size 20
                    text_xalign 0.5
                    text_yalign 0.5
                    background "#333333" if inventory.current_category == "importantes" else "#555555"
                    hover_background "#444444"
                    action SetField(inventory, "current_category", "importantes")
            
            ## Main Content Area
            hbox:
                xfill True
                yfill True
                spacing 20
                
                ## Left Side - Item Grid
                frame:
                    xsize 900
                    yfill True
                    background "#1a1a1a"
                    padding (20, 20)
                    
                    vbox:
                        text "CUADRICULA DE ITEMS" xalign 0.5 size 25 color "#FFFFFF"
                        
                        null height 20
                        
                        ## Item Grid
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            
                            grid 6 10:  # 6 columns, 10 rows
                                spacing 10
                                
                                for item in inventory.get_items_by_category(inventory.current_category):
                                    button:
                                        xsize 120
                                        ysize 120
                                        background "#2a2a2a"
                                        hover_background "#3a3a3a"
                                        selected_background "#4a4a4a"
                                        selected (inventory.selected_item == item)
                                        action SetField(inventory, "selected_item", item)
                                        
                                        if item.icon:
                                            add item.icon xalign 0.5 yalign 0.5
                                        else:
                                            text item.name[0:3].upper() xalign 0.5 yalign 0.5 size 20
                                
                                ## Fill empty slots
                                for i in range(60 - len(inventory.get_items_by_category(inventory.current_category))):
                                    button:
                                        xsize 120
                                        ysize 120
                                        background "#1a1a1a"
                                        sensitive False
                
                ## Right Side - Item Details
                frame:
                    xsize 660
                    yfill True
                    background "#1a1a1a"
                    padding (20, 20)
                    
                    vbox:
                        spacing 20
                        
                        ## Item Name Section
                        frame:
                            xfill True
                            ysize 150
                            background "#2a2a2a"
                            padding (15, 15)
                            
                            if inventory.selected_item:
                                text inventory.selected_item.name:
                                    xalign 0.5
                                    yalign 0.5
                                    size 35
                                    color "#FFFFFF"
                                    text_align 0.5
                            else:
                                text "NOMBRE ITEM":
                                    xalign 0.5
                                    yalign 0.5
                                    size 35
                                    color "#666666"
                                    text_align 0.5
                        
                        ## Item Description Section
                        frame:
                            xfill True
                            yfill True
                            background "#2a2a2a"
                            padding (15, 15)
                            
                            viewport:
                                scrollbars "vertical"
                                mousewheel True
                                draggable True
                                
                                if inventory.selected_item:
                                    text inventory.selected_item.description:
                                        size 20
                                        color "#FFFFFF"
                                        line_spacing 5
                                else:
                                    text "DESCRIPCION DE ITEM":
                                        xalign 0.5
                                        yalign 0.5
                                        size 25
                                        color "#666666"
                                        text_align 0.5
    
    ## Close Button
    textbutton "X":
        xalign 0.95
        yalign 0.05
        xsize 50
        ysize 50
        text_size 30
        text_xalign 0.5
        text_yalign 0.5
        background "#aa0000"
        hover_background "#ff0000"
        action Return()

## Label to show inventory (can be called from anywhere)
label show_inventory:
    call screen inventory
    return

## Add the inventory keybinding
init:
    $ config.underlay.append(renpy.Keymap(inventory = ShowMenu("inventory")))