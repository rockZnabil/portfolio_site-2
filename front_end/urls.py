from django.urls import path
from front_end.views import (PublicationPageView, ProfPageView,
                             LoginPageView, PhdPageView, MScPageView,
                             BScPageView, ContactPageView, HomepagePageView,
                             Nano_assemblyPageView, NanofabricationPageView,
                             Nano_bioPageView, Nano_energyPageView, IoDPageView)

urlpatterns = [
    path('', HomepagePageView.as_view()),
    path('index', HomepagePageView.as_view()),
    path('publications', PublicationPageView.as_view()),
    path('professor', ProfPageView.as_view()),
    path('phd', PhdPageView.as_view()),
    path('ms', MScPageView.as_view()),
    path('bs', BScPageView.as_view()),
    path('contact', ContactPageView.as_view()),
    path('nano_assembly', Nano_assemblyPageView.as_view()),
    path('nanofabrication', NanofabricationPageView.as_view()),
    path('nano_bio', Nano_bioPageView.as_view()),
    path('nano_energy', Nano_energyPageView.as_view()),
    path('login', LoginPageView.as_view()),
    path('iod', IoDPageView.as_view()),
]
