# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from typeidea.blog.models import Post


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
    )

    target = models.ForeignKey(Post, verbose_name="评论目标")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱")
    website = models.URLField(verbose_name="网站地址")
    content = models.CharField(max_length=2000, verbose_name="内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    status = models.IntegerField(choices=STATUS_ITEMS, default=STATUS_NORMAL, verbose_name="状态")

    class Meta:
        verbose_name = verbose_name_plural = "评论"