from django.db import models


class AddressLegalCode(models.Model):
    city_code = models.CharField('시군구코드', max_length=5)
    legal_code = models.CharField('법정동코드', max_length=5)
    full_code = models.CharField('법정동전체코드', max_length=10)
    address = models.CharField('법정동명', max_length=50)

    def __str__(self):
        return f'{self.address} : {self.full_code}'
