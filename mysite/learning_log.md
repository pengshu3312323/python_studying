
1.DetailView����ΰ������Ĵ���ģ��html��
--�����ָ��context_object_name ���������Զ�����model�����ɣ���model="Post",context name="post"

2.URLField����ʱ�������ʾ����������ȷ��URL�����ڱ������novalidate����Ҳ����

�����ı�����URLField��EmailField �����������ֶ����ͣ�Django ��ʹ��url��email�� number ������HTML5 �������͡�
Ĭ������£���������ܻ����Щ�ֶν��������������֤����Щ��֤���ܱ�Django ����֤���ϸ�
���������������Ϊ��������form ��ǩ��novalidate ���ԣ�����ָ��һ����ͬ���ֶΣ���TextInput��

--δ���

3.{% load static %}��Ч
{% load static %}��{% extends "XXX/base.html" %}����ͬʱʹ�á�����
ȥ��{% extends ... %}������

4.�޸���ģ�ͺ������non-nullable Feild���ԣ������ݿ��ڵ�ԭ����ȱ�ټ�¼
--�ֶ���ӻ�����defaultֵ����blank=True��null=True

5.ͨ��ForeignKey����User���ֶ����ʱ����Ӧ�����user.id��ȴ��ӳ�user.username��,
����ValueError: invalid literal for int() with base 10
�޸ĺ��Ǳ���
--ֱ�Ӵ�Mysql��ɾ���������Ŀ����migrate

6.����ģ�ͺ󱨡�Unknown column 'XXX' in 'field list'��
--ɾ����app�µ�migrations�ļ��У�Django ORM����ֻ���Ӳ�ɾ����

7.����ģ�����˸��ģ�makemigrationsҲ�и��£���migrate��ʾ��No migrations to apply��
--��Mysql�У�ɾ��TABLE django_migrations�е�ԭ����Ŀ����migrate

8.Ϊģ�������ImageField���谲װPillow�����ã���
settings.py����ӣ�
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

urls.py����ӣ�
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

template��ͨ��<img src="{{ post.image.url }}">�ɹ���ʾ��ͼƬ����ʵ�ֹ��̵����岻����

9.һƪ���º��ж���ͼƬ��