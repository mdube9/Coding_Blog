from django.http import HttpResponse
from django.shortcuts import render
from .models import post,question
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def  index(request):
	query_set=question.objects.all()

	paginator = Paginator(query_set,10) # Show 25 contacts per page
	page=request.GET.get('page')
	try:
		context = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		context = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		context = paginator.page(paginator.num_pages)
	return render(request,"index.html",{'data':context})


def  about(request):
	
	return render(request,"about.html",{})

def  contact(request):
	
	return render(request,"contact.html",{})



def  categories(request):
	cate=["personal",
		"web development",
		"coding"]
	data={
	"dat":cate,
	}
	
	return render(request,"categories.html",data)			


def post_detail(request,id=None):
	query_set=post.objects.all()
	context={
	"data":query_set,

	}
	return render(request,"index.html",context)



	#return HttpResponse("<h1>Helloooo</h1>")



def post_create(request):
	
	return render(request,"index.html",context)



def post_update(request):
	
	return render(request,"index.html",context)

def post_delete(request):
	
	return render(request,"index.html",context)		
	