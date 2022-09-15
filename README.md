Online shop project.


settings.py переименован в base.py
> settings.py -> base.py
Дополнительные настройки вынесены в conf.py

![Пустой диаграммой](https://user-images.githubusercontent.com/91150884/190425971-1dd63bdb-64b4-4d49-b97e-58fd90446bff.png)




urls.py вынесено в директорию urls
> urls.py -> urls\urls.py



## Структура БД

![Пустой диаграммой (1)](https://user-images.githubusercontent.com/91150884/190438696-b1c0c9d0-4fae-40fe-8c0d-f21a2382031c.png)





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

