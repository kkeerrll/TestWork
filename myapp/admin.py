from django.contrib import admin
from .models import Supplier, NetworkObject, Factory, RetailNetwork, IndividualEntrepreneur



class NetworkObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_supplier_link', 'city')
    list_filter = ('city',)
    actions = ['clear_debt']

    def get_supplier_link(self, obj):
        return '<a href="/admin/myapp/supplier/{}/change">{}</a>'.format(obj.supplier.id, obj.supplier.name)
    get_supplier_link.short_description = 'Поставщик'
    get_supplier_link.allow_tags = True

    def clear_debt(self, request, queryset):
        for obj in queryset:
            obj.debt_amount = 0
            obj.save()
    clear_debt.short_description = 'Очистить задолженность перед поставщиком'

admin.site.register(Factory)
admin.site.register(RetailNetwork)
admin.site.register(IndividualEntrepreneur)
admin.site.register(Supplier)
admin.site.register(NetworkObject)

