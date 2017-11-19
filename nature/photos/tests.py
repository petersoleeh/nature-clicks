from django.test import TestCase
from .models import Post,tags,User

# Create your tests here.
class UserTestClass(TestCase):
    def setUp(self):
        self.peter = User(first_name = 'Peter', last_name = 'Maina', email= "petre@yahoo.com")

    #instance
    def test_instance(self):
        self.assertTrue(isinstance(self.peter,User))

    #test save method
    def test_save(self):
        self.peter.save_user()
        users = User.objects.all()
        self.assertTrue(len(users)>0)

class PostTestClass(TestCase):
    def setUp(self):
        self.peter = User(first_name = 'Peter', last_name = 'Maina', email= "petre@yahoo.com")
        self.peter.save_user()

        #new tags
        self.new_tag = tags(name = "wild")
        self.new_tag.save()

        self.post = Post(img_desc = "A bird", user =self.peter)
        self.post.save()

        #adding tags to the post
        self.post.tags.add(self.new_tag)

        #clear the data after every tests
    def tearDown(self):
        User.objects.all().delete()
        tags.objects.all().delete()
        Post.objects.all().delete()

    #instance tests
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))
