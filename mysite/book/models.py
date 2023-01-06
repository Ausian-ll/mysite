from django.db import models
# Create your models here.

class Tb_book_info(models.Model):
    book_id = models.CharField('书籍id',max_length=50,default='',primary_key=True)
    title = models.CharField('书籍名称',max_length=50)
    store = models.CharField('所属商店',max_length=50)
    price = models.DecimalField('价格',max_digits=7,decimal_places=2)
    status = models.CharField('书籍状态',max_length=5,default='0')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    updata_time = models.DateTimeField('更新时间',auto_now=True)
    num = models.IntegerField('库存')
    publish_id = models.CharField('出版社id',max_length=100,null=True)
    is_delete = models.BooleanField('删除',default=False)
    class Meta:
        db_table = 'tb_book_info'
