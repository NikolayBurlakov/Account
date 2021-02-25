from django.contrib import admin
from .models import Users, Diller, Mold, Plotter
# Register your models here.

models = (Users, Diller, Mold, Plotter)
for model in models:
    admin.site.register(model)