from django.db import models
class Director(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=99)
    description = models.TextField(null=True, blank=True)
    duration = models.TextField(null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def reviews(self):
        review = Review.objects.filter(movie=self)
        return [{'text'} for i in review]
    @property
    def rating(self):
        rate = 0
        for i in self.reviews.all():
            rate += int(i.star)
        try:
            rat = rate/self.reviews.all().count()
            return rat
        except ZeroDivisionError:
            rat = rate/1
            return rat
CHOISE =(
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)

class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    star = models.IntegerField(default=1, choices=CHOISE, null=True)
    def __str__(self):
        return self.text