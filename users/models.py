from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    USER_TYPES = (
        ("customer", "Customer"),
        ("restaurant_owner", "Restaurant Owner"),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default="customer")
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\d{10}$", message="מספר הטלפון חייב להיות מורכב מ-10 ספרות."
            )
        ],
    )
    city = models.CharField(max_length=20)
    street_name = models.CharField(max_length=50)
    house_number = models.IntegerField(null=True)

    def __str__(self):
        return self.username
