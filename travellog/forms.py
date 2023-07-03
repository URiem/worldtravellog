from django import forms
from .models import Logentry, Country, Image


class ImageForm(forms.ModelForm):
    """
    Class to enable adding images to a Logentry
    """
    class Meta:
        model = Image
        fields = ('gallery_image', 'caption', 'alttext',)


class LogentryForm(forms.ModelForm):
    """
    Class to enable authenticated users to add a logentry to the site
    """

    # Thanks for this line of code, Roman Rakic!!
    country = forms.ModelChoiceField(
        queryset=Country.objects.filter(approved=True))

    class Meta:
        model = Logentry

        fields = ('title', 'country', 'year', 'description', 'excerpt',
                  'featured_image', 'status', 'privacy', )

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter a title'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Add a descriptions of your adventure!'}
            ),
            'excerpt': forms.Textarea(
                attrs={'placeholder': 'Add a short teaser about your trip'})
        }


class CountryForm(forms.ModelForm):
    """
    class enables authenticated users to add a country to the site
    """
    class Meta:
        model = Country
        fields = ('ctry_title',)

        widgets = {
            'ctry_title': forms.TextInput(attrs={'placeholder': 'Enter country name'}),
        }
