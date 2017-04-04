from django.contrib import admin


from posts.models import post
from posts.models import question
# Register your models here.

class postModelAdmin(admin.ModelAdmin):
	list_display=["__unicode__","time"]
	class Meta:
		model=post


class questionModelAdmin(admin.ModelAdmin):
	list_display=["__unicode__","time"]
	list_filter=["time"]
	search_fields=["question","answer"]
	class Meta:
		model=question		

admin.site.register(post,postModelAdmin)
admin.site.register(question,questionModelAdmin)