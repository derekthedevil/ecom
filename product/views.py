from django.shortcuts import render,redirect
from product.models import ProductTable


# Create your views here.

def add_product(request):
   data ={}
   if request.method == 'POST':
      name = request.POST.get('name')
      price = request.POST.get('price')
      description=request.POST.get('description')
      quantity=request.POST.get('quantity')
      category=request.POST.get('category')
      image = request.FILES['image']
      is_available=(request.POST.get('is_available',False)) and ('is_available' in request.POST)
      product=ProductTable.objects.create(name=name,price=price,description=description,quantity=quantity,category=category,images=image,is_available=is_available)
      product.save()      
      return redirect("/admin/product/view/",context=data)
   return render(request,'admin/product/add_product.html')


def view_products(request):
   data ={}
   all_product = ProductTable.objects.all()
   data['products'] = all_product
   return render(request,'admin/product/view_product.html',context=data)


def delete(request,int):
   product = ProductTable.objects.get(id=int)
   product.is_available = 0
   product.save()
   return redirect('/admin/product/view')


def edit_product(request,int):
   data = {}
   product = ProductTable.objects.get(id=int)
   data['product'] = product
   if request.method=='POST':
      product.name = request.POST.get('name')
      product.price = request.POST.get('price')
      product.description=request.POST.get('description')
      product.quantity=request.POST.get('quantity')
      product.category=request.POST.get('category')
      if request.FILES['image'] :
         product.images = request.FILES['image']
      product.save()
      return redirect('/admin/product/view')
   return render(request, 'admin/product/edit_product.html',context=data)