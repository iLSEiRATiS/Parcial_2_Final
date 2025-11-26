from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


def _get_carrito(session):
    if "carrito" not in session:
        session["carrito"] = {}
    return session["carrito"]


def productos_view(request):
    productos = Producto.objects.all().order_by("-fecha_creacion")
    return render(request, "shop/productos.html", {"productos": productos})


@login_required
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            messages.info(request, "Producto creado.")
            return redirect("productos")
    else:
        form = ProductoForm()
    return render(request, "shop/crear_producto.html", {"form": form})


def carrito_view(request):
    carrito = _get_carrito(request.session)
    items = []
    total = Decimal("0.00")
    productos = Producto.objects.filter(id__in=carrito.keys())
    for producto in productos:
        cantidad = carrito.get(str(producto.id), 0)
        subtotal = producto.precio * cantidad
        items.append({"producto": producto, "cantidad": cantidad, "subtotal": subtotal})
        total += subtotal
    return render(request, "shop/carrito.html", {"items": items, "total": total})


def agregar_carrito(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    carrito = _get_carrito(request.session)
    carrito[str(producto.id)] = carrito.get(str(producto.id), 0) + 1
    request.session.modified = True
    return redirect("carrito")


def quitar_carrito(request, pk):
    carrito = _get_carrito(request.session)
    prod_id = str(pk)
    if prod_id in carrito:
        carrito[prod_id] -= 1
        if carrito[prod_id] <= 0:
            del carrito[prod_id]
        request.session.modified = True
    return redirect("carrito")
