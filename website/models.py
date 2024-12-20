from django.db import models


class Player(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=150)
	title = models.CharField(max_length=20, blank=True, null=True)
	FIDE_rating = models.IntegerField(default=1000)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")