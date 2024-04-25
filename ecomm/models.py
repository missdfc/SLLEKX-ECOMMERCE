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
SIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL','Extra Extra large'),
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
    mobile = models.IntegerField
    zipcode = models.

    def __str__(self):
        return self.full_name

# our products
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey
    size = models.CharField(choices=SIZE_CHOICES, max_length=10)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=9999999999.99)
    product_image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.product_name
    
# users cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey
    quantity = models.

    def __str__(self):
        return self.
    
# users wishlist
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey

    def __str__(self):
        return self.
    
# customers payment model
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.
    razor_order_id = models.
    razor_payment_status = models
    razor_payment_idn = models.
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.

# orders placed by customers
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.
    date_ordered = models.
    status = models.
    payment = models.

    def __str__(self):
        return self.
    
# users review on our products
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.ImageField()
    date = models.

    def __str__(self):
        return self.