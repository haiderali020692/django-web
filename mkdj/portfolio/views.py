from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .serializers import PortSerializer, CartItemSerializer
from .models import Portfolio, CartItem, Cart

#def get_port(request):
 #   portfolios = Portfolio.objects.all()
  #  port_list = []
   # for portfolio in portfolios:
    #    port_list.append({
     #       'title': portfolio.title,
      #      'description': portfolio.description,
       #     'image': portfolio.image,
            # Add other fields as needed
        #})
    #return JsonResponse({'portfolios': port_list}) 

# Create your views here.

class PortList(generics.ListAPIView):

    queryset = Portfolio.objects.all()
    serializer_class = PortSerializer

@api_view(['POST'])
def add_to_cart(request, product_id):
    try:
        product = Portfolio.objects.get(pk=product_id)
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        return Response({'message': 'Product added to cart successfully.'})
    except Portfolio.DoesNotExist:
        return Response({'error': 'Product not found.'})

@api_view(['GET'])
def get_cart_items(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        try:
            cart = Cart.objects.get(pk=cart_id)
            cart_items = cart.items.all()
            serializer = CartItemSerializer(cart_items, many=True)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({'message': 'Cart is empty.'})
    else:
        return Response({'message': 'Cart is empty.'})



