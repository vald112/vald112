Данный бот для телеграм был написан для личного пользования.

Бот написан на python3.9. На данный момент используется на Orangepi PC 2, на Debian 11 также работает. 

Функции бота:
1. Присылает погоду ежедневно в 7.30 погоду, нагруженность дорог (в данном примере указан город Краснодар).
2. Если боту прислать аудио файл, то файл направиться по webdav на nextcloud/owncloud.
3. По команде /p присылает нагруженность дорог в Краснодаре
4. По команде /w присылает текущую температуру на улице, а также оповещает об осадках. (парсится страница яндекс, никакого api нет)
5. По команде /news присылает 20 статей (все статьи с первой страницы) хабра. Парсится страница хабра. Пока что выглядит нелепо, но в скором времени займусь 
отображением статей. А именно будет переработан: 
  a) Вид сообщения. Будет отображаться последняя статья, под ней будет 2 кнопки, первая кнопка будет возвращать к обратной статье, вторая к следующей статье;
  b) Запись в sql была сделана по топорному, будет переработан механизм записи и вывода статей.
  
