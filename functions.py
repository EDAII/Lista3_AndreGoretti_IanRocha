import csv
import random

def nomes_reader():
    with open('nomes.csv') as csvfile:
        nomesCSV = csv.reader(csvfile, delimiter=',')
        aux = random.randint(1,100)
        auxs = str(aux)
        for x in nomesCSV:
            if auxs == x[0]:
                return x[1]

def random_city():
    with open('cidades.csv') as csvfile:
        cidadesCSV = csv.reader(csvfile, delimiter=',')
        aux = random.randint(1, 20)
        for x in cidadesCSV:
            if str(aux) == x[0]:
                return x[1]

def random_cpf():
    cpf1 = random.randint(100, 999)
    cpf2 = random.randint(100, 999)
    cpf3 = random.randint(100, 999)
    cpf4 = random.randint(0,99)

    cpf = str(cpf1) + "." + str(cpf2) + "." + str(cpf3) + "-" + str(cpf4)
    return cpf

def random_date():
    random_date.year = random.randint(1960, 2001)
    random_date.date = random.randint(1, 31)
    random_date.month = random.randint(1, 12)
    
    date = str(random_date.date) + "/" + str(random_date.month) + "/" + str(random_date.year)
    return date

def random_tel():
    tel1 = random.randint(100, 999)
    tel2 = random.randint(1000, 9999)

    tel = str((3000 + tel1)) + "-" + str(tel2)
    return tel

person = []
date = []
cpf = []
age = []
tel = []
city = []
year = []

for k in range(51):
    person.append(nomes_reader())
    date.append(random_date())
    cpf.append(random_cpf())
    year.append(date[k][-4:])
    age.append(2019 - int(year[k]))
    tel.append(random_tel())
    city.append(random_city())

#Ordering by age
def bucketSort():
    arr = []
    slot_size = 10
    
    for i in range(slot_size):
        arr.append([])

    for j in age:
        index_b = int(slot_size * j)
        arr[index_b].append(j)

    for i in range(slot_size):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(slot_size):
        for j in range(len(arr[i])):
            age[k] = arr[i][j]
            k += 1
    
def insertion_sort():
    for i in range (len(city)):
        if i > 0:
            j = i
            while j != 0 and (city[j] < city[j-1]):
                aux = city[j]
                city[j] = city[j - 1]
                city[j - 1] = aux
                #
                aux = person[j]
                person[j] = person[j - 1]
                person[j - 1] = aux
                #
                aux = age[j]
                age[j] = age[j - 1]
                age[j - 1] = aux
                #
                aux = tel[j]
                tel[j] = tel[j - 1]
                tel[j - 1] = aux
                #
                aux = date[j]
                date[j] = date[j - 1]
                date[j - 1] = aux
                #
                aux = cpf[j]
                cpf[j] = cpf[j - 1]
                cpf[j - 1] = aux
                j -= 1

        
#Ordering by Name
def shellSort():
    n = len(person)
    gap = n / 2
    while int(gap) > 0:
        for i in range(int(gap),n):
            tempAge = age[i]
            tempPerson = person[i]
            tempCity = city[i]
            tempDate = date[i]
            tempCpf = cpf[i]
            tempTel = tel[i]

            j = i
            while j >= int(gap) and person[j - int(gap)] > tempPerson:
                age[j] = age[j - int(gap)]
                person[j] = person[j - int(gap)]
                city[j] = city[j - int(gap)]
                date[j] = date[j - int(gap)]
                cpf[j] = cpf[j - int(gap)]
                tel[j] = tel[j - int(gap)]
                j -= int(gap)

            age[j] = tempAge
            person[j] = tempPerson
            city[j] = tempCity
            date[j] = tempDate
            cpf[j] = tempCpf
            tel[j] = tempTel
        gap /= 2


#Ordering by City
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

def partition(arr, low, high):
    i = low - 1
    pivo = city[high]

    for j in range(low, high):
        if city[j] <= pivo:
            i += 1
            city[i], city[j] = city[j], city[i]
            age[i], age[j] = age[j], age[i]
            person[i], person[j] = person[j], person[i]
            date[i], date[j] = date[j], date[i]
            cpf[i], cpf[j] = cpf[j], cpf[i]
            tel[i], tel[j] = tel[j], tel[i]
    
    city[i+1], city[high] = city[high], city[i+1]
    age[i+1], age[high] = age[high], age[i+1]
    person[i+1], person[high] = person[high], person[i+1]
    date[i+1], date[high] = date[high], date[i+1]
    cpf[i+1], cpf[high] = cpf[high], cpf[i+1]
    tel[i+1], tel[high] = tel[high], tel[i+1]
    
    return (i+1)