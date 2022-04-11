from django.test import TestCase
from .models import Project,Profile,Rating

# Create your tests here.

class ImageTestClass(TestCase):
    # testing project
    def setUp(self):
        self.project= Project(name = 'James', owner ='John', link = "www.john.com",description = "john",pub_date ="2020")
    # Testing  profile
    def setUp(self):
        self.profile= Profile(username="Mzazi", description = "student of life", contact ="0188381" )
        # Testing Rating
    def setUp(self):
        self.rating= Rating(design = 'James', usability ='John', content = "Johny",ratings = "john", project = "Delani Studio", published_date ="2020")
    
    # Testing Save Method
    def test_save_method(self):
        self.project.save()
        self.profile.save()
        self.rating.save()

    def tearDown(self):        
        Project.objects.all().delete()
        Profile.objects.all().delete()
        Rating.objects.all().delete()

        