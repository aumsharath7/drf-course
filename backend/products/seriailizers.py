from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            #'get_discount'
            'my_discount'
        ]
    
    # Initaially
    # def get_my_discount(self, obj):
    #     #print(obj.id) # 1
    #     #print(obj.title)  # Hello World
    #     try:
    #        return obj.get_discount()
    #     except:
    #         None

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):     # Both are simalar diffrent case
            return None
        if not isinstance(obj, Product):   # Both are simalar
            return None
        return obj.get_discount()

    