
Титул покупателя UсdBuyerContent
================================

Содержание титула покупателя *Универсального корректировочного документа* в формате приказа `ЕД-7-26/736@ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857#h765>`_

.. rubric:: Свойства

:AcceptanceDate
  **Дата (ДД.ММ.ГГГГ)** — дата согласования [`ДатаСоглас <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611143>`_]. Обязательна, если дата согласования не совпадает со значением [`ДатаНапр <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611311>`_], указанным в файле обмена корректировочного счета-фактуры с дополнительной информацией

:AdditionalInfoId
  **Коллекция** :doc:`AdditionalInfoId <../../objects/AdditionalInfoId736>` — информационное поле факта хозяйственной жизни 4 [`ИнфПолФХЖ4 <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611144>`_]

:Creator*
  **Строка (1-1000)** — наименование экономического субъекта - составителя файла обмена информации покупателя [`НаимЭконСубСост <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611138>`_]

:CreatorBase
  **Строка (1-120)** — основание, по которому экономический субъект является составителем файла обмена (информации покупателя) [`ОснДоверОргСост <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611139>`_]. Обязательно, если составитель информации продавца не является продавцом

:OperationContent*
  **Строка (1-255)** — содержание операции (текст) [`СодОпер <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611142>`_]

:Signers*
  **Коллекция** :doc:`ExtendedSigner <../../objects/ExtendedSigner>` — сведения о лице, подписывающем файл обмена информации покупателя в электронной форме [`Подписант <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611145>`_]


\*обязательные поля