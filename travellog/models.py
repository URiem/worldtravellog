from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = ((0, "Draft"), (1, "Published"))
PRIVACY = ((0, "Private"), (1, "Public"))


class Country(models.Model):
    """
    Country Model acting as categories linked to each Logentry
    """
    ctry_title = models.CharField(max_length=40, blank=False)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return self.ctry_title


class Logentry(models.Model):
    """
    Logentry Model
    Log entries are displayed in reverse order of year of travel date
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="log_entries")
    year = models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2030)], blank=False)
    description = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    privacy = models.IntegerField(choices=PRIVACY, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="countries")
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        helper method to generate slug for travel logs submitted
        by non-admin users
        """
        self.slug = slugify(self.title)
        super(Logentry, self).save(*args, **kwargs)


class Image(models.Model):
    """
    Image Model 
    Images are associated with individual Log Entries
    """
    logentry = models.ForeignKey(
        Logentry, on_delete=models.CASCADE, related_name="images")
    gallery_image = CloudinaryField('image', default='placeholder')
    caption = models.CharField(max_length=80)
    alttext = models.CharField(max_length=50)

    def __str__(self):
        return self.caption
