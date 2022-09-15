Online shop project.


settings.py переименован в base.py
> settings.py -> base.py
Дополнительные настройки вынесены в conf.py

![Пустой диаграммой](https://user-images.githubusercontent.com/91150884/190425971-1dd63bdb-64b4-4d49-b97e-58fd90446bff.png)




urls.py вынесено в директорию urls
> urls.py -> urls\urls.py



## Структура БД

![db_sturucture](https://user-images.githubusercontent.com/91150884/190425782-d3ca7f12-9ac7-4adb-8e1a-cbe87be5ae2b.png)




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

