Online shop project.

settings.py переименован в base.py
> settings.py -> base.py
Дополнительные настройки вынесены в conf.py

urls.py вынесено в директорию urls
> urls.py -> urls\urls.py


Прилложения помещены в директорию 'apps', в параметрах base.py добавлено:
```
sys.path.append(
    os.path.join(BASE_DIR, "apps")
)
```
