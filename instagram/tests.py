from django.test import TestCase
# Create your tests here.
from .models import Profile,Comments,Image
from django.contrib.auth.models import User
import datetime as dt


class ProfileTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):
        self.user = User.objects.create(id =1,username='zily')
        self.profile = Profile(firstname = ' Zilfa',lastname = 'cyamani,profile_photo = 'BOOK.jpeg',bio = 'Cute',date = '20.1.2121', user = self.user)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
    
    def test_save_method(self):
        '''
        test image by save
        '''
        self.profile.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=1) 
   
    def test_delete_method(self):
        '''
        test of delete image
        '''
        self.profile.save_profile()
        profile=Profile.delete_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=0) 

class CommentTestClass(TestCase):
    def setUp(self):
        self.comment=Comments.objects.create(comment='yes')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.comment.save_comments()
        comment=Comments.objects.all()
        self.assertTrue(len(comm)>0) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
        self.comment.save_comments()
        self.comment.delete_comments()
        comment=Comments.objects.all()
        self.assertTrue(len(comm)>0)


class ImageTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):
        self.image = Image(image ='BOOK.jpeg', image_name='oops', image_caption='just an image',date='11.6.2020')
    
    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()


        # Testing Instance
        def test_instance(self):
            self.assertTrue(isinstance(self.image,Image))


        # Testing the save method
        def test_save_method(self):
            self.image=Image(name='cat',description='beautiful',user=self.user1,likes="1",post="image")
            self.image.save_image()
            images = Image.objects.all()
            self.assertTrue(len(images) >= 1)

    def test_delete_method(self):
            self.image=Image(name='cat',description='beautiful',user=self.user1,likes="1",post="image")
            self.image.save_image()
            images = self.image.delete_image
            deleted = Image.objects.all()
            self.assertTrue(len(deleted) <= 0)