from django.db import models
from core.models import CustumUser, StyleImage

# Create your models here.


class Image(models.Model):

    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Image -- "+str(self.post)

class Post(models.Model):

    text = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustumUser, on_delete=models.CASCADE)
    styleImage = models.ForeignKey(StyleImage, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    pass 

class ClickForStyle(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    click_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return str(self.click_date)+"--"+str(self.post)


class PostComment(models.Model):

    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustumUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    response_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.contenu
    

class UpVote(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustumUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username+"--"+str(self.post)

class DownVote(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustumUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username+"--"+str(self.post)


class LikeComment(models.Model):

    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE)
    vote_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustumUser, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username+"--"+str(self.comment)

class DislikeComment(models.Model):

    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE)
    vote_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustumUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username+"--"+str(self.comment)


