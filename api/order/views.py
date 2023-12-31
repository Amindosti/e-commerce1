from rest_framework import viewsets
from django.http import JsonResponse
from .serializers import OrderSerializer
from .models import Order
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt


def validate_user_session(id, token):
    UserModel = get_user_model
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    
    except UserModel.DoesNotExist:
        return False
    

@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Please re-login!', 'code': '1'})
    if request.method == 'POST':
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']

        total_product = len(products.split(',')[:-1])

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=user_id)


        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'User Does not exist!'})
        
        order = Order(user=user, product_names=products, total_product=total_product,
                      transaction_id=transaction_id, total_amount=amount)
        order.save()
        return JsonResponse({'seccess': True, 'error': False, 'massage': 'Order placed seccessfully'})
    


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('product_names')
    serializer_class = OrderSerializer
    