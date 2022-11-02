import time
from curses.ascii import US
from http.client import HTTPResponse
from django.shortcuts import render,redirect, get_object_or_404
from jogos.models import Cliente, Mega,Carteira, Bicho,Rbicho,Rmega
from jogos.forms import ClienteForm , UserCreateForm ,User , MegaForm, BichoForm, CarteiraForm
from django.contrib.auth import authenticate, login, logout
from random import randint, sample 
import sched





def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('cadastrar_cli')


    else:
        form = UserCreateForm()
    return render(request,'jogos/cadastrar_cli.html', {'form': form})

    
def login_user(request):
    return render(request, 'jogos/login.html', {})


def cadastrar_cli(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            form.save()
        return redirect('login_user')
                       
    else:
        form = ClienteForm()
    return render(request, 'jogos/cadastrar_cli.html', {'form': form})



def autenticar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            id = user.id
            user = get_object_or_404(User, pk=id)
            return render(request,'jogos/home.html')
        else:
           return redirect('create_user')

    return render(request,'jogos/home.html')


def logaut_user(request):
    logout(request)
    return redirect('login_user')

    

def home(request):
    return render(request, 'jogos/home.html')



def mega_sena(request):
    user = request.user
    formS = sample(range(1,61,6),6)
    cliente = Rmega.objects.create(resultado=formS)
    cliente.save()
    result1 = Mega.objects.all()
    result2 = Rmega.objects.all()
    print(result1, result2)
    result = set(map(str,result1)) & set(str(result2))
    for x in result1:
        for y in result2:
            if (str(x) in(str (y))):
                result1 = Mega.objects.filter(nome=user.id)
    print(result)
    if result1 in result2:
        saldos = Mega.objects.filter(nome= result1.id)
        print(saldos)
    return render(request,'jogos/perfil.html',{'formS':formS, 'result': result})

  
        

def aposta(request):
    if request.method == 'POST':
        form = MegaForm(request.POST)
        if form.is_valid():
            Mega = form.save(commit=False)
            Mega.save()
        return redirect('listar')
    else:
        form = MegaForm()
        return render(request,'jogos/mega.html',{'form':form})
   
   
    
def listar(request):
    user = request.user
    print(user)
    megas = Mega.objects.filter(nome= user.id)
    print(megas)
       
    return render(request, 'jogos/mega.html', {'megas':megas,'user':user})


def carteira(request):
    user = request.user
    print(user)
    
    saldos = Carteira.objects.filter(nome= user.id)
    
    print(str(saldos))

    return render(request, 'jogos/carteira.html',{'saldos':saldos,'user':user})



def depositar(request):
    if(request.method == 'POST'):
        saldo = CarteiraForm(request.POST)
        if(saldo.is_valid()):
                saldo = saldo.save(commit=False)
                print(saldo)
                saldo.save()
                
        return redirect('carteira')
    else:
         saldo = CarteiraForm
        
         return render(request,'jogos/carteira.html',{'form':saldo})

def somar(request):
    servicos = CarteiraForm.objects.all() # aplicar filtros padroes se precisar
    soma_total = 0.00
    for servico in servicos:
       soma_total += saldo
    return render(request, 'jogos/carteira.html',{'form':soma_total})

def subtrair():
    pass

def jogo_bicho(request):
    if(request.method == 'POST'):
        form = BichoForm(request.POST)
        if(form.is_valid()):
                form = form.save(commit=False)
            
                form.save()
                
        return redirect('listarb')
    else:
         form = BichoForm
        
         return render(request,'jogos/jbicho.html',{'form':form})

        
   
    
   
                
def listarb(request):
    user = request.user
    print()
    bichos = Bicho.objects.filter(nome= user.id)
        
    return render(request, 'jogos/jbicho.html', {'bichos':bichos,})


def perfil(request):
    return  render(request,'jogos/perfil.html')

    
def listar_perf(request):
    user = request.user
    mega = Cliente.objects.all()
    return render(request, 'jogos/perfil.html', {'mega':mega,'user':user})





def Sbicho(request):
    listaf=[]
    for i in range(0,5):
        lista=[]
        c=0
        while(c<4):
            val=str(randint(0,9))
            if(val not in lista):
                lista.append(val)
            elif(val in lista):
                c-=1
            c+=1
        list2=lista[::-1]
        listaf.append(list2)
    aposta = Rbicho.objects.create(resultado1=listaf)
    aposta.save()
    
       
    return render(request,'jogos/perfil.html',{'lista':lista,'list2':list2,'listaf':listaf})
'''         formB = sample(range(0,9),4)
            formB1 = sample(range(0,9),4)
            formB2 = sample(range(0,9),4)
            formB3 = sample(range(0,9),4)
            formB4 = sample(range(0,9),4)
            lista = []
            lista(formB,formB1,formB2,formB3,formB4)
        cliente1 = Rbicho.objects.create(resultado1=lista[0,4])'''
    
    
def res_b(request,jogo_bicho,sbicho):
    pass
        

            
def listarjb(request):
    sorteio = Rbicho.objects.all()
    print(sorteio) 
    return render(request, 'jogos/perfil.html', {'bichos':sorteio,})

