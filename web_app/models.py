from django.db import models
from ckeditor.fields import RichTextField


class index(models.Model):
    oc_mid_tit_001 = models.CharField(
        max_length=100000, verbose_name='預約連結', blank=True)
    oc_mid_txt_001 = models.CharField(
        max_length=100000, verbose_name='臘腸狗圖-size:300X300px', blank=True)
    oc_mid_tit_002 = models.CharField(
        max_length=100000, verbose_name='科基圖-size:300X300px', blank=True)
    oc_mid_txt_002 = models.CharField(
        max_length=100000, verbose_name='博美圖-size:300X300px', blank=True)
    oc_mid_tit_003 = models.CharField(
        max_length=100000, verbose_name='柴犬圖-size:300X300px', blank=True)
    oc_mid_txt_003 = models.CharField(
        max_length=100000, verbose_name='吉娃娃圖-size:300X300px', blank=True)
    oc_mid_tit_004 = models.CharField(
        max_length=100000, verbose_name='雪納瑞圖-size:300X300px', blank=True)

    oc_dog_ctn_001 = RichTextField(
        max_length=100000, verbose_name='注意事項', blank=True)
    oc_dog_ctn_002 = RichTextField(
        max_length=100000, verbose_name='小美容', blank=True)
    oc_dog_ctn_003 = RichTextField(
        max_length=100000, verbose_name='大美容', blank=True)
    oc_dog_ctn_004 = RichTextField(
        max_length=100000, verbose_name='額外服務', blank=True)
    oc_dog_ctn_005 = RichTextField(
        max_length=100000, verbose_name='獲獎事項', blank=True)
    oc_dog_ctn_006 = RichTextField(
        max_length=100000, verbose_name='專業證照', blank=True)

    oc_dog_ph_001 = models.CharField(
        max_length=100000, verbose_name='獎項證照圖-1', blank=True)
    oc_dog_ph_002 = models.CharField(
        max_length=100000, verbose_name='獎項證照圖-2', blank=True)
    oc_dog_ph_003 = models.CharField(
        max_length=100000, verbose_name='獎項證照圖-3', blank=True)
    oc_dog_ph_004 = models.CharField(
        max_length=100000, verbose_name='獎項證照圖-4', blank=True)

    oc_dog_line = models.CharField(
        max_length=100000, verbose_name='LINE連結', blank=True)
    oc_dog_mail = models.CharField(
        max_length=100000, verbose_name='信箱', blank=True)
    oc_dog_phone = models.CharField(
        max_length=100000, verbose_name='電話', blank=True)
    oc_dog_adr = models.CharField(
        max_length=100000, verbose_name='地址', blank=True)
    oc_dog_fb = models.CharField(
        max_length=100000, verbose_name='Facebook', blank=True)
    oc_dog_ig = models.CharField(
        max_length=100000, verbose_name='instagram', blank=True)

    def __str__(self):
        return "首頁"

    class Meta:
        verbose_name_plural = "首頁"
        verbose_name = "首頁"
