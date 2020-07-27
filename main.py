liste: List[number] = []
y = 0
liste = [0, 1, 2, 3, 4]
led.plot(0, 0)

def Aller_retour(x: number):
    while liste[x] < 4:
        led.unplot(x, liste[x])
        liste[x] = liste[x] + 1
        led.plot(x, liste[x])
        basic.pause(150)
    while liste[x] > 0:
        led.unplot(x, liste[x])
        liste[x] = liste[x] - 1
        led.plot(x, liste[x])
        basic.pause(150)

def on_forever():
    Aller_retour(0)
basic.forever(on_forever)

def on_forever2():
    Aller_retour(1)
basic.forever(on_forever2)

def on_forever3():
    Aller_retour(2)
basic.forever(on_forever3)

def on_forever4():
    Aller_retour(3)
basic.forever(on_forever4)

def on_forever5():
    Aller_retour(4)
basic.forever(on_forever5)
