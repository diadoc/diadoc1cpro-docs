
ItemIdentificationNumber
========================

Номер средств идентификации товаров `(НомСредИдТовТип) <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969553>`_

.. rubric:: Свойства

:PackageIds
  **Коллекция строк (1-255)** — уникальный идентификатор вторичной (потребительской)/третичной (заводской, транспортной) упаковки [`НомУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969564>`_]. Обязателен при отсутствии [`КИЗ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969557>`_] и [`ИдентТрансУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969562>`_]

:TransPackageId
  **Строка (1-255)** — уникальный идентификатор транспортной упаковки [`ИдентТрансУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969562>`_]. Обязателен при отсутствии [`КИЗ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969557>`_] и [`НомУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969564>`_]

:Units
  **Коллекция строк (1-255)** — контрольный идентификационный знак [`КИЗ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969557>`_]. Обязателен при отсутствии [`ИдентТрансУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969562>`_] и [`НомУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969564>`_]
