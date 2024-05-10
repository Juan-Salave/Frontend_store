from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistroForm

def login_request(request):
    msg_login=""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                login(request, user)
                return render(request, 'venta/nosotros.html')
        msg_login ="Usuario o Contraseña incorrectos"
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form, 'msg_login':msg_login})

def register(request):

    msg_registro = ''
    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = UserRegistroForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"venta/nosotros.html" ,  {"mensaje":"Usuario Creado :)"})
        msg_registro = 'Error en los datos ingresados'

    else:
        #form = UserCreationForm()       
        form = UserRegistroForm()     

    return render(request,"users/registro.html" ,  {"form":form})    