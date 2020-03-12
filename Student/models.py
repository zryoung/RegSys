from django.db import models


# Create your models here.
class Stud(models.Model):
    name = models.CharField('姓名', max_length=20)
    idCard = models.CharField('身份证号', max_length=18)
    phone1 = models.CharField('联系电话1', max_length=20)
    phone2 = models.CharField('联系电话2', max_length=20, null=True, blank=True)
    primarySchool = models.CharField('毕业小学', max_length=50, null=True, blank=True)
    juniorSchool = models.CharField('毕业初中', max_length=50)
    testScore1 = models.DecimalField('初三上学期期中考成绩', max_digits=5, decimal_places=2, null=True, blank=True)
    testRank1 = models.IntegerField('初三上学期期中考年级排名', null=True, blank=True)
    testScore2 = models.DecimalField('初三上学期期末考成绩', max_digits=5, decimal_places=2, null=True, blank=True)
    testRank2 = models.IntegerField('初三上学期期末考年级排名', null=True, blank=True)
    specialty = models.CharField('特长', max_length=20, null=True, blank=True)
    photo = models.ImageField('照片', upload_to='img')

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.OneToOneField(Stud, on_delete=models.CASCADE)
    classRoom = models.CharField('试室号', max_length=50)
    seatNo = models.CharField('座位号', max_length=20)

    class Meta:
        verbose_name = '准考证'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
