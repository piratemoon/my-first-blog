from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class  Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
	"""docstring for  Post"models.Modelf 
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	tle = models.CharField(max_length=200)
	xt = models.TextField()
	eated_date = models.DateTimeField(default=timezone.now)__init__(self, arg):
		super( Post,models.Model._
		author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
		tle = models.CharField(max_length=200)
		xt = models.TextField()
		eated_date = models.DateTimeField(default=timezone.now)_init__()
		self.arg = arg
		"""