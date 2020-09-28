from django.contrib import admin
from myapp.models import *
# Register your models here.
admin.site.register(Constituency)
admin.site.register(Candidate)
admin.site.register(Voter)