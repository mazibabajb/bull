from django.contrib import admin

from mainapp.models import *

# Register your models here.
admin.site.site_header = "BRAVEBULL ADMINDASHBORD"
admin.site.register(category)
admin.site.register(blog_post)
admin.site.register(Email)
admin.site.register(Analyse)
admin.site.register(Sig_cat)
