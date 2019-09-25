from django.test import TestCase
from django.contrib.auth.models import User
from lsofadmin.dns.models import Domain, Record

class DomainTestCase(TestCase):
    domain1 = None
    domain2 = None
    user = None

    def setUp(self):
        user = User.objects.create_user('testluser', password='test')
        user.is_superuser = False
        user.is_staff = False
        user.save()

        self.domain1 = Domain.objects.create(name="test.com")
        self.domain2 = Domain.objects.create(name="test.org")
        self.user = user
    
    def test_can_create_records(self):
        """Able to create records"""
        record1 = Record.objects.create(name="test", 
                                        domain=self.domain1,
                                        owner=self.user)
        record2 = Record.objects.create(name="test", 
                                        domain=self.domain2,
                                        owner=self.user)
        
        self.assertIsInstance(record1, Record)
        self.assertIsInstance(record2, Record)