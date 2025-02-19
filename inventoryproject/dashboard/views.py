from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import  ProductForm,AssemblyForm,ComponentForm,OrderForm
from .models import Product,Order,Warehouse,Assembly,Component
from django.contrib.auth.models import User
from django.db.models import F
from django.contrib import messages

THRESHOLD = 100


# Create your views here.
@login_required
def warehouse(request):
    warehouses=Warehouse.objects.all()

    context = {
        'warehouses':warehouses
    }
    return render(request,'dashboard/department.html',context)


@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    customers_count = User.objects.all().count()
    products_count = products.count()
    order_count=Order.objects.all().count()

    if request.method=='POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('dashboard-index')

    else:
        form = ProductForm()

    # **Data for Pie Chart (Product Distribution)**
    product_labels = [product.name for product in products]
    assembly_count = [Assembly.objects.filter(product=product).count() for product in
                      products]  # Example: Count of assemblies per product

    # **Data for Bar Chart (Orders per Product)**
    order_labels = [order.name.name for order in orders]  # Fix: Get actual product name
    per_order_count = [order.order_quantity for order in orders]
    context = {
        'orders': orders,
        'form':form,
        'products':products,
        'customers_count': customers_count,
        'order_count': order_count,
        'products_count': products_count,
        # Graph Data
        'product_labels': product_labels,
        'assembly_count': assembly_count,
        'order_labels': order_labels,


    }
    return render(request,'dashboard/index.html',context)

@login_required
def customers(request):
    customers = User.objects.all()
    customers_count = customers.count()
    order_count = Order.objects.all().count()
    products_count = Product.objects.all().count()

    context = {
        'customers': customers,
        'customers_count': customers_count,
        'products_count': products_count,
        'order_count': order_count,
    }
    return render(request,'dashboard/customers.html',context)

@login_required
def customer_detail(request, pk):

    customers = User.objects.get(id=pk)
    customers_count = User.objects.all().count()
    order_count = Order.objects.all().count()
    products_count = Product.objects.all().count()
    context = {
        'customers': customers,
        'customers_count': customers_count,
        'products_count': products_count,
        'order_count': order_count,

    }
    return render(request, 'dashboard/customers_detail.html', context)


@login_required
def customer_page(request):
    user = request.user

    # Ensure the user has a profile
    if hasattr(user, 'profile'):
        user_department = user.profile.department  # Get the staff's department

        # Filter products by department
        products = Product.objects.filter(department=user_department)
    else:
        products = Product.objects.none()  # No products if the user has no department

    context = {
        'products': products,
    }
    return render(request, 'dashboard/customer_index.html', context)

@login_required
def add_assembly(request,pk):
    item = Product.objects.get(id=pk)


    if request.method == 'POST':
        form=AssemblyForm(request.POST)
        if form.is_valid():
            assembly = form.save(commit=False)
            assembly.product = item
            assembly.save()
            return redirect('dashboard-product-view-assembly', item.id)
    else:
        form = AssemblyForm()
    context = {
        'form':form,
        'item':item
    }
    return render(request, 'dashboard/add_assembly.html', context)

@login_required
def view_assembly(request,pk):
    item = Product.objects.get(id=pk)
    assemblies=Assembly.objects.filter(product=item)

    context = {
        'item': item,
        'assemblies':assemblies,
        'id': pk,
    }
    return render(request, 'dashboard/view_assembly.html', context)

@login_required
def add_component(request,pk):

    assembly = Assembly.objects.get(id=pk)
    item = assembly.product
    #
    if request.method == 'POST':
         form=ComponentForm(request.POST)
         if form.is_valid():
             component = form.save(commit=False)
             component.assembly = assembly
             component.save()
             return redirect('dashboard-product-assembly-view-component', assembly.id)
    else:
        form = ComponentForm()
    context = {
        'form':form,
        'assembly':assembly,
        'item':item
    }
    return render(request, 'dashboard/add_component.html', context)




@login_required
def view_component(request,pk):

    assembly = Assembly.objects.get(id=pk)
    item = assembly.product
    components = Component.objects.filter(assembly=assembly)
    #

    context = {
        'item':item,
        'assembly':assembly,
        'id':pk,
        'components':components
    }
    return render(request, 'dashboard/view_component.html', context)


@login_required
def order(request):
    orders = Order.objects.all()
    customers_count = User.objects.all().count()
    products_count = Product.objects.all().count()
    order_count = orders.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['name']  # Get product from form
            order_quantity = form.cleaned_data['order_quantity']  # Get order quantity

            assemblies = Assembly.objects.filter(product=product)

            low_stock_components = []  # To store components with low stock
            insufficient_stock = False  # Track if any component has insufficient stock

            for assembly in assemblies:
                components = Component.objects.filter(assembly=assembly)

                for component in components:
                    required_qty = component.quantity * order_quantity  # Calculate required quantity
                    new_inventory = component.inventory_qty - required_qty  # Compute new inventory

                    if new_inventory < 0:
                        messages.error(request, f'Insufficient stock: {component.description} (Available: {component.inventory_qty}, Required: {required_qty})')
                        insufficient_stock = True  # Mark order as failed

                    if new_inventory < THRESHOLD:
                        low_stock_components.append(f"{component.description} (New stock: {new_inventory})")

            if insufficient_stock:
                return redirect('dashboard-order')  # Stop process, do NOT save order

            # If stock is sufficient, save the order and update inventory
            order_instance = form.save()

            for assembly in assemblies:
                components = Component.objects.filter(assembly=assembly)
                for component in components:
                    required_qty = component.quantity * order_quantity
                    component.inventory_qty = F('inventory_qty') - required_qty
                    component.save()

            if low_stock_components:
                messages.warning(request, f"Warning: Low stock for {', '.join(low_stock_components)}")

            messages.success(request, 'Order placed and inventory updated successfully!')
            return redirect('dashboard-order')

    else:
        form = OrderForm()

    context = {
        'form': form,
        'orders': orders,
        'customers_count' : customers_count,
        'products_count' : products_count,
        'order_count'  :order_count
    }
    return render(request, 'dashboard/order.html', context)


def product(request):

    customer = User.objects.filter(groups=2)
    customers_count = User.objects.all().count()

    products=Product.objects.all()
    products_count=products.count()
    order_count = Order.objects.all().count()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context={
        'customer':customer,
        'form': form,
        'products':products,
        'customers_count':customers_count,
        'order_count': order_count,
        'products_count':products_count
    }
    return render(request,'dashboard/product.html',context)


@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    context = {
        'item': item
    }
    return render(request, 'dashboard/product_delete.html', context)


@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
        else:
            print(form.errors)  # Debug validation errors
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'dashboard/product_edit.html', context)



