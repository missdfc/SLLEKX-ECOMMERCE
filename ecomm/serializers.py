from rest_framework import serializers
from .models import *

# category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# customer serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

# product serializer
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'

# cart serializer
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

# wishlist serializer
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

# payment serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__' # come back to this

# orders placed serializer
class OrderPlacedSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer
    payment = PaymentSerializer
    class Meta:
        model = OrderPlaced
        fields = '__all__' # comee back to this

# review serializer
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' # come back to this