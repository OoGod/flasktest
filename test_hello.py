import unittest

from hello import app

class HelloTestCase(unittest.TestCase):

    def setUp(self):
        app.config.update(
            TESTING=True,
            WTF_CSRF_ENABLED=False
        )
        self.client = app.test_client()

    def tearDown(self):
        pass
    
    def test_app_exist(self):
        self.assertFalse(app is None)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    def test_404_page(self):
        response = self.client.get('/nothing')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 404)
    
    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('Enter Your Name', data)

    def test_create_message(self):
        response = self.client.post('/', data=dict(
            name='aa'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('Hello, aa!', data)

    def test_form_validation(self):
        response = self.client.post('/', data=dict(
            name=' '
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('This field is required.', data)


if __name__ == '__main__':
    unittest.main()