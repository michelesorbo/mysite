from django.shortcuts import render, get_object_or_404
#from cart.forms import CartAddProductForm
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(main_category=None)
    products_list = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)
    
    # paginator = Paginator(product_list, 3) #£ prodotti per pagina
    # page_number = request.GET.get("page")
    # #print(paginator.num_pages)
    # try:
    #     products = paginator.get_page(page_number)
    # except EmptyPage:
    #     products = paginator.page(paginator.num_pages)
    # except PageNotAnInteger:
    #     products = paginator.page(paginator.num_pages)
    
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products_list})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    related_product = Product.objects.filter(category=product.category).filter(available=True).exclude(id=product.id)
    cart_product_form = CartAddProductForm(initial={'quantity':product.quantity})
    return render(request, 'shop/product/detail.html',{'product': product, 'related_product':related_product , 'cart_product_form': cart_product_form, 'max_buy':range(1,product.quantity+1)})