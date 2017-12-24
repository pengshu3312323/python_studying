
1.DetailView的如何把上下文传入模板html？
--如果不指定context_object_name ，对象名自动根据model名生成，如model="Post",context name="post"

2.URLField输入时浏览器提示“请输入正确的URL”，在表单中添加novalidate属性也不行

如果你的表单包含URLField、EmailField 或其它整数字段类型，Django 将使用url、email和 number 这样的HTML5 输入类型。
默认情况下，浏览器可能会对这些字段进行它们自身的验证，这些验证可能比Django 的验证更严格。
如果你想禁用这个行为，请设置form 标签的novalidate 属性，或者指定一个不同的字段，如TextInput。

--未解决

3.{% load static %}无效
{% load static %}和{% extends "XXX/base.html" %}不能同时使用。。。
去掉{% extends ... %}后正常

4.修改了模型后（添加了non-nullable Feild属性），数据库内的原数据缺少记录
--手动添加或设置default值，或blank=True，null=True

5.通过ForeignKey关联User，手动添加时出错（应该添加user.id，却添加成user.username）,
报错：ValueError: invalid literal for int() with base 10
修改后还是报错
--直接从Mysql中删除了相关条目，再migrate

6.更改模型后报“Unknown column 'XXX' in 'field list'”
--删除了app下的migrations文件夹（Django ORM对其只增加不删减）

7.明明模型做了更改，makemigrations也有更新，但migrate提示“No migrations to apply”
--在Mysql中，删除TABLE django_migrations中的原有条目后，再migrate

8.为模型添加了ImageField，需安装Pillow（作用？）
settings.py中添加：
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

urls.py中添加：
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

template中通过<img src="{{ post.image.url }}">成功显示出图片，但实现过程的意义不明了

9.一篇文章含有多张图片？