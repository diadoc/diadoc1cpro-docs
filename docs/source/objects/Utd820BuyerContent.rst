
Титул покупателя Utd820BuyerContent
===================================

Содержание титула покупателя *Универсального передаточного документа* в формате приказа `ММВ-7-15/820@ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588#h345>`_

.. rubric:: Свойства

:AcceptanceDate:
  **Дата (ДД.ММ.ГГГГ)** — дата принятия товаров (результатов выполненных работ), имущественных прав (подтверждения факта оказания услуг) [`ДатаПрин <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237499>`_]. Обязательна, если дата получения груза не совпадает с [`ДатаПер <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427393>`_] информации продавца

:AdditionalInfoId:
  :doc:`AdditionalInfoId <../../objects/AdditionalInfoId>` — информационное поле документа [`ИнфПолФХЖ4 <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237502>`_]

:BuyerInfoCircumPublicProc:
  :doc:`BuyerInfoCircumPublicProc <../../objects/BuyerInfoCircumPublicProc>` — информация покупателя об обстоятельствах закупок для государственных и муниципальных нужд [`ИнфПокГосЗакКазн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237507>`_]. Обязательна при осуществлении закупок для обеспечения государственных и муниципальных нужд и (или) для формирования сведений о денежном обязательстве Федеральным казначейством

:ContentOperCode:
  :doc:`ContentOperCode <../../objects/ContentOperCode>` — код содержания операции [`КодСодОпер <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237508>`_]. Обязателен при отсутствии [`СодОпер <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427400>`__]

:DocumentCreator\*:
  **Строка (1-1000)** — составитель файла обмена (информации покупателя) [`НаимЭконСубСост <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237494>`_]

:DocumentCreatorBase:
  **Строка (1-120)** — основание, по которому экономический субъект является составителем файла обмена (информации покупателя) [`ОснДоверОргСост <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237496>`_]. Обязателен, если составитель информации покупателя не является покупателем

:Employee\*:
  :doc:`Employee <../../objects/Employee>` — работник организации покупателя [`РабОргПок <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237500>`_]

:OperationCode:
  **Строка (1-255)** — вид операции [`ВидОперации <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237497>`_]

:OperationContent:
  **Строка (1-255)** — содержание операции (текст) [`СодОпер <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237498>`_]. Обязательно при отсутствии [`КодСодОпер <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237508>`_]

:OtherIssuer\*:
  :doc:`OtherIssuer <../../objects/OtherIssuer>` — иное лицо [`ИнЛицо <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237501>`_]

:Signers\*:
  **Коллекция** :doc:`ExtendedSigner <../../objects/ExtendedSigner>` — подписанты документа [`Подписант <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=237503>`_]


\*обязательные поля