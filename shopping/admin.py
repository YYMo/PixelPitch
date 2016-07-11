from django.contrib import admin
import shopping.models as m 
# Register your models here.

admin.site.register(m.Artist)
admin.site.register(m.Item)
admin.site.register(m.Photo)