from django.db import models
from django.utils import timezone

# Create your models here.

# models는 Post 클래스가 장고모델로 정해짐을 말한다.
#이 코드 덕분에 장고는 post 클래스가 데이터베이스에 저장되어야함을 인지한다.

class Post(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()

	created_date = models.DateTimeField(
		default=timezone.now)
	published_data = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_data = timezone.now()
		self.save()

	def __str__(self):
		return self.title
