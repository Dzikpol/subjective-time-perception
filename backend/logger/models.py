import hashlib
from django.db import models
from django.utils.translation import ugettext_lazy as _


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_sha1(text):
    return hashlib.sha1(bytes(text, encoding='utf-8')).hexdigest()


class HTTPRequest(models.Model):
    METHOD_GET = 'GET'
    METHOD_POST = 'POST'
    METHOD_PATCH = 'PATCH'
    METHOD_PUT = 'PUT'
    METHOD_HEAD = 'HEAD'

    METHOD_CHOICES = [
        (METHOD_GET, _('GET')),
        (METHOD_POST, _('POST')),
        (METHOD_PATCH, _('PATCH')),
        (METHOD_PUT, _('PUT')),
        (METHOD_HEAD, _('HEAD')),
    ]

    DATA_STATUS_PRODUCTION = 'production'
    DATA_STATUS_TEST = 'test'
    DATA_STATUS_CHOICES = [
        (DATA_STATUS_PRODUCTION, _('Production')),
        (DATA_STATUS_TEST, _('Test')),
    ]

    # TODO: merge logger with APIvX...

    data_status = models.CharField(verbose_name=_('Data status'), max_length=30, choices=DATA_STATUS_CHOICES, null=True, blank=True, default=DATA_STATUS_PRODUCTION)
    added = models.DateTimeField(verbose_name=_('Datetime'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Datetime'), auto_now=True, db_index=True)
    ip = models.GenericIPAddressField(verbose_name=_('IP'), default='127.0.0.1')
    method = models.CharField(verbose_name=_('Method'), max_length=10, choices=METHOD_CHOICES, default=METHOD_POST)
    api_version = models.PositiveSmallIntegerField(verbose_name=_('API version'), default=3)
    data = models.TextField(verbose_name=_('Data'), null=True, blank=True)
    sha1 = models.CharField(verbose_name=_('SHA1'), max_length=40, db_index=True, unique=True, null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        self.sha1 = get_sha1(self.data)
        super().save(*args, **kwargs)

    @staticmethod
    def add(request, api_version):
        return HTTPRequest.objects.get_or_create(
            sha1=get_sha1(request.body.decode('utf-8')),
            defaults={
                'ip': get_client_ip(request),
                'api_version': api_version,
                'method': request.method,
                'data': str(request.body, encoding='utf-8'),
            })

    def __str__(self):
        return f'[{self.modified}] ({self.sha1:.7}) {self.method} - {self.ip}'

    class Meta:
        verbose_name = _('HTTP Request')
        verbose_name_plural = _('HTTP Requests')


class ErrorLogger(models.Model):
    added = models.DateTimeField(verbose_name=_('Datetime'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Datetime'), auto_now=True, db_index=True)
    http_request_sha1 = models.CharField(verbose_name=_('SHA1'), max_length=40, db_index=True, unique=True)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True, default=None)
    traceback = models.TextField(verbose_name=_('Traceback'), null=True, blank=True, default=None)

    class Meta:
        verbose_name = _('Error')
        verbose_name_plural = _('Errors')

    def __str__(self):
        return f'[{self.modified:%Y-%m-%d %H:%M:%S}] {self.http_request_sha1}'
