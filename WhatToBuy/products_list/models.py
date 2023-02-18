from django.db.models import (
   CASCADE, CharField, ForeignKey, BooleanField, Model
    )
from django.urls import reverse
# Create your models here.
class ShoppingList(Model):
    title = CharField('Shopping list name', max_length=100)

    def __str__(self):
        return self.title


class ShoppingItem(Model):
    name = CharField("Shopping list item name", max_length=100)
    description = CharField("Description of the shopping list item", max_length=300, null=True, blank=True)
    is_completed = BooleanField(default=False)
    shopping_list = ForeignKey(ShoppingList, on_delete=CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("items-list", kwargs={"pk": self.shopping_list.pk})
    