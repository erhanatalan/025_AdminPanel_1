from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_title = 'Atalan Page'
admin.site.site_header = 'Atalan Header'
admin.site.index_title = 'Atalan Index Title'


class ProductAdmin(admin.ModelAdmin):

    list_display = ['id',
        'name',
        'is_in_stock',
        'create_date',
        'update_date']

    list_editable = ['is_in_stock']
    
    list_display_links = ('id', 'name')

    list_filter = (
        'is_in_stock',
        'create_date',
        'update_date')

    search_fields = ('id', 'name')


    # siralama
    ordering = ['name']

     # Sayfa başına kayıt sayısı:
    list_per_page = 20

    # Otomatik kaıyıt oluştur:
    prepopulated_fields = {'slug' : ['name']}

    # Form liste görüntüleme
    # fields = (
    #     ('name', 'is_in_stock'),
    #     ('slug'),
    #     ('description')
    # )


    # Detaylı form liste görüntüleme
    fieldsets = (
        ('General Settings', {
            "classes": ("wide",),
            "fields": (
                ('name', 'slug'),
                "is_in_stock"
            ),
        }),
        ('Optionals Settings', {
            "classes": ("collapse",),
            "fields": ("description",),
            'description': "You can use this section for optionals settings"
        }),
    )

    def set_stock_in(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.')
    

    def set_stock_out(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f'{count} adet "Stokta Yok" olarak işaretlendi.')

    actions = ('set_stock_in', 'set_stock_out')

    set_stock_in.short_description = 'İşaretli ürünleri stoğa ekle'
    set_stock_out.short_description = 'İşaretli ürünleri stoktan çıkar'

    def added_days_ago(self, object):
        from django.utils import timezone
        different = timezone.now() - object.create_date
        return different.days

    list_display +=['added_days_ago']




admin.site.register(Product, ProductAdmin)
