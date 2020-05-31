from django.contrib import admin
from django.urls import path
from portfoliohome import views

admin.site.site_header = "Prajapti Portfolio Admin"
admin.site.site_title = "Prajapti Portfolio Admin Portal"
admin.site.index_title = "Welcome to Prajapti Portfolio Portal"

urlpatterns = [
    path('',views.index,name="homepage" ),
    path('portfolio',views.portfolio,name="portfolio" ),
    path('about',views.about,name="about" ),
    path('contact',views.contact,name="contact" ),
    path('testimonial',views.testimonial,name="testimonial" ),
    path('privacy',views.privacy,name="privacy" ),
    path('terms',views.terms,name="terms" ),
]