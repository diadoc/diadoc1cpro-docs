
Item
====

Сведения об отгруженных товарах (о выполненных работах, оказанных услугах), переданных имущественных правах `(СведТов) <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239722>`_

.. rubric:: Свойства

:AdditionalProperty:
  **Строка (1-4)** — дополнительная информация о признаке [`ДопПризн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239740>`_]

:CatalogCode:
  **Строка (=27)** — код каталога [`КодКат <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239761>`_]

:CustomDeclarations:
  **Коллекция** :doc:`CustomDeclaration <../../objects/CustomDeclaration820>` — сведения о таможенной декларации [`СвТД <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239764>`_]

:Excise\*:
  **Число (19.2)** — сумма акциза [`СумАкциз <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239730>`_].
  Если не указано значение, тогда будет заполнено поле [`БезАкциз <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239733>`_]

:HyphenSubtotal:
  **Булево** — признак того, что стоимость товаров (работ, услуг) не указана. Если Истина, то будет установлено значение "-" в поле [`ДефСтТовУчНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239738>`_]. Обязателен при [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФ или [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФДОП при отсутствии [`СтТовУчНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427427>`__]

:HyphenUnit:
  **Булево** — признак того, что код единицы измерения не указан. Если Истина, то будет установлено значение "-" в поле [`ДефОКЕИ_Тов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=318878>`_]. Обязателен при [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФ или [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФДОП при отсутствии [`ОКЕИ_Тов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427428>`__]

:HyphenVat\*:
  **Булево** — признак того, что сумма налога не указана. Если Истина, то будет установлено значение "-" в поле [`ДефНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239719>`_]

:ItemArticle:
  **Строка (1-50)** — артикул товара [`АртикулТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239759>`_]. Обязателен при отсутствии [`НаимТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427429>`__],  [`ХарактерТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427430>`__] и [`КодТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427431>`__]

:ItemCharact:
  **Строка (1-1000)** — характеристика товара [`ХарактерТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239758>`_]. Обязателен при отсутствии [`НаимТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427429>`__], [`КодТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427431>`__] и [`АртикулТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239759>`__]

:ItemIdentificationNumbers:
  **Коллекция** :doc:`ItemIdentificationNumber <../../objects/ItemIdentificationNumber>` — номер средств идентификации товаров [`НомСредИдентТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239767>`_]. Обязателен для товаров, включенных в систему маркировки

:ItemKind:
  **Строка (1-10)** — сорт товара [`СортТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239760>`_]

:ItemMark:
  **Строка (=1)** — признак Товар/Работа/Услуга/Право/Иное   [`ПрТовРаб <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239739>`_] . Принимает |Item-ItemMark|_

:ItemToRelease:
  **Число (26,11)** — заказанное количество (количество надлежит отпустить) [`НадлОтп <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239742>`_]

:ItemTracingInfos:
  **Коллекция** :doc:`ItemTracingInfo <../../objects/ItemTracingInfo>` — сведения о товаре, подлежащем прослеживаемости [`СведПрослеж <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239766>`_]

:ItemTypeCode:
  **Строка (=10)** — код вида товара [`КодВидТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239762>`_]. Обязателен в случае отражения в счете-фактуре товаров, вывезенных за пределы территории Российской Федерации на территорию государства-члена Евразийского экономического союза

:ItemVendorCode:
  **Строка (1-100)** — код товара [`КодТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239741>`_]. Обязателен при отсутствии [`НаимТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427429>`__],  [`ХарактерТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427430>`__] и [`АртикулТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239759>`__]

:Price:
  **Число (26.11)** — цена (тариф) за единицу измерения [`ЦенаТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239729>`_]

:Product:
  **Строка (1-1000)** — наименование товара (описание выполненных работ, оказанных услуг), имущественных прав [`НаимТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239723>`_]. Обязателен при отсутствии [`ХарактерТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427430>`__], [`АртикулТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239759>`__] и [`КодТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427431>`__]

:Quantity:
  **Число (26.11)** — количество (объем) [`КолТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239728>`_]. Обязателен при [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФ или [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФДОП при наличии [`ОКЕИ_Тов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427428>`__]

:StructedAdditionalInfos:
  **Коллекция** :doc:`StructedAdditionalInfo <../../objects/AdditionalInfoItem>` — информационное поле факта хозяйственной жизни 2 [`ИнфПолФХЖ2 <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239765>`_]

:Subtotal:
  **Число (19.2)** — стоимость товаров (работ, услуг), имущественных прав с налогом - всего [`СтТовУчНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239737>`__].
  Если не указано значение, тогда будет заполнено поле [`ДефСтТовУчНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239738>`_]. Обязателен при [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФ или [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФДОП при отсутствии [`СтТовУчНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427435>`__]

:SubtotalWithVatExcluded:
  **Число (19.2)** — стоимость товаров (работ, услуг), имущественных прав без налога - всего [`СтТовБезНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239735>`_]. Обязателен для [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФ или [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФДОП, кроме случаев, когда отсутствие числового значения предусмотрено `Правилами <https://normativ.kontur.ru/document?moduleId=1&documentId=310239#l13>`_ заполнения счета-фактуры, применяемого при расчетах по налогу на добавленную стоимость

:TaxRate\*:
  **Строка (1-35)** — налоговая ставка, принимает одно из значений [`НалСт <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239734>`_]

:Unit:
  **Строка (3-4)** — код единицы измерения [`ОКЕИ_Тов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239724>`__]. Обязателен при [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФ или [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427426>`_] = СЧФДОП и наличии натурального измерителя факта хозяйственной жизни

:UnitName:
  **Строка (1-255)** — наименование единицы измерения [`НаимЕдИзм <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239726>`_]. Обязателен при наличии [`ОКЕИ_Тов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427428>`__]

:Vat\*:
  **Число (19.2)** — сумма налога, предъявляемая покупателю [`СумНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239736>`_]

:WithoutVat\*:
  **Строка** — принимает значение либо "false", либо "true". Используется для заполнения [`СумНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239736>`_].
  Если указано значение "true", тогда будет заполнено [`БезНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239711>`_]


\*обязательные поля

.. rubric:: Дополнительная информация

.. |Item-ItemMark| replace:: возможные значения
.. _Item-ItemMark:

===================== ===========================================================================================================================
Значение *ItemMark*   Описание
===================== ===========================================================================================================================
Job                   работа
NotSpecified          неопределено
Other                 иное
Property              имущество
PropertyRights        имущественные права
Service               услуга
===================== ===========================================================================================================================