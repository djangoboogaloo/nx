
from __future__ import unicode_literals
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class post_manager(models.Manager): #fil data draft...
	def active(self,*args,**kwargs):
		#post.objects.all()=super(post_manager,self).active()
		return super(post_manager,self).filter(draft=False).filter(publish__lte=timezone.now())



def upload_location(instance,filename):
	return "%s-%s" %(instance.id, filename)

class post(models.Model):
	user= models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=1)
	title=models.CharField(max_length=120)
	slug=models.SlugField(unique=True)
	content=models.TextField()
	draft=models.BooleanField(default=False)
	#publish=models.DateField(auto_now=False, auto_now_add=False)
	publish=models.DateField(auto_now=False, auto_now_add=False)
	image=models.ImageField(null=True,blank=True, upload_to=upload_location, )
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
	objects=post_manager()
	def __unicode__(self):
	    return self.content

	def __str__(self):
		return self.content


	def get_content_api_url(self):
		return reverse("blog-api:detail", kwargs={"slug": self.slug})


	def get_absolute_url(self):
		return reverse("blog:detail", kwargs={"slug":self.slug})

	@property
	def get_content_type(self):
		instance=self
		content_type=ContentType.objects.get_for_model(instance.__class__)
		return content_type

def create_slug(instance,new_slug=None):
	slug=slugify(instance.title)
	if new_slug is not None:
		slug=new_slug
	qs=post.objects.filter(slug=slug).order_by("-id")
	exists=qs.exists()
	if exists:
		new_slug= "%s-%s" %(slug, qs.first().id)
		return create_slug(instance,new_slug=new_slug)
	return slug


def pre_save_post_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=post)
