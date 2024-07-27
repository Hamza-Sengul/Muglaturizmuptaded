from django.contrib import admin
from .models import Bungalov, BungalovImage, Villa, VillaImage

class BungalovImageInline(admin.TabularInline):
    model = BungalovImage
    extra = 1

class BungalovAdmin(admin.ModelAdmin):
    inlines = [BungalovImageInline]

admin.site.register(Bungalov, BungalovAdmin)


class VillaImageInline(admin.TabularInline):
    model = VillaImage
    extra = 1

@admin.register(Villa)
class VillaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    inlines = [VillaImageInline]

@admin.register(VillaImage)
class VillaImageAdmin(admin.ModelAdmin):
    list_display = ('villa', 'image')
    search_fields = ('villa__name',)
