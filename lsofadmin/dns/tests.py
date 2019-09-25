from django.test import TestCase
from django.contrib.auth.models import User
from lsofadmin.dns.models import Domain, Record

class DomainTestCase(TestCase):
    domain = None
    # def setUp(self):

    def test_can_create_domains(self):
        """Able to create domains"""
        self.domain = Domain.objects.create(name="test.com")
        self.assertIsInstance(self.domain, Domain)
    
    def test_can_delete_domains(self):
        """Able to delete domains"""
        Domain.objects.delete(self.domain)
        self.assertNotIsInstance(self.domain, Domain)

class RecordTestCase(TestCase):
    domain = None
    owner = None
    admin = None
    staff = None
    anonymous = None

    record = None

    def setUp(self):
        owner = User.objects.create_user('testuser', password='test')
        owner.is_superuser = False
        owner.is_staff = False
        owner.save()

        anonymous = User.objects.create_user('testanonuser', password='test')
        anonymous.is_superuser = False
        anonymous.is_staff = False
        anonymous.save()

        admin = User.objects.create_user('testadmin', password='test')
        admin.is_superuser = True
        admin.is_staff = False
        admin.save()

        staff = User.objects.create_user('teststaff', password='test')
        staff.is_superuser = False
        staff.is_staff = True
        staff.save()
        
        self.owner = owner
        self.admin = admin
        self.staff = staff
        self.anonymous = anonymous

        self.domain = Domain.objects.create(name="test.com")

    def test_owner_can_create_records(self):
        """Owner able to create records"""
        self.record = Record.objects.create(name="test", 
                                        domain=self.domain,
                                        owner=self.owner)
        
        self.assertIsInstance(self.record, Record)
    
    def test_owner_can_delete_records(self):
        """Owner able to delete records"""
        Record.objects.delete(self.record)
        self.assertNotIsInstance(self.record, Record)

    def test_staff_can_create_records(self):
        """Staff able to create records"""
        self.record = Record.objects.create(name="test", 
                                        domain=self.domain,
                                        owner=self.staff)
        
        self.assertIsInstance(self.record, Record)
    
    def test_staff_can_delete_records(self):
        """Staff able to delete records"""
        Record.objects.delete(self.record)
        self.assertNotIsInstance(self.record, Record)

    def test_admin_can_create_records(self):
        """Admin able to create records"""
        self.record = Record.objects.create(name="test", 
                                        domain=self.domain,
                                        owner=self.admin)
        
        self.assertIsInstance(self.record, Record)
    
    def test_admin_can_delete_records(self):
        """Admin able to delete records"""
        Record.objects.delete(self.record)
        self.assertNotIsInstance(self.record, Record)
