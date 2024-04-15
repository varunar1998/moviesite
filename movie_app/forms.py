#
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import Movie, Review
#
# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
#
# class UserLoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#
# class MovieForm(forms.ModelForm):
#     class Meta:
#         model = Movie
#         fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']
#
# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['rating', 'comment']
