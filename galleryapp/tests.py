 
from django.test import TestCase
from django.urls import reverse, resolve
from .views import welcome, search_results, image_location

# Create your tests here.
from .models import Image, Category, Location

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.location = Location(name='kenya')
        self.location.save_location()

        self.category = Category(name='cars')
        self.category.save_category()

        self.image_test = Image(id=1, name='ford', description='my favorite car', location=self.location,
                                category=self.category)

        

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))


    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 


    def test_delete_image(self):
        self.new_image = Image(name = 'ford', description = 'my favorite car')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 0)


    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def tearDown(self):
        Image.objects.all().delete()

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='kenya')
        self.location.save_location()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

   
    def test_update_location(self):
        new_location_name = 'Paris'
        self.location.update_location(self.location.id,new_location_name)
        changed_location = Location.objects.filter(name='Paris')
        self.assertTrue(len(changed_location)>0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='cars')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
    
    def test_update_category(self):
        new_category = 'soccer'
        self.category.update_category(self.category.id, new_category)
        changed_category = Category.objects.filter(name='soccer')
        self.assertTrue(len(changed_category) > 0)   

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class IndexPageTest(TestCase):
    def test_welcome_view_status_code(self):
        url = reverse('welcome')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_index_url_resolves_welcome_view(self):
        view = resolve('/')
        self.assertEquals(view.func, welcome)
        
class SearchPageTest(TestCase):
    def test_search_view_status_code(self):
        url = reverse('search_results')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_search_url_resolves_search_view(self):
        view = resolve('/search/')
        self.assertEquals(view.func, search_results)