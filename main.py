from tkinter import *
from functions import *
from tkinter import ttk

# s=ttk.Style()
# s.theme_use('clam')


 
def abrirBusca():

   def clickedN():
      
      ContatoBusca.config(state="normal")
      ContatoBusca.delete('1.0', END)
      Nome = EntradaN.get()
      
      i = 0
      while(i <= 50):
            
            if person[i] == Nome:
               
               ContatoBusca.insert(INSERT, "--------------------")
               ContatoBusca.insert(INSERT, "\n ")
               ContatoBusca.insert(INSERT, "Nome: ")
               ContatoBusca.insert(INSERT, person[i])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "CPF: ")
               ContatoBusca.insert(INSERT, cpf[i])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "idade: ")
               ContatoBusca.insert(INSERT, age[i])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Cidade: ")
               ContatoBusca.insert(INSERT, city[i])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Numero Telefone: ")
               ContatoBusca.insert(INSERT, tel[i])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Nascimento: ")
               ContatoBusca.insert(INSERT, date[i])
               ContatoBusca.insert(INSERT, "\n")
            i += 1       

      ContatoBusca.config(state="disabled")                  

      #ContatoBusca.insert(INSERT, )

   def clickedA():

      ContatoBusca.config(state="normal")
      ContatoBusca.delete('1.0', END)
      AgeB = int(EntradaA.get())
      j = 0
      while(j <= 50):
            if age[j] == AgeB:
               ContatoBusca.insert(INSERT, "--------------------")
               ContatoBusca.insert(INSERT, "\n ")
               ContatoBusca.insert(INSERT, "Nome: ")
               ContatoBusca.insert(INSERT, person[j])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "CPF: ")
               ContatoBusca.insert(INSERT, cpf[j])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "idade: ")
               ContatoBusca.insert(INSERT, age[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Cidade: ")
               ContatoBusca.insert(INSERT, city[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Numero Telefone: ")
               ContatoBusca.insert(INSERT, tel[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Nascimento: ")
               ContatoBusca.insert(INSERT, date[j])
               ContatoBusca.insert(INSERT, "\n")
            j += 1

      ContatoBusca.config(state="disabled")      

   def clickedC():

      ContatoBusca.config(state="normal")
      ContatoBusca.delete('1.0', END)
      Cidade = EntradaC.get()
      j = 0
      while(j <= 50):
            
            if Cidade == city[j]:
               ContatoBusca.insert(INSERT, "--------------------")
               ContatoBusca.insert(INSERT, "\n ")
               ContatoBusca.insert(INSERT, "Nome: ")
               ContatoBusca.insert(INSERT, person[j])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "CPF: ")
               ContatoBusca.insert(INSERT, cpf[j])
               ContatoBusca.insert(INSERT, "\n ")

               ContatoBusca.insert(INSERT, "idade: ")
               ContatoBusca.insert(INSERT, age[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Cidade: ")
               ContatoBusca.insert(INSERT, city[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Numero Telefone: ")
               ContatoBusca.insert(INSERT, tel[j])
               ContatoBusca.insert(INSERT, "\n ") 

               ContatoBusca.insert(INSERT, "Nascimento: ")
               ContatoBusca.insert(INSERT, date[j])
               ContatoBusca.insert(INSERT, "\n")
            j += 1   
     
      ContatoBusca.config(state="disabled")

   janelaBusca = Toplevel()
   janelaBusca.geometry('480x550')

   lblN = ttk.Label(janelaBusca, text="Nome")
   lblN.place(x = 1, y = 15)

   lblA = ttk.Label(janelaBusca, text="Idade")
   lblA.place(x = 1, y = 40)

   lblC = ttk.Label(janelaBusca, text="Cidade")
   lblC.place(x = 1, y = 70)
   
   EntradaN = ttk.Entry(janelaBusca,width=10)
   EntradaN.place(x = 50, y = 15)

   EntradaA = ttk.Entry(janelaBusca,width=10)
   EntradaA.place(x = 50, y = 40)

   EntradaC = ttk.Entry(janelaBusca,width=10)
   EntradaC.place(x = 50, y = 70)   

   ContatoBusca = Text(janelaBusca, width = 30, height = 30)
   ContatoBusca.place(x = 230, y = 0)
   ContatoBusca.config(state="disabled")

   btnNome = ttk.Button(janelaBusca, text="Buscar", command=clickedN)
   btnAge = ttk.Button(janelaBusca, text="Buscar", command=clickedA)
   
   btnCity = ttk.Button(janelaBusca, text="Buscar", command=clickedC)

   btnAge.place(x = 140, y = 40)
   btnNome.place(x = 140, y = 10)
   
   btnCity.place(x = 140, y = 70)

   btnClose = ttk.Button(janelaBusca, text="Fechar", command=janelaBusca.destroy)
   btnClose.place(x = 100, y = 500)     



def openList():

   ContatoPrin.delete('1.0', END)
   ContatoPrin.config(state="normal")

   
   j = 0
   while(j <= 50):

      ContatoPrin.insert(INSERT, "--------------------") 
      ContatoPrin.insert(INSERT, "\n ")      
      ContatoPrin.insert(INSERT, "Nome: ")
      ContatoPrin.insert(INSERT, person[j])
      ContatoPrin.insert(INSERT, "\n ")

      ContatoPrin.insert(INSERT, "CPF: ")
      ContatoPrin.insert(INSERT, cpf[j])
      ContatoPrin.insert(INSERT, "\n ")

      ContatoPrin.insert(INSERT, "idade: ")
      ContatoPrin.insert(INSERT, age[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Cidade: ")
      ContatoPrin.insert(INSERT, city[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Numero Telefone: ")
      ContatoPrin.insert(INSERT, tel[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Nascimento: ")
      ContatoPrin.insert(INSERT, date[j])
      ContatoPrin.insert(INSERT, "\n")
      j += 1

   ContatoPrin.config(state="disabled")   


def clickedIdade():

   shellSort()

   ContatoPrin.config(state="normal")
   ContatoPrin.delete('1.0', END)

   
   j = 0
   while(j <= 50):

      ContatoPrin.insert(INSERT, "--------------------") 
      ContatoPrin.insert(INSERT, "\n ")      
      ContatoPrin.insert(INSERT, "Nome: ")
      ContatoPrin.insert(INSERT, person[j])
      ContatoPrin.insert(INSERT, "\n ")

      ContatoPrin.insert(INSERT, "CPF: ")
      ContatoPrin.insert(INSERT, cpf[j])
      ContatoPrin.insert(INSERT, "\n ")

      ContatoPrin.insert(INSERT, "idade: ")
      ContatoPrin.insert(INSERT, age[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Cidade: ")
      ContatoPrin.insert(INSERT, city[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Numero Telefone: ")
      ContatoPrin.insert(INSERT, tel[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Nascimento: ")
      ContatoPrin.insert(INSERT, date[j])
      ContatoPrin.insert(INSERT, "\n")
      j += 1

   ContatoPrin.config(state="disabled")      

def clickedNome():

   shellSort()

   ContatoPrin.config(state="normal")
   ContatoPrin.delete('1.0', END)

   
   j = 0
   while(j <= 50):

      ContatoPrin.insert(INSERT, "--------------------") 
      ContatoPrin.insert(INSERT, "\n ")      
      ContatoPrin.insert(INSERT, "Nome: ")
      ContatoPrin.insert(INSERT, person[j])
      ContatoPrin.insert(INSERT, "\n ")

      ContatoPrin.insert(INSERT, "CPF: ")
      ContatoPrin.insert(INSERT, cpf[j])
      ContatoPrin.insert(INSERT, "\n ")

      ContatoPrin.insert(INSERT, "idade: ")
      ContatoPrin.insert(INSERT, age[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Cidade: ")
      ContatoPrin.insert(INSERT, city[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Numero Telefone: ")
      ContatoPrin.insert(INSERT, tel[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Nascimento: ")
      ContatoPrin.insert(INSERT, date[j])
      ContatoPrin.insert(INSERT, "\n")
      j += 1

   ContatoPrin.config(state="disabled")  

def clickedCidade():

   n = len(city)
   quickSort(city, 0, n-1)

   ContatoPrin.config(state="normal")
   ContatoPrin.delete('1.0', END)

   
   j = 0
   while(j <= 50):

      ContatoPrin.insert(INSERT, "--------------------") 
      ContatoPrin.insert(INSERT, "\n ")      
      ContatoPrin.insert(INSERT, "Nome: ")
      ContatoPrin.insert(INSERT, person[j])
      ContatoPrin.insert(INSERT, "\n ")

      ContatoPrin.insert(INSERT, "CPF: ")
      ContatoPrin.insert(INSERT, cpf[j])
      ContatoPrin.insert(INSERT, "\n ")

      ContatoPrin.insert(INSERT, "idade: ")
      ContatoPrin.insert(INSERT, age[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Cidade: ")
      ContatoPrin.insert(INSERT, city[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Numero Telefone: ")
      ContatoPrin.insert(INSERT, tel[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Nascimento: ")
      ContatoPrin.insert(INSERT, date[j])
      ContatoPrin.insert(INSERT, "\n")
      j += 1

   ContatoPrin.config(state="disabled")            
   
   

   

window1 = Tk() 

window1.title("Agenda")
 
window1.geometry('470x550')

s=ttk.Style()
s.theme_use()

ContatoPrin = Text(window1, width = 30, height = 30)
ContatoPrin.place(relx = 0.72, rely = 0.5, anchor = CENTER)
ContatoPrin.config(state="disabled")

openList()


btnBusca = ttk.Button(window1, text="Buscas", command=abrirBusca)
btnBusca.place(relx = 0.25, rely = 0.3, anchor = CENTER)

btnOrdenaidade = ttk.Button(window1, text="Ordenar por Idade", command = clickedIdade)      
btnOrdenaidade.place(relx = 0.25, rely = 0.5, anchor = CENTER)

btnOrdenaNome = ttk.Button(window1, text="Ordenar por Nome", command=clickedNome)      
btnOrdenaNome.place(relx = 0.25, rely = 0.6, anchor = CENTER)

btnOrdenacidade = ttk.Button(window1, text="Ordenar por Cidade", command=clickedCidade)      
btnOrdenacidade.place(relx = 0.25, rely = 0.7, anchor = CENTER)

 
window1.mainloop()