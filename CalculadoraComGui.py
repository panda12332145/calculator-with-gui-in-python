# By create: panda12332145
# My github: https://github.com/panda12332145
from tkinter import *
from functools import partial
import math
################################################
root = Tk()
root.title("CalculadoraComGUI")
pif = False

#comands


def click_igual():
	segundo_numero = tela.get()
	tela.delete(0, END)
	pif = False
	if matematica == "soma":
		tela.insert(0, p_numero + float(segundo_numero))
	if matematica == "subtracao":
		tela.insert(0, p_numero - float(segundo_numero))
	if matematica == "multiplicacao":
		tela.insert(0, p_numero * float(segundo_numero))
	if matematica == "divisao":
		tela.insert(0, p_numero / float(segundo_numero))

def click_divi():
	primeiro_numero = tela.get()
	global p_numero
	global matematica
	matematica = "divisao"
	p_numero = float(primeiro_numero)
	tela.delete(0, END)

def click_mul():
	primeiro_numero = tela.get()
	global p_numero
	global matematica
	matematica = "multiplicacao"
	p_numero = float(primeiro_numero)
	tela.delete(0, END)

def click_sub():
	primeiro_numero = tela.get()
	global p_numero
	global matematica
	matematica = "subtracao"
	p_numero = float(primeiro_numero)
	tela.delete(0, END)

def click_soma():
	primeiro_numero = tela.get()
	global p_numero
	global matematica
	matematica = "soma"
	p_numero = float(primeiro_numero)
	tela.delete(0, END)

def deletar():
	pif = False
	tela.delete(0, END)

def click_ponto():
	tela.insert(END, ".") 

def click_pi():
	global pif
	if pif == True:
		tela.delete(0, END)
		pif = False
		tela.insert(END, math.pi)
	else:
		tela.delete(0, END)
		pif = True
		tela.insert(END, "3.14")


def click_raiz():
	primeiro_numero = tela.get()
	global p_numero
	global matematica
	matematica = "raiz"
	p_numero = float(primeiro_numero)
	tela.delete(0, END)
	if matematica == "raiz":
		tela.insert(0, p_numero ** (1/2))

def click_arredondar():
	primeiro_numero = tela.get()
	global p_numero
	global matematica
	matematica = "arredondar"
	p_numero = float(primeiro_numero)
	tela.delete(0, END)
	if matematica == "arredondar":
		tela.insert(0, round (p_numero))


def click_button(numero):
	atual = tela.get()
	tela.delete(0,END)
	tela.insert(END, str(atual)+ str(numero))

#VISOR
tela = Entry(root,bg="white")
tela.place(x=75, y=30)

#ADC_fileira
btpi = Button(root, text="π", bg="lightgray", pady=4, padx=13, bd=4, command=click_pi)
btpi.place(x=10, y=64)

btraiz = Button(root, text="x²", bg="lightgray", pady=4, padx=12, bd=4, command= click_raiz)
btraiz.place(x=60, y=64)

btarredondar = Button(root, text="≅", bg="lightgray", pady=4, padx=14, bd=4, command= click_arredondar)
btarredondar.place(x=110, y=64)


#P_fileira
bt1 = Button(root, text="1", bg="lightgray", pady=14, padx=14, bd=4, command= lambda: click_button(1))
bt1.place(x=10, y=100)

bt2 = Button(root, text="2", bg="lightgray", pady=14, padx=14, bd=4, command= lambda: click_button(2))
bt2.place(x=60, y=100)

bt3 = Button(root, text="3", bg="lightgray", pady=14, padx=14, bd=4, command= lambda: click_button(3))
bt3.place(x=110, y=100)

btmais = Button(root, text="+", bg="lightgray", pady=14, padx=14, bd=4, command= click_soma)
btmais.place(x=160, y=100)


#S_fileira
bt4 = Button(root, text="4", bg="lightgray", pady=14, padx=14, bd=4, command= lambda: click_button(4))
bt4.place(x=10, y=155)

bt5 = Button(root, text="5", bg="lightgray", pady=14, padx=14, bd=4, command= lambda: click_button(5))
bt5.place(x=60, y=155)

bt6 = Button(root, text="6", bg="lightgray", pady=14, padx=14, bd=4, command= lambda: click_button(6))
bt6.place(x=110, y=155)

btmenos = Button(root, text="- ", bg="lightgray", pady=14, padx=14, bd=4, command= click_sub)
btmenos.place(x=160, y=155)

#T_fileira
bt7 = Button(root, text="7", bg="lightgray", pady=14, padx=14, bd=4, command= lambda: click_button(7))
bt7.place(x=10, y=210)

bt8 = Button(root, text="8", bg="lightgray", pady=14, padx=14, bd=4, command= lambda: click_button(8))
bt8.place(x=60, y=210)

bt9 = Button(root, text="9", bg="lightgray", pady=14, padx=14, bd=4, command= lambda: click_button(9))
bt9.place(x=110, y=210)

bt0 = Button(root, text="0", bg="lightgray", pady=14, padx=14, bd=4, command= lambda: click_button(0))
bt0.place(x=10, y=265)

btponto = Button(root, text=".", bg="lightgray", pady=14, padx=41, bd=4, command=click_ponto)
btponto.place(x=60, y=265)

btmultiplicacao = Button(root, text="X", bg="lightgray", pady=14, padx=14, bd=4, command= click_mul)
btmultiplicacao.place(x=160, y=210)

btdivisao = Button(root, text="/ ", bg="lightgray", pady=14, padx=14, bd=4, command= click_divi)
btdivisao.place(x=160, y=265)

#botão de AC
btac = Button(root, text="AC", bg="lightgray", pady=97, padx=14, bd=4, command=deletar)
btac.place(x=210, y=100)

#botão de igual
btigual = Button(root, text="=", bg="lightgray", pady=14, padx=117, bd=4, command= click_igual)
btigual.place(x=10, y=320)


root.resizable(False, False)
root.geometry("280x380")
root.mainloop()
