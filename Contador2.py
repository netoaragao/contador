from tkinter import *

count = 0

def click():
    global count
    count += 3
    label.config(text=count)

def removeclick():
    global count
    count -= 3
    label.config(text=count)

def zerar():
    global count
    count = 0
    label.config(text=count)

def plusone():
    global count
    count += 1
    label.config(text=count)

def minus():
    global count
    count -= 1
    label.config(text=count)

window = Tk()
window.config(bg='#000000')

# Label do contador
contador = Label(window, text='Contador De Grip')
contador.grid(row=0, column=0, columnspan=4)  # Posiciona o label na primeira linha, centralizado
contador.config(font=('Helvetica', 15, 'bold'))
contador.config(bg='#000000')
contador.config(fg='#ffffff')

# Botão +3
clickbutton = Button(window, text='+3')
clickbutton.config(command=click)
clickbutton.config(font=('Helvetica', 35, 'bold'))
clickbutton.config(bg='#000000')
clickbutton.config(fg='#7112e6')
clickbutton.config(activebackground='white')
clickbutton.config(activeforeground='#7112e6')
clickbutton.config(width=3, height=1)
clickbutton.grid(row=1, column=0, padx=5, pady=5)  # Posiciona na segunda linha, primeira coluna

# Botão -3
removebutton = Button(window, text='-3')
removebutton.config(command=removeclick)
removebutton.config(font=('Helvetica', 35, 'bold'))
removebutton.config(bg='#000000')
removebutton.config(fg='#7112e6')
removebutton.config(activebackground='white')
removebutton.config(activeforeground='#7112e6')
removebutton.config(width=3, height=1)
removebutton.grid(row=1, column=1, padx=5, pady=5)  # Posiciona na segunda linha, segunda coluna

# Botão +1
plusbutton = Button(window, text='+1')
plusbutton.config(command=plusone)
plusbutton.config(font=('Helvetica', 35, 'bold'))
plusbutton.config(bg='#000000')
plusbutton.config(fg='#7112e6')
plusbutton.config(activebackground='white')
plusbutton.config(activeforeground='#7112e6')
plusbutton.config(width=3, height=1)
plusbutton.grid(row=1, column=2, padx=5, pady=5)  # Posiciona na segunda linha, terceira coluna

# Botão -1
minusbutton = Button(window, text='-1')
minusbutton.config(command=minus)
minusbutton.config(font=('Helvetica', 35, 'bold'))
minusbutton.config(bg='#000000')
minusbutton.config(fg='#7112e6')
minusbutton.config(activebackground='white')
minusbutton.config(activeforeground='#7112e6')
minusbutton.config(width=3, height=1)
minusbutton.grid(row=1, column=3, padx=5, pady=5)  # Posiciona na segunda linha, quarta coluna

# Botão de zerar
clearbutton = Button(window, text='Clear')
clearbutton.config(command=zerar)
clearbutton.config(font=('Helvetica', 35, 'bold'))
clearbutton.config(bg='#000000')
clearbutton.config(fg='#7112e6')
clearbutton.config(activebackground="white")
clearbutton.config(activeforeground="#7112e6")
clearbutton.config(width=5, height=2)
clearbutton.grid(row=3, column=0, columnspan=4, pady=10)  # Posiciona na terceira linha, centralizado

# Label do contador numérico
label = Label(window, text=count)
label.grid(row=3, column=0, columnspan=4)  # Posiciona na quarta linha, centralizado
label.config(font=('Helvetica', 35, 'bold'))
label.config(bg='#000000')
label.config(fg='#7112e6')
label.grid(row=2, column=0, columnspan=4, pady=10)

window.mainloop()