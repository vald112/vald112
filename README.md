Данный бот для телеграм был написан для личного пользования.

Бот написан на python3.9. На данный момент используется на Orange pi PC 2, на Debian 11 также работает. 

Функции бота:
1. Присылает ежедневно в 7.30 погоду, нагруженность дорог (в данном примере указан город Краснодар). В обновленной версии был закомментирован блок с выдачей информации по пробкам (замечено не стабильно прогружается страница яндек.пробки библиотекой Selenium) 
2. Если боту прислать аудио-файл, то файл направится по webdav на nextcloud/owncloud.
3. ~~Присылает нагруженность дорог в Краснодаре~~
4. Присылает текущую температуру на улице, а также оповещает об осадках. (парсится страница яндекс, никакого api нет)
5. Присылает по 1 статье с хабра. Парсится страница хабра. Был переработан интерфейс. Теперь есть кнопки управления и можно не писать сообщения, а нажимать на виртуальную клавиатуру.
