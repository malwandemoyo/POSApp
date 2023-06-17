from .models import Product
from inventory_man.models import Category

from rest_framework import viewsets

from .serializers import ProductSerializer, CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class SevenHundredDrillion:
#     selected_category = ""

# class POSApp(View):
#     def get(self, request):
#         products = Product.objects.all()
#         categories = Category.objects.all()
                
#         return render(
#                     request, 
#                     'pos-app.html',
#                     {
#                         "products": products,
#                         "categories": categories,  
#                         "common": SevenHundredDrillion.selected_category,
#                     }
#                 )
        
# class CategoryView(View):
#     template = "categories.html"
    
#     def get(self, request):
#         categories = Category.objects.all()
#         return render(
#             request,
#             self.template,
#             {
#                 "categories": categories,
#                 "common": SevenHundredDrillion.selected_category,               
#             }
#         )

#     def post(self, request):
        
#         common = request.POST.get('common')
#         print(common)
#         request.session['common'] = common
        
#         return redirect('pos-app')