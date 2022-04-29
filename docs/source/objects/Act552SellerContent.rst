Act552SellerContent
====================

Содержание титула продавца *Акта о выполнении работ* в формате приказа `ММВ-7-10/552@ <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5994969>`_

.. rubric:: Свойства

:AdditionalInfo:
  **Структура** :doc:`AdditionalInfoId <../../objects/552@/AdditionalInfoId>` — информационное поле факта хозяйственной жизни 1 [`ИнфПолФХЖ1 <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5994970>`_]

:Buyer\*:
  **Коллекция** :doc:`ExtendedOrganizationInfo <../../objects/552@/ExtendedOrganizationInfo>` — заказчик [`Заказчик <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5994971>`_]

:Currency\*:
  **Строка (=3)** — код валюты [`КодОКВ <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5994972>`_]

:CurrencyRate:
  **Число (10.4)** — курс валюты [`КурсВал <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5994973>`_]

:DocumentCreator\*:
  **Строка (1-1000)** — наименование составителя информации исполнителя [`НаимЭконСубСост <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5994975>`_]

:DocumentCreatorBase:
  **Строка (1-120)** — основание, по которому организация является составителем информации исполнителя [`ОснДоверОргСост <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5994976>`_]. Обязателен, если составитель информации исполнителя не является исполнителем

:DocumentDate\*:
  **Дата (ДД.ММ.ГГГГ)** — дата составления документа о передаче результатов работ [`ДатаДокПРУ <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995187>`_]

:DocumentName\*:
  **Строка (1-255)** — наименование документа, определенное организацией [`НаимДокОпр <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995190>`_]

:DocumentNumber\*:
  **Строка (1-255)** — номер документа о передаче результатов работ [`НомДокПРУ <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995189>`_]

:GovernmentContractInfo:
  **Строка (1-255)** — идентификатор государственного контракта [`ИдГосКон <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995192>`_]

:Grounds\*:
  **Коллекция** :doc:`GroundInfo <../../objects/552@/GroundInfo>` — основание [`Основание <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995193>`_]

:OperationTitle:
  **Строка (1-2000)** — заголовок содержания операции [`ЗагСодОпер <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995194>`_]

:OperationType:
  **Строка (1-225)** — вид операции [`ВидОперации <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995196>`_]

:RevisionDate\*:
  **Дата (ДД.ММ.ГГГГ)** — дата исправления документа [`ДатаИспрДокПРУ <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995204>`_]

:RevisionNumber\*:
  **Число (3)** — номер исправления документа [`НомИспрДокПРУ <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995207>`_]

:Seller\*:
  **Коллекция** :doc:`ExtendedOrganizationInfo <../../objects/552@/ExtendedOrganizationInfo>` — исполнитель [`Исполнитель <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995210>`_]

:Signers\*:
  **Коллекция** :doc:`ExtendedSigner <../../objects/552@/ExtendedSigner>` — сведения о лице, подписавшем информацию исполнителя в электронном виде [`Подписант <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995212>`_]

:TransferInfo\*:
  **Коллекция** :doc:`Act552TransferInfo <../../objects/552@/Act552TransferInfo>` — содержание факта хозяйственной жизни 2 — сведения о передаче результатов работ [`СодФХЖ2 <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995213>`_]

:Type:
  **Строка** — тип документа, константа

:Works\*:
  **Коллекция** :doc:`Act552WorkDescription <../../objects/552@/Act552WorkDescription>` — описание выполненных работ [`ОписРабот <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995215>`_]


\*обязательные поля