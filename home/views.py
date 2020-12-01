from django.shortcuts import render,redirect
from .forms import*
from .models import*
from django.contrib.auth import login,logout, authenticate

# Create your views here.
def registro_vista(request):
    formulario = registro_form()
    formulario_2 = Perfil_Form()
    if request.method == 'POST':
        formulario = registro_form(request.POST)
        formulario_2 = Perfil_Form(request.POST,request.FILES)
        if formulario.is_valid() and formulario_2.is_valid():
            nombre = formulario.cleaned_data['name']
            email = formulario.cleaned_data['email']
            password = formulario.cleaned_data['password_1']
            u = User.objects.create_user(username=nombre,email=email, password=password)
            #u.is_staff = True
            #u.is_superuser = True
            u.save()
            p = formulario_2.save(commit=False)
            p.user = u
            p.save()
            #formulario_2.user = u.id
            #formulario_2.save()
            return render (request,'principal.html',locals())
    else: #METHOD GET
        return render (request,'registro.html',locals())
    return render (request,'registro.html',locals())

def principal_vista(request):  
    return render(request,'principal.html',locals())

def login_vista(request):
    usuarioo = ''
    clavee   = ''
    if request.method == 'POST':
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usuarioo = formulario.cleaned_data['user']
            clavee   = formulario.cleaned_data['password']
            usuario = authenticate(username=usuarioo,password=clavee)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('principal')
            else:
                mensaje = "Usuario o clave incorrectos, revise mayusculas"
    else: #GET 
        formulario = login_form()
        x= 'xxxxxxx'
    return render (request,'login.html',locals())

def logout_vista(request):
    logout(request)
    return redirect('/login')