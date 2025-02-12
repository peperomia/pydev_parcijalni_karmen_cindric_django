from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    vat_id = models.CharField(max_length=20, unique=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Overrides the save method to include any custom logic.
        Django automatically handles insert/update based on whether the instance has a primary key.
        """
        super().save(*args, **kwargs)

    @classmethod
    def from_tuple(cls, data):
        """
        Creates a Customer instance from a tuple.
        Args:
            data (tuple): A tuple containing (id, name, vat_id, street, city, country).
        Returns:
            ProdCustomeruct: An instance of Customer.
        """
        return cls(id=data[0], name=data[1], vat_id=data[2], street=data[3], city = data[4], country = data[5])

    @classmethod
    def get_all(cls):
        """
        Retrieves all Customer instances from the database.
        Returns:
            QuerySet: A QuerySet containing all Customer objects.
        """
        return cls.objects.all()
