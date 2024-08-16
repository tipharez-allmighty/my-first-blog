from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
		)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True,
		null=True
		)

	def __str__(self):
		return self.title

class PostDocument(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='document')
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.post.title} - {self.document.name}"

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    num_likes = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_comments', blank=True)

    def delete_comment(self, user):
        if user != self.author and user != self.post.author and not user.is_staff:
            raise PermissionDenied("You are not authorized to delete this comment.")
        self.delete()

    def like_comment(self, user):
        if not self.liked_by.filter(id=user.id).exists():
            self.num_likes += 1
            self.liked_by.add(user)
            self.save()

    def __str__(self):
        return self.text
