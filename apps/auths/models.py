# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     PermissionsMixin,
# )
# from django.db.models import (
#     EmailField,
#     CharField,
# )

# from abstracts.models import AbstractDateTime


# class CustomUser(
#     AbstractBaseUser,
#     PermissionsMixin,
#     AbstractDateTime
# ):
#     email = EmailField(
#         unique=True,
#         db_index=True,
#         verbose_name="Почта/Логин"
#     )
#     first_name = CharField(
#         max_length=200,
#         verbose_name="Имя"
#     )
#     last_name = CharField(
#         max_length=200,
#         verbose_name="Фамилия"
#     )
