Online shop project.





urls.py вынесено в директорию urls
> urls.py -> urls\urls.py

settings.py переименован в base.py
> settings.py -> base.py

Кастомные настройки вынесены в conf.py

env хранит окружения для различных задач

![Пустой диаграммой (1)](https://user-images.githubusercontent.com/91150884/190438947-70b64dde-f19d-4949-8313-e872ddea588e.png)



## Структура БД

![db_sturucture](https://user-images.githubusercontent.com/91150884/190438855-764c198c-7ba6-4541-a3dc-319286409f43.png)



## Приложения (Apps)

Прилложения помещены в директорию 'apps', в параметрах base.py добавлено:
```
sys.path.append(
    os.path.join(BASE_DIR, "apps")
)
```

#Apps

abstracts
auths
contacts
goods
locations
orders
shops

