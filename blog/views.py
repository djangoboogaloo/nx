
from django.contrib.contenttypes.models import ContentType

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .form import post_form
from .models import post
from django.contrib import messages

from django.utils import timezone


today= timezone.now()
def post_list(request):
	queryset_list=post.objects.active()
	qs=post.objects.active().order_by("-timestamp")
	if  request.user.is_staff or  request.user.is_superuser:
		qs=post.objects.all().order_by("-timestamp")
	search = request.GET.get('q')
	if search:
		qs=qs.filter(
			Q(title__icontains=search) |
			Q(content__icontains=search)
			).distinct()
	paginator = Paginator(qs,10) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)


	context= {
	"title":"BLOG",
	"post_list":contacts, # dung paginato query vaof db
	"today":today,
	}
	return render(request,"blog/post_list.html",context)













def post_detail(request, slug=None):
	today=timezone.now()
	instance=get_object_or_404(post,slug=slug)
	# if instance.publish > today or instance.draft:
	# 	if not request.user.is_staff or not request.user.is_superuser:
	# 		raise Http404
	context={
	'instance':instance,
	}

	return render(request,"blog/post_detail.html",context)

def post_create(request):
	if not request.user.is_authenticated():
		raise Http404
	form=post_form(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request,"congo")

		return HttpResponseRedirect(instance.get_absolute_url())


	context= {
	"form":form,

	}
	return render(request,"blog/post_create.html",context)





def post_edit(request, slug=None):
	if not request.user.is_authenticated():
		raise Http404
	instance=get_object_or_404(post,slug=slug)
	form=post_form(request.POST or None,request.FILES or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"congo")
		return HttpResponseRedirect(instance.get_absolute_url())
	context= {
	"instance":instance,
	"title":"edit",
	"form":form,
	}
	return render(request,"blog/post_edit.html",context)
def post_delete(request, slug=None):
	if not request.user.is_authenticated():
		raise Http404
	instance=get_object_or_404(post,slug=slug)
	instance.delete()
	messages.success(request,"congo")

	return redirect("blog:list")
