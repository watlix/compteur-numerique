let nombre_de_persone = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    nombre_de_persone += 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    nombre_de_persone = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    nombre_de_persone += -1
})
basic.forever(function on_forever() {
    
    basic.showNumber(nombre_de_persone)
    if (nombre_de_persone < 0) {
        nombre_de_persone = 0
    }
    
    if (nombre_de_persone > 20) {
        basic.showLeds(`
            . # # # .
                        # # . # #
                        # . # . #
                        # # . # #
                        . # # # .
        `)
        nombre_de_persone = 20
    }
    
})
