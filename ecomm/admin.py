from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Payment)
admin.site.register(OrderPlaced)
admin.site.register(ProductReview)

admin.site.site_header = 'SLEEKX'
admin.site.site_title = 'SLEEKX'
admin.site.site_index_title = 'Welcome to SLEEKX online clothing store'