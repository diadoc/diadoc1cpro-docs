
ItemIdentificationNumber
========================

Номер средств идентификации товаров `(НомСредИдентТов) <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239778>`_

.. rubric:: Свойства

:PackageIds
  **Коллекция строк (1-255)** — уникальный идентификатор вторичной (потребительской)/третичной (заводской, транспортной) упаковки [`НомУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239790>`_]. Обязателен при отсутствии [`КИЗ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239789>`_] и [`ИдентТрансУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239787>`_]

:TransPackageId
  **Строка (1-255)** — уникальный идентификатор транспортной упаковки [`ИдентТрансУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239787>`_]. Обязателен при отсутствии [`КИЗ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239789>`_] и [`НомУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239790>`_]

:Units
  **Коллекция строк (1-255)** — контрольный идентификационный знак [`КИЗ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239789>`_]. Обязателен при отсутствии [`ИдентТрансУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239787>`_] и [`НомУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239790>`_]
