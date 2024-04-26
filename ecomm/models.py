from django.db import models
from django.contrib.auth.models import User

# our users state choice
STATE_CHOICES = (
    ('AB', 'Abia'),
    ('AD', 'Adamawa'),
    ('AK', 'Akwa Ibom'),
    ('AN', 'Anambra'),
    ('BA', 'Bauchi'),
    ('BY', 'Bayelsa'),
    ('BE', 'Benue'),
    ('BO', 'Borno'),
    ('CR', 'Cross River'),
    ('DE', 'Delta'),
    ('EB', 'Ebonyi'),
    ('EN', 'Enugu'),
    ('EK', 'Ekiti'),
    ('ED', 'Edo'),
    ('EK', 'Ekiti'),
    ('GO', 'Gombe'),
    ('IM', 'Imo'),
    ('JI', 'Jigawa'),
    ('KD', 'Kaduna'),
    ('KN', 'Kano'),
    ('KT', 'Katsina'),
    ('KE', 'Kebbi'),
    ('KO', 'Kogi'),
    ('KW', 'Kwara'),
    ('LA', 'Lagos'),
    ('NA', 'Nassarawa'),
    ('NI', 'Niger'),
    ('OG', 'Ogun'),
    ('ON', 'Ondo'),
    ('OS', 'Osun'),
    ('OY', 'Oyo'),
    ('PL', 'Plateau'),
    ('RI', 'Rivers'),
    ('SO', 'Sokoto'),
    ('TA', 'Taraba'),
    ('YO', 'Yobe'),
    ('ZA', 'Zamfara'),
)

# our users size choice
STATUS_CHOICES = (
    ('PENDING', 'Pending'),
    ('PROCESSING', 'Processing'),
    ('SHIPPED', 'Shipped'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
)

# status of orders placed by our users
SIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL','Extra Extra large'),
)

# users rating of products
RATING = (
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
)

# category of clothes i.e men,women, kids..
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

# customers details    
class Customer(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    state = models.CharField(choices=STATE_CHOICES, max_length=10)
    city = models.CharField(max_length=100)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.full_name

# our products
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    size = models.CharField(choices=SIZE_CHOICES, max_length=10)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=9999999999.99)
    product_image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.product_name
    
# users cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.price
    
# users wishlist
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
# customers payment model
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField()
    razor_order_id = models.CharField(max_length=100, blank=True, null=True)
    razor_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razor_payment_idn = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)

# orders placed by customers
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.quantity * self.product.price
    
# users review on our products
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name
    
    def get_rating(self):
        return self.rating