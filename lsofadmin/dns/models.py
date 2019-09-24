from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class DomainManager(models.Model):
    def create_domain(self, name):
        domain = self.create(name=name)

        return domain

class Domain(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Domain: {0}'.format(self.name)

    objects = DomainManager()

    class Meta:
        ordering = ['name']
        managed = True

        def __unicode__(self):
            return self.name

class Record(models.Model):
    name = models.CharField(max_length=255)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=16)
    ttl = models.CharField(max_length=4)
    created_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}.{1}'.format(self.name, self.domain.name)

    class Meta:
        ordering = ['name', 'domain']
        managed = True

        def __unicode__(self):
            return self.name

