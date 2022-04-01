ItemIdentificationNumber
============================

Номер средств идентификации товаров `(НомСредИдентТов) <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597474>`_

.. rubric:: Свойства

:PackageIds:
  **Коллекция строк (1-255)** — уникальный идентификатор вторичной (потребительской) или третичной (заводской, транспортной) упаковки [`НомУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597504>`_]. Обязателен при отсутствии [`КИЗ <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597479>`_] и [`ИдентТрансУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597512>`_]

:TransPackageId:
  **Строка (1-255)** — уникальный идентификатор транспортной упаковки [`ИдентТрансУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597512>`_]. Обязателен при отсутствии [`КИЗ <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597479>`_] и [`НомУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597504>`_]

:Units:
  **Коллекция строк (1-255)** — контрольный идентификационный знак [`КИЗ <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597479>`_]. Обязателен при отсутствии [`ИдентТрансУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597512>`_] и [`НомУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597504>`_]