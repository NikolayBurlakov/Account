from django.contrib import admin
from .models import User, Diller, Mold, Plotter
# Register your models here.

models = (User, Diller, Mold, Plotter)
for model in models:
    admin.site.register(model)