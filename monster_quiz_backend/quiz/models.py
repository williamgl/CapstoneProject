from django.db import models


# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=255)  # quiz title
    slug = models.SlugField()  # address name for url creation
    description = models.TextField(blank=True, null=True)  # description
    completed = models.BooleanField(default=False)  # completed
    date_added = models.DateTimeField(auto_now_add=True)  # created_at

    class Meta:
        ordering = ('-title', )

    def __str__(self):
        # return the quiz title
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # question name
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)  # description
    date_added = models.DateTimeField(auto_now_add=True)  # created at
    score = models.IntegerField()

    class Meta:
        ordering = ('-date_added', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.quiz.slug}/{self.slug}/'
