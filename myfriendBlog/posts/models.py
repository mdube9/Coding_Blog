from __future__ import unicode_literals

from django.db import models

# Create your models here.

class post(models.Model):
	category_post=(
		('PERSONAL','personal'),
		('CODING','coding'),
		('WEB DEVELOPMENT','web development'),
		)
	title =models.CharField(max_length=120)
	content=models.TextField()
	category=models.CharField(max_length=120,choices=category_post,default='personal')
	updates=models.DateTimeField(auto_now=True,auto_now_add=False)
	time=models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title


class question(models.Model):
	category_post=(
		('PERSONAL','personal'),
		('CODING','coding'),
		('WEB DEVELOPMENT','web development'),
		)

	coding_category=(
		('ARRAYS','Arrays'),
		('STRINGS','Strings')
		)

	status_category=(
		('Concept Done','1_Concept_Done'),
		('Code','2_Code'),
		('Done','3_Done'),
		)
	question=models.CharField(max_length=120)
	answer=models.TextField()
	time=models.DateTimeField()
	time_complexity=models.CharField(max_length=12,default='O(n^2)')
	space_complexity=models.CharField(max_length=12,default='O(1)')
	status=models.CharField(max_length=120,default='Thinking.',choices=status_category)
	category=models.CharField(max_length=120,choices=category_post,default='personal')
	Question_Category=models.CharField(max_length=120,choices=coding_category,default='Arrays')
	updates=models.DateTimeField(auto_now=True,auto_now_add=False)
	time=models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):
		return self.question

	def __unicode__(self):
		return self.question





