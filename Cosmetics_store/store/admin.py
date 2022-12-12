from django.contrib import admin
from .models import types_cosmetics,Manufacturers, cosmetics,comment_cosmetics


admin.site.register(types_cosmetics)
admin.site.register(Manufacturers)
admin.site.register(cosmetics)
admin.site.register(comment_cosmetics)
