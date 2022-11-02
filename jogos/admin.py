from django.contrib import admin
from .models import Cliente , Mega, Carteira,Bicho, Rbicho,Rmega




class clienteAdmin(admin.ModelAdmin):

 
    #list_display = ['']
#pesquisa por nome
   list_display = ['saldo'] #filtrar por ano
#class megaadmin(admin.ModelAdmin):
  # pass

admin.site.register(Cliente)
admin.site.register(Mega)
admin.site.register(Carteira,clienteAdmin)
admin.site.register(Bicho)
admin.site.register(Rbicho)
admin.site.register(Rmega)


