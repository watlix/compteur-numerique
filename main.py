nombre_de_persone = 0

def on_button_pressed_a():
    global nombre_de_persone
    nombre_de_persone += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global nombre_de_persone
    nombre_de_persone = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global nombre_de_persone
    nombre_de_persone += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global nombre_de_persone
    basic.show_number(nombre_de_persone)
    if nombre_de_persone < 0:
        nombre_de_persone = 0
    if nombre_de_persone > 20:
        basic.show_leds("""
            . # # # .
                        # # . # #
                        # . # . #
                        # # . # #
                        . # # # .
        """)
        nombre_de_persone = 20
basic.forever(on_forever)
