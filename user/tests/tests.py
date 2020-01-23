from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# App
from user.models import UserProfile

# Third Party
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import RequestsClient

# Create your tests here.
class TestUserAuth(APITestCase):
    def setUp(self):
        super().setUp()
        self.client = APIClient()
        self.reg_url = reverse('rest_register')
        self.user={
            'username':'peter',
            'email':'petermadasi@gmail.com',
            'password1':'Madasipeter',
            'password2':'Madasipeter'
        }
        self.user_wrong_email={
            'username':'peter',
            'email':'petermail.com',
            'password1':'Madasipeter',
            'password2':'Madasipeter'
        }
        self.user_no_username={
            'email':'petermadasi@gmail.com',
            'password1':'Madasipeter',
            'password2':'Madasipeter' 
        }
        self.user_no_password={
            'username':'peter',
            'email':'petermadasi@gmail.com',
        }
        self.user_no_missmatch_password={
            'username':'peter',
            'email':'petermadasi@gmail.com',
            'password1':'Madasipeter',
            'password2':'Madasipe' 
        }
        self.user_no_email={
            'username':'peter',
            'password1':'Madasipeter',
            'password2':'Madasipeter' 
        }
        self.user_with_short_password={
            'username':'peter',
            'email':'petermadasi@gmail.com',
            'password1':'pet',
            'password2':'pet' 
        }

    def test_user_login_ok(self):
        url = reverse('rest_login')
        self.assertEquals(url, '/rest-auth/login/')

    def test_user_register_url_ok(self):
        url = reverse('rest_register')
        self.assertEquals(url, '/rest-auth/registration/')

    def test_user_register_no_data_fails(self):
        response = self.client.post(self.reg_url, data={}, format='json')
        self.assertEqual(response.json()['username'], ['This field is required.'])

    def test_user_register_no_data_fails(self):
        response = self.client.post(self.reg_url, data={}, format='json')
        self.assertEqual(response.json()['username'], ['This field is required.'])
        


    def test_user_register_no_password_fails(self):
        data = {'email': ''}
        response = self.client.post(self.reg_url, data=data, format='json')
    
    #If all data filled and Correct ,User Created
    def test_can_register_user(self):
        response=self.client.post(self.reg_url,self.user, format='json')
        self.assertEqual(response.status_code,201)
        #Created/Registerd

    #username not entered
    def test_can_register_user_without_username(self):
        response=self.client.post(self.reg_url,self.user_no_username, format='json')
        self.assertEqual(response.status_code,400)
        #Bad Request

    #Short Password
    def test_can_register_user_with_short_password(self):
        response=self.client.post(self.reg_url,self.user_with_short_password, format='json')
        self.assertEqual(response.status_code,400)
        #Bad Request

     #password not entered
    def test_can_register_user_without_password(self):
        response=self.client.post(self.reg_url,self.user_no_password, format='json')
        self.assertEqual(response.status_code,400)
        #Bad Request    

     #password missmatch
    def test_can_register_user_missmatch_password(self):
        response=self.client.post(self.reg_url,self.user_no_missmatch_password, format='json')
        self.assertEqual(response.status_code,400)
        #Bad Request   

     #User Creating without providing Email
    def test_can_register_user_without_email(self):
        response=self.client.post(self.reg_url,self.user_no_email, format='json')
        self.assertEqual(response.status_code,201)
        #Created  
    
    #User Creating withwith wrong email
    def test_can_register_user_with_wrong_email(self):
        response=self.client.post(self.reg_url,self.user_wrong_email, format='json')
        self.assertEqual(response.status_code,400)
        #Bad Requests

    def test_user_register_with_registred_user(self):
        self.client.post(self.reg_url, self.user, format='json')
        response = self.client.post(self.reg_url,self.user, format='json')
        self.assertEqual(response.status_code,400)


class TestLogin(APITestCase):
    def setUp(self):
        super().setUp()
        self.client = APIClient()
        self.log_url = reverse('rest_login')
        self.reg_url = reverse('rest_register')
        self.user={
            'username':'peter',
            'email':'petermadasi@gmail.com',
            'password1':'Madasipeter',
            'password2':'Madasipeter'
        }

    #Login Url
    def test_user_login_ok(self):
        url = reverse('rest_login')
        self.assertEquals(url, '/rest-auth/login/')
    
    def test_login_with_valid_user(self):
        self.client.post(self.reg_url, self.user, format='json')
        user=User.objects.first()
        user.is_active=True
        user.save()
        response = self.client.post(self.log_url,data={'username':'peter','password':'Madasipeter'}, format='json')
        self.assertEqual(response.status_code,200)
    
    def test_login_with_invalid_user(self):
        self.client.post(self.reg_url, self.user, format='json')
        response = self.client.post(self.log_url,self.user, format='json')
        print(response.status_code)
         
        self.assertEqual(response.status_code,400)
    
    def test_login_without_username(self):
        self.client.post(self.reg_url, data={'username':'','password':'Madasipeter'}, format='json')
        response = self.client.post(self.log_url,self.user, format='json')
        self.assertEqual(response.status_code,400)
    
    def test_login_without_password(self):
        self.client.post(self.reg_url, data={'username':'peter','password':''}, format='json')
        response = self.client.post(self.log_url,self.user, format='json')
        self.assertEqual(response.status_code,400)

    




class UserView(APITestCase):
    def setUp(self):
        super().setUp()
        self.client = APIClient()
        self.log_url = reverse('rest_login')
        self.user_url = reverse('rest_user_details')
        self.reg_url = reverse('rest_register')
        self.user={
            'username':'peter',
            'email':'petermadasi@gmail.com',
            'password1':'Madasipeter',
            'password2':'Madasipeter'
        }

    def test_user_details_view(self):
        url = reverse('rest_user_details')
        self.assertEquals(url, '/rest-auth/user/')
        self.user=User.objects.create_user(username='peter',password='Madasipeter')
        self.token=Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)

    def test_profile_list_authentication(self):
        user=User.objects.create_user(username='peter',password='Madasipeter')
        print("/rest-auth/user/{}".format(user.id))
        response = self.client.get("/rest-auth/user/")
        self.assertEqual(response.status_code,200)

    def test_profile_list_unauthentication(self):
        self.client.force_authenticate(user=None)
        response=self.client.get(self.user_url)
        self.assertEqual(response.status_code,403)
        
    def test_profile_retrive(self):
        self.client.post(self.reg_url, self.user, format='json')
        user=User.objects.first()
        user.is_active=True
        user.save()

class TestProfile(APITestCase):
    def setUp(self):
        super().setUp()
        self.profile_list_url = reverse('user-api:profile-list')

    def test_user_profile_url_exists(self):
        self.assertEqual(self.profile_list_url, '/api/v1/user/profile/')

    def test_get_user_profile_list_ok(self):
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.json(), [])

    def test_get_user_profile_list(self):
        user = User.objects.create_user(username='peter',password='Madasipeter')
        profile = UserProfile.objects.create(user=user)

        response = self.client.get(self.profile_list_url)
        self.assertEqual(len(response.json()), 1)

        profile_detail_url = reverse('user-api:profile-detail', args=[profile.id])
        response = self.client.get(profile_detail_url)
        print(profile_detail_url, response.json())