from tkinter import *
from functions import *
from tkinter import ttk

# s=ttk.Style()
# s.theme_use('clam')



def abrirAdic():
   
   def inserir():
      temp = [InserirN.get(),InserirCidade.get(), InserirCPF.get(), InserirData.get(), InserirTelefone.get() ]
      contatosCSV.append(temp)
      openList()
      janelaAdic.destroy()

   janelaAdic = Toplevel()
   janelaAdic.geometry('480x550')

   InserirN = ttk.Entry(janelaAdic,width=45)
   InserirN.place(x = 100, y = 15)

   InserirCPF = ttk.Entry(janelaAdic,width=45)
   InserirCPF.place(x = 100, y = 65)

   InserirCidade = ttk.Entry(janelaAdic,width=45)
   InserirCidade.place(x = 100, y = 115)

   InserirData = ttk.Entry(janelaAdic,width=45)
   InserirData.place(x = 100, y = 165)

   InserirTelefone = ttk.Entry(janelaAdic,width=45)
   InserirTelefone.place(x = 100, y = 215)

   lblN = ttk.Label(janelaAdic, text="Nome")
   lblN.place(x = 30, y = 15)

   lblCPF = ttk.Label(janelaAdic, text="CPF")
   lblCPF.place(x = 30, y = 65)

   lblCidade = ttk.Label(janelaAdic, text="Cidade")
   lblCidade.place(x = 30, y = 115)

   lblData = ttk.Label(janelaAdic, text="Data.N")
   lblData.place(x = 30, y = 165)

   lblTelefone = ttk.Label(janelaAdic, text="Telef.")
   lblTelefone.place(x = 30, y = 215)

   lblN = ttk.Label(janelaAdic, text="Nome")
   lblN.place(x = 30, y = 15)

   btnCloseAdic = ttk.Button(janelaAdic, text="Fechar", command=janelaAdic.destroy)
   btnCloseAdic.place(x = 100, y = 300)

   btnCloseAdic = ttk.Button(janelaAdic, text="Inserir", command=inserir)
   btnCloseAdic.place(x = 300, y = 300)

def abrirDelet():

   def deletar():
      nome = InserirN.get()
      
      for line in contatosCSV:
         if line[0] == nome:
            contatosCSV.remove(line)
            
      openList()
      janelaDelet.destroy()

   janelaDelet = Toplevel()
   janelaDelet.geometry('480x200')

   InserirN = ttk.Entry(janelaDelet,width=45)
   InserirN.place(x = 100, y = 15)

   lblN = ttk.Label(janelaDelet, text="Nome")
   lblN.place(x = 30, y = 15)

   btnCloseAdic = ttk.Button(janelaDelet, text="Fechar", command=janelaDelet.destroy)
   btnCloseAdic.place(x = 100, y = 100)

   btnCloseAdic = ttk.Button(janelaDelet, text="Deletar", command=deletar)
   btnCloseAdic.place(x = 300, y = 100)

 
def abrirBusca():

   def clickedN():
      
      ContatoBusca.config(state="normal")
      ContatoBusca.delete('1.0', END)
      Nome = EntradaN.get()
      
      i = 0
      for line in contatosCSV:
         
         if line[0] == Nome:
            
            print(line[0])
            ContatoBusca.insert(INSERT, "--------------------") 
            ContatoBusca.insert(INSERT, "\n ")      
            ContatoBusca.insert(INSERT, "Nome: ")
            ContatoBusca.insert(INSERT, line[0])
            ContatoBusca.insert(INSERT, "\n ")

            ContatoBusca.insert(INSERT, "CPF: ")
            ContatoBusca.insert(INSERT, line[2])
            ContatoBusca.insert(INSERT, "\n ")

            #ContatoBusca.insert(INSERT, "idade: ")
            #ContatoBusca.insert(INSERT, age[j])
            #ContatoBusca.insert(INSERT, "\n ") 

            ContatoBusca.insert(INSERT, "Cidade: ")
            ContatoBusca.insert(INSERT, line[1])
            ContatoBusca.insert(INSERT, "\n ") 

            ContatoBusca.insert(INSERT, "Numero Telefone: ")
            ContatoBusca.insert(INSERT, line[4])
            ContatoBusca.insert(INSERT, "\n ") 

            ContatoBusca.insert(INSERT, "Idade: ")
            ContatoBusca.insert(INSERT, line[3])
            ContatoBusca.insert(INSERT, "\n")
            
     
      ContatoBusca.config(state="disabled")      

      ContatoBusca.config(state="disabled")                  

      #ContatoBusca.insert(INSERT, )

   def clickedA():

      ContatoBusca.config(state="normal")
      ContatoBusca.delete('1.0', END)
      AgeB = EntradaA.get()
      j = 0
      for line in contatosCSV:
         
         if line[3] == AgeB:
            
            
            ContatoBusca.insert(INSERT, "--------------------") 
            ContatoBusca.insert(INSERT, "\n ")      
            ContatoBusca.insert(INSERT, "Nome: ")
            ContatoBusca.insert(INSERT, line[0])
            ContatoBusca.insert(INSERT, "\n ")

            ContatoBusca.insert(INSERT, "CPF: ")
            ContatoBusca.insert(INSERT, line[2])
            ContatoBusca.insert(INSERT, "\n ")

            #ContatoBusca.insert(INSERT, "idade: ")
            #ContatoBusca.insert(INSERT, age[j])
            #ContatoBusca.insert(INSERT, "\n ") 

            ContatoBusca.insert(INSERT, "Cidade: ")
            ContatoBusca.insert(INSERT, line[1])
            ContatoBusca.insert(INSERT, "\n ") 

            ContatoBusca.insert(INSERT, "Numero Telefone: ")
            ContatoBusca.insert(INSERT, line[4])
            ContatoBusca.insert(INSERT, "\n ") 

            ContatoBusca.insert(INSERT, "Idade: ")
            ContatoBusca.insert(INSERT, line[3])
            ContatoBusca.insert(INSERT, "\n")
            
     
      ContatoBusca.config(state="disabled")      

   def clickedC():

      ContatoBusca.config(state="normal")
      ContatoBusca.delete('1.0', END)
      Cidade = EntradaC.get()
      
      for line in contatosCSV:
         
         if line[1] == Cidade:
            
            print(line[1])
            ContatoBusca.insert(INSERT, "--------------------") 
            ContatoBusca.insert(INSERT, "\n ")      
            ContatoBusca.insert(INSERT, "Nome: ")
            ContatoBusca.insert(INSERT, line[0])
            ContatoBusca.insert(INSERT, "\n ")

            ContatoBusca.insert(INSERT, "CPF: ")
            ContatoBusca.insert(INSERT, line[2])
            ContatoBusca.insert(INSERT, "\n ")

            #ContatoBusca.insert(INSERT, "idade: ")
            #ContatoBusca.insert(INSERT, age[j])
            #ContatoBusca.insert(INSERT, "\n ") 

            ContatoBusca.insert(INSERT, "Cidade: ")
            ContatoBusca.insert(INSERT, line[1])
            ContatoBusca.insert(INSERT, "\n ") 

            ContatoBusca.insert(INSERT, "Numero Telefone: ")
            ContatoBusca.insert(INSERT, line[4])
            ContatoBusca.insert(INSERT, "\n ") 

            ContatoBusca.insert(INSERT, "Idade: ")
            ContatoBusca.insert(INSERT, line[3])
            ContatoBusca.insert(INSERT, "\n")
            
     
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

   btnClose2 = ttk.Button(janelaBusca, text="Fechar", command=janelaBusca.destroy)
   btnClose2.place(x = 100, y = 500)     



def openList():

   ContatoPrin.config(state="normal")
   ContatoPrin.delete('1.0', END)

   
   j = 0
   for line in contatosCSV:

      ContatoPrin.insert(INSERT, "--------------------") 
      ContatoPrin.insert(INSERT, "\n ")      
      ContatoPrin.insert(INSERT, "Nome: ")
      ContatoPrin.insert(INSERT, line[0])
      ContatoPrin.insert(INSERT, "\n ")

      ContatoPrin.insert(INSERT, "CPF: ")
      ContatoPrin.insert(INSERT, line[2])
      ContatoPrin.insert(INSERT, "\n ")

      #ContatoPrin.insert(INSERT, "idade: ")
      #ContatoPrin.insert(INSERT, age[j])
      #ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Cidade: ")
      ContatoPrin.insert(INSERT, line[1])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Numero Telefone: ")
      ContatoPrin.insert(INSERT, line[4])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Idade: ")
      ContatoPrin.insert(INSERT, line[3])
      ContatoPrin.insert(INSERT, "\n")
      j += 1

   ContatoPrin.config(state="disabled")   


def clickedIdade():

   shellSortAge()

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

      #ContatoPrin.insert(INSERT, "idade: ")
      #ContatoPrin.insert(INSERT, age[j])
      #ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Cidade: ")
      ContatoPrin.insert(INSERT, city[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Numero Telefone: ")
      ContatoPrin.insert(INSERT, tel[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Idade: ")
      ContatoPrin.insert(INSERT, age[j])
      ContatoPrin.insert(INSERT, "\n")
      j += 1

   ContatoPrin.config(state="disabled")      

def clickedNome():

   shellSortName()

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

      # ContatoPrin.insert(INSERT, "idade: ")
      # ContatoPrin.insert(INSERT, age[j])
      # ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Cidade: ")
      ContatoPrin.insert(INSERT, city[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Numero Telefone: ")
      ContatoPrin.insert(INSERT, tel[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Idade: ")
      ContatoPrin.insert(INSERT, age[j])
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

      # ContatoPrin.insert(INSERT, "idade: ")
      # ContatoPrin.insert(INSERT, age[j])
      # ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Cidade: ")
      ContatoPrin.insert(INSERT, city[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Numero Telefone: ")
      ContatoPrin.insert(INSERT, tel[j])
      ContatoPrin.insert(INSERT, "\n ") 

      ContatoPrin.insert(INSERT, "Idade: ")
      ContatoPrin.insert(INSERT, age[j])
      ContatoPrin.insert(INSERT, "\n")
      j += 1

   ContatoPrin.config(state="disabled")            
   
   

def fechar():
   contatos_writer(contatosCSV)
   window1.destroy()

 
window1 = Tk() 

window1.title("Agenda")
 
window1.geometry('470x550')

s=ttk.Style()
s.theme_use()

ContatoPrin = Text(window1, width = 30, height = 30)
ContatoPrin.place(relx = 0.72, rely = 0.5, anchor = CENTER)
ContatoPrin.config(state="disabled")

openList()

btnAdicionar = ttk.Button(window1, text="Adicionar", command=abrirAdic)
btnAdicionar.place(x = 78, y = 50)

btnDeletar = ttk.Button(window1, text="Deletar", command=abrirDelet)
btnDeletar.place(x = 78, y = 80)

btnBusca = ttk.Button(window1, text="Buscas", command=abrirBusca)
btnBusca.place(relx = 0.25, rely = 0.3, anchor = CENTER)

btnOrdenaidade = ttk.Button(window1, text="Ordenar por Idade", command = clickedIdade)      
btnOrdenaidade.place(relx = 0.25, rely = 0.5, anchor = CENTER)

btnOrdenaNome = ttk.Button(window1, text="Ordenar por Nome", command=clickedNome)      
btnOrdenaNome.place(relx = 0.25, rely = 0.6, anchor = CENTER)

btnOrdenacidade = ttk.Button(window1, text="Ordenar por Cidade", command=clickedCidade)      
btnOrdenacidade.place(relx = 0.25, rely = 0.7, anchor = CENTER)

btnClose = ttk.Button(window1, text="Fechar", command=fechar)
btnClose.place(x = 70, y = 500)

 
window1.mainloop()