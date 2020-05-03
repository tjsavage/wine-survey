from django.db import models

from django.utils.html import format_html


class WineItem(models.Model):
    LABEL_TYPE_CHOICES = [
        ('TR', 'Traditional'),
        ('WH', 'Whimsical'),
        ('CO', 'Colorful'),
        ('MO', 'Modern'),
        ('MI', 'Minimalist'),
    ]
    CLOSURE_TYPE_CHOICES = [
        ('CO', 'Cork'),
        ('SC', 'Screwtop'),
    ]
    WINE_TYPE_CHOICES = [
        ('R', 'Red'),
        ('W', 'White'),
        ('S', 'Sparkling'),
        ('Ro', 'Rose'),
    ]


    item_key = models.CharField(primary_key=True, max_length=120)
    name = models.CharField(max_length=240)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    bottle_image_url = models.URLField(blank=True, null=True)
    label_type = models.CharField(
        max_length=2,
        choices=LABEL_TYPE_CHOICES,
        blank=True,
        null=True
    )
    closure_type = models.CharField(
        max_length=2,
        choices=CLOSURE_TYPE_CHOICES,
        blank=True,
        null=True
    )
    country = models.CharField(max_length=120, blank=True, null=True)
    region = models.CharField(max_length=120, blank=True, null=True)
    origin = models.CharField(max_length=120, blank=True, null=True)
    wine_type = models.CharField(
        max_length=2,
        choices=WINE_TYPE_CHOICES
    )
    varietal = models.CharField(max_length=120, blank=True, null=True)
    vintage = models.IntegerField(blank=True, null=True)
    point_score = models.IntegerField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    user_rating = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    original_url = models.URLField(blank=True, null=True)
    tasting_notes = models.TextField(blank=True, null=True)
    winc_product_id = models.CharField(max_length=120, blank=True, null=True)
    winc_product_code = models.CharField(max_length=120, blank=True, null=True)

    def bottle_image_thumbnail_html(self):
        return format_html(
            '<img width="100" src="%s" />' % self.bottle_image_url
        )
    
    def __str__(self):
        return "%s" % self.name

class SurveyResponse(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    email = models.EmailField(primary_key=True)

    def __str__(self):
        return "%s %s" % (self.last_updated, self.email)

class SurveyQuestion(models.Model):
    slug = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return "%s" % self.slug

class SurveyQuestionResponse(models.Model):
    survey_response = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE)
    survey_question = models.ForeignKey(SurveyQuestion, null=True, on_delete=models.SET_NULL)
    answer = models.CharField(max_length=120)

    def __str__(self):
        return "%s %s %s" % (self.survey_response, self.survey_question, self.answer)

class SurveyABTestInstance(models.Model):
    survey_response = models.ForeignKey(SurveyResponse, null=True, on_delete=models.SET_NULL)
    item_A = models.ForeignKey(WineItem, null=True, on_delete=models.SET_NULL, related_name='+')
    item_B = models.ForeignKey(WineItem, null=True, on_delete=models.SET_NULL, related_name='+')
    winner = models.ForeignKey(WineItem, null=True, on_delete=models.SET_NULL, related_name='+')
    loser = models.ForeignKey(WineItem, null=True, on_delete=models.SET_NULL, related_name='+')

    def __str__(self):
        return "%s %s beat %s" % (self.survey_response, self.winner, self.loser)