from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile_image", null=True, blank=True)

    def __str__(self):
        return self.username


class Expense(models.Model):
    EXPENSE_TYPE_CHOICES = (
        ("Food", "Food"),
        ("Travel", "Travel"),
        ("Entertainment", "Entertainment"),
        ("Internet", "Internet"),
        ("Other", "Other"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    description = models.TextField(null=True, blank=True)
    expense_type = models.CharField(max_length=100, choices=EXPENSE_TYPE_CHOICES)
    expense_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    expense_proof = models.ImageField(
        upload_to="expense_proof",
        default="expense_proof/default.pdf",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.description} - {self.amount} - {self.expense_type}"


class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    expected_return = models.FloatField(default=0.0, null=True, blank=True)
    actual_return = models.FloatField(default=0.0, null=True, blank=True)
    profit = models.FloatField(default=0.0, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tnx_time = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)

    def __str__(self):
        return self.name


class Quotation(models.Model):

    """
    Model representing a quotation.

    Attributes:
        STATUS_CHOICES (list): Choices for the status field.
        customer (ForeignKey): Relation to the Customer model.
        date_created (DateTimeField): Date and time the quotation was created.
        status (CharField): Status of the quotation.
        total_price (DecimalField): Total price of the quotation.
    """

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("sent", "Sent"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    quotation_items = models.ManyToManyField("QuotationItem")
    total_price = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the quotation.

        Returns:
            str: String representation of the quotation.
        """

        return f"Quotation #{self.pk} - {self.customer.name} - {self.total_price} ZMW"


class QuotationItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
