# Поддержка прокси для NVDA #

* Автор: Jose Manuel Delicado
* Совместимость с NVDA: 2021.3 и выше
* Скачать [стабильную версию][1]

Это дополнение позволяет программе чтения с экрана NVDA подключаться к
Интернету через один или несколько прокси-серверов. Чтобы это стало
возможным, он применяет различные исправления к стандартной библиотеке
Python или модифицирует определенные переменные среды в зависимости от
выбранной конфигурации. Вы сможете автоматически обновлять NVDA и их
дополнения из вашей корпоративной среды и даже выполнять удаленные сеансы,
если это позволяет прокси-сервер вашей организации.

## Возможности

* Поддержка различных типов прокси-серверов: http, socks4 и socks5.
* Возможность перенаправить весь трафик через прокси-сервер или только
  определенный трафик (http, https, ftp).
* Возможность перенаправить весь трафик через прокси-сервер и после этого
  перенаправить определенный трафик через другие серверы (вложенные прокси).
* Переключение профиля и сброс настроек: если вы обычно работаете с
  портативной копией NVDA, вы можете создавать различные профили для разных
  сред (дом, работа, офис1, офис2) и активировать их вручную.

## Использование

Это дополнение добавляет новую категорию в диалог настроек NVDA под
названием "Прокси". В этой категории вы найдете четыре группы
настроек. Первый позволяет настроить общий прокси для всего
трафика. Остальные группы позволяют настраивать прокси-серверы только для
определенных протоколов. Все группы имеют следующие поля:

* Хост: имя хоста или IP-адрес прокси-сервера. Оставьте пустым, чтобы
  отключить этот конкретный прокси.
* Порт: порт сервера.
* Имя пользователя: необязательно. Имя пользователя для аутентификации
  сервера.
* Пароль: необязательно. Пароль для аутентификации сервера. Обратите
  внимание, что для серверов socks4 пароль не требуется.

Помимо предыдущих полей, в первой группе настроек доступны следующие опции:

* Тип прокси SOCKS: можно выбрать socks4, socks5 или http.
* Использовать прокси для DNS-запросов, если это возможно: если этот флажок
  установлен, имена хостов или доменные имена будут напрямую отправляться и
  разрешаться на прокси-сервере. Если флажок снят, имена будут разрешаться
  локально, и сервер будет получать только IP-адрес назначения. Обратите
  внимание, что не все прокси-серверы socks4 поддерживают эту опцию.

Как правило, большинству пользователей потребуется настроить только первую
группу параметров. Если вы не знаете данные своего прокси-сервера,
обратитесь за дополнительной информацией к сетевому администратору вашей
организации.

## Ограничения

* Очень ограниченная поддержка IPV6.
* Трафик UDP поддерживается не на всех прокси-серверах.
* Внешние библиотеки DLL не будут учитывать параметры, настроенные в этом
  дополнении.
* Для HTTP-прокси-серверов поддерживается только базовая
  аутентификация. Дайджест-аутентификация не поддерживается.
* Для перенаправления всего трафика (включая https-соединения) через
  http-прокси сервер должен поддерживать метод CONNECT http.
* Невозможно настроить режим "прямое подключение". Если вы отключите
  конкретный прокси, вместо него будет использоваться системное значение по
  умолчанию.

## Список изменений

### Версия 1.1

* Совместимость с NVDA 2022.1.
* В целях безопасности минимальная версия NVDA установлена на 2021.3.
* Исправлена функция socket.getaddrinfo, когда установлен флажок
  "Использовать прокси для DNS-запросов, если возможно" и настроен общий
  прокси.

### Версия 1.0

* Первый выпуск.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=nvdaproxy