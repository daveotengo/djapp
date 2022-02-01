from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     print("printing obj")
#     print(obj.description)
#     # context={
#     #     'title':obj.title,
#     #     'description':obj.description
#     # }
#     context = {
#         'object':obj
#     }
#     return render(request,'product/product_detail.html',context)

def product_detail_view(request,id):
    #obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product,id=id)
    print("printing obj")
    print(obj.description)

    context = {
        'object':obj
    }
    return render(request,'product/product_detail.html',context)




def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
            #print(my_form.save())
            #my_form.save()
        else:
            print(my_form.errors)

    context = {
        'form':my_form
    }
    return render(request,'product/product_create.html',context)


def product_update_view(request,id): #rendering with initial data
    initial_data = {
        'title':"My this awsome title"
    }
    obj = Product.objects.get(id=id)
    form = ProductForm(request.POST,None,obj)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
    else:
        print(form.errors)

    context = {
        'form':form
    }
    return render(request,'product/product_update.html',context)
    





# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     #print(form)
#     if form.is_valid():
#         print("print save")
#         print(form.save())
#         form.save()
  
#     context = {
#         'form':form
#     }
#     return render(request,'product/product_create.html',context)


def product_delete_view(request,my_id):
    #obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product,id=my_id)
    print("printing obj")
    print(obj.description)
    if request.method == 'POST': 
        obj.delete()
        return redirect('../../')

    context = {
        'object':obj
    }
    return render(request,'product/product_delete.html',context)

def product_list_view(request):
    query_set = Product.objects.all()
    print("printing obj")
    print(query_set)

    for a in query_set:
        print(a.get_absolute_url)

    context = {
        'object_list':query_set
    }
    return render(request,'product/product_list.html',context)










