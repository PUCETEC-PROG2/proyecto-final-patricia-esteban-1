from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Articulo, Cliente, Compra
from .forms import ArticuloForm, ClienteForm, CompraForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


#Login:

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    
#Vista para los clientes:

def client_list(request):
    clientes = Cliente.objects.all()
    template = loader.get_template('client_list.html')
    return HttpResponse(template.render({'clientes':clientes}, request))

    
@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('jugueteria_pechan:index')
    else:
        form = ClienteForm()
    return render(request, 'clientes_form.html', {'form':form})

@login_required
def edit_client(request, cliente_id):
    cliente = Cliente.objects.get(pk = cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('jugueteria_pechan:index')
    else:
        form = ClienteForm(instance=cliente)
    return render (request, 'clientes_form.html', {'form': form})
    
@login_required
def delete_client(request, cliente_id):
    cliente = Cliente.objects.get(pk = cliente_id)
    cliente.delete()
    return redirect("jugueteria_pechan:index")


#Vistas para los productos:

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('jugueteria_pechan:index')
    else:
        form = ArticuloForm()
    return render(request, 'product_form.html', {'form':form})



#Listar productos

def product(request, category_name, articulo_id):
    articulo = Articulo.objects.get(pk=articulo_id)
    template = loader.get_template('display_product.html')
    context = {
        'articulo': articulo,
        'category_name': category_name
    }
    return HttpResponse(template.render(context, request))


class CustomLoginView(LoginView):
    template_name = 'login.html'

def product_list(request):
    articulos = Articulo.objects.all()
    template = loader.get_template('product_list.html')
    return HttpResponse(template.render({'articulos': articulos}, request))


@login_required
def edit_product(request, category_name, articulo_id):
    articulo = Articulo.objects.get(pk= articulo_id)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('jugueteria_pechan:category_view', category_name=category_name)
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'product_form.html', {'form': form, 'category_name': category_name})

@login_required
def delete_product(request, category_name, articulo_id):
    product = Articulo.objects.get(pk=articulo_id)
    product.delete()
    return redirect('jugueteria_pechan:category_view', category_name=category_name)


#Filtrar un producto por su categoria

def category_view(request, category_name):
    articulos = Articulo.objects.filter(category=category_name)
    return render(request, 'categorias.html', {'articulos': articulos, 'category_name': category_name})

#Mostrar todas las categorias

def category_list(request):
    # Obtén una lista de todas las categorías distintas
    categories = Articulo.objects.values_list('category', flat=True).distinct()
    return render(request, 'category_list.html', {'categories': categories})


def sale_list(request):
    sales = Compra.objects.all()
    return render(request, 'sale_list.html', {'sales':sales})

                                                                            
def add_sale(request):
    if request.method == 'POST':
        form = CompraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('jugueteria_pechan:index')
    else:
        form = CompraForm()
    return render(request, 'sale_form.html', {'form':form})

@login_required
def edit_sale(request, compra_id):
    compra = Compra.objects.get(pk = compra_id)
    if request.method == 'POST':
        form = CompraForm(request.POST, request.FILES, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('jugueteria_pechan:index')
    else:
        form = CompraForm(instance=compra)
    return render (request, 'sale_form.html', {'form': form})
   
@login_required
def delete_sale(request, compra_id):
    sale = Compra.objects.get(pk = compra_id)
    sale.delete()
    return redirect("jugueteria_pechan:index")