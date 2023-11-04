from django.test import TestCase
from django.core.exceptions import ValidationError
# when we call the test runner it will try and run every method 
# that begin with test from this class
from .models import User

class userModelTestcase(TestCase):
    #this method is executed whenever a test is run
    def setUp(self):
        self.user = User.objects.create_user(
            '@Javed12',
            first_name = 'javed',
            last_name = 'Hussain',
            email = "javed@gmail.com",
            password = 'Pass123',
            bio = 'Hello'
        )

    def test_valid_user(self):
        self.assert_user_is_valid()
    
    def test_username_not_blank(self):
        
        self.user.username = ''
        self.assert_user_is_invalid()
    
    def test_username_is_30chars_long(self):
        self.user.username = '@' + 'x' * 29
        self.assert_user_is_valid()
    
    def test_username_isnt_over_30chars_long(self):
        self.user.username = '@' + 'x' * 30
        self.assert_user_is_invalid()

    def test_username_must_be_unique(self):
        second_user = self.create_second_user()
        self.user.username = second_user.username
        self.assert_user_is_invalid()

    def test_all_usernames_start_with_at(self):
        self.user.username = 'Javed12'
        self.assert_user_is_invalid()

    def test_all_usernames_only_alphanumericals_and_at(self):
        self.user.username = '@Javed!12'
        self.assert_user_is_invalid()
    
    def test_all_usernames_contain_at_least_3_alphanumericals(self):
        self.user.username = '@Ja'
        self.assert_user_is_invalid()
    
    def test_all_usernames_may_contain_numbers(self):
        self.user.username = '@Javed12'
        self.assert_user_is_valid()
    
    def test_all_usernames_contain_only_one_at(self):
        self.user.username = '@@Javed12'
        self.assert_user_is_invalid()

    def test_first_name_isnt_blank(self):
        self.user.first_name = ''
        self.assert_user_is_invalid()

    def test_first_name_isnt_unique(self):
        secondUser = self.create_second_user()
        self.user.first_name = secondUser.first_name
        self.assert_user_is_valid()
    
    def test_firstname_max_50chars(self):
        self.user.first_name = 'x' * 51
        self.assert_user_is_invalid()
    
    def test_firstname_can_contain_50chars(self):
        self.user.first_name = 'x' * 50
        self.assert_user_is_valid()
    
    def test_last_name_isnt_blank(self):
        self.user.last_name = ''
        self.assert_user_is_invalid()

    def test_last_name_isnt_unique(self):
        secondUser = self.create_second_user()
        self.user.last_name = secondUser.first_name
        self.assert_user_is_valid()
    
    def test_lastname_max_50chars(self):
        self.user.last_name = 'x' * 51
        self.assert_user_is_invalid()
    
    def test_lastname_can_contain_50chars(self):
        self.user.last_name = 'x' * 50
        self.assert_user_is_valid()
    
    def test_email_isnt_blank(self):
        self.user.email = ''
        self.assert_user_is_invalid()

    def test_email_must_be_unique(self):
        second_user = self.create_second_user()
        self.user.email = second_user.email
        self.assert_user_is_invalid()
    
    def test_email_must_contain_at_symbol(self):
        self.user.email = 'javed.ecamole.com'
        self.assert_user_is_invalid()

    def test_email_must_contain_username(self):
        self.user.email = '@example.com'
        self.assert_user_is_invalid()

    def test_email_must_contain_domain_name(self):
        self.user.email = 'javed@.com'
        self.assert_user_is_invalid()
    
    def test_email_must_contain_domain(self):
        self.user.email = 'javed@example'
        self.assert_user_is_invalid()
    
    def test_email_must_not_contain_more_than_1_at(self):
        self.user.email = 'javed@@example.com'
        self.assert_user_is_invalid()
    
    def test_bio_can_be_blank(self):
        self.user.bio = ''
        self.assert_user_is_valid()

    def test_bio_cannot_be_unique(self):
        second_user = self.create_second_user()
        self.user.bio = second_user.bio
        self.assert_user_is_valid()
    
    def test_bio_max_520chars(self):
        self.user.bio = 'x' * 521
        self.assert_user_is_invalid()
    
    def test_bio_can_contain_520chars(self):
        self.user.bio = 'x' * 520
        self.assert_user_is_valid()
    

    

    def create_second_user(self):
        user = User.objects.create_user(
            '@Jamal12',
            first_name = 'jamal',
            last_name = 'Hussain',
            email = "jamal@gmail.com",
            password = 'Pass123',
            bio = 'Hello im jamal'
        )
        return user

    def assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()
