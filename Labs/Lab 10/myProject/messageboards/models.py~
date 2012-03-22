from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Message(models.Model):
	page = models.CharField(max_length=31)
	user = models.ForeignKey(User)
	message = models.TextField()
	time = models.DateTimeField()
	
	def __str__(self):
		return self.page

	def __unicode__(self):
		return self.title
		
	def save(self):
		if(self.time == None):
			self.time = datetime.now()
		super(Message, self).save()
