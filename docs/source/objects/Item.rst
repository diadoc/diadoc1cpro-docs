
Item
====

Сведения об отгруженных товарах (о выполненных работах, оказанных услугах), переданных имущественных правах `(СведТов) <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239722>`_

.. rubric:: Свойства

:Product:
  **Строка (1-1000)** - наименование товара (описание выполненных работ, оказанных услуг), имущественных прав [`НаимТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239723>`_]

:Unit:
  **Строка (3-4)** - код единицы измерения [`ОКЕИ_Тов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239724>`_]

:UnitName:
  **Строка (1-255)** - наименование единицы измерения [`НаимЕдИзм <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239726>`_]

:Quantity:
  **Число (26,11)** - количество (объем) [`КолТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239728>`_]

:Price:
  **Число (26,11)** - цена (тариф) за единицу измерения [`ЦенаТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239729>`_]

:Excise:
  **Число (19,2)** - сумма акциза [`СумАкциз <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239730>`_].
  Если не указано значение, тогда будет заполнено поле [`БезАкциз <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239733>`_].

:TaxRate:
  **Строка (1-35)** - налоговая ставка, принимает одно из значений [`НалСт <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239734>`_]

:SubtotalWithVatExcluded:
  **Число (19,2)** - стоимость товаров (работ, услуг), имущественных прав без налога - всего [`СтТовБезНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239735>`_]

:Vat:
  **Число (19,2)** - сумма налога, предъявляемая покупателю [`СумНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239736>`_].
  Если есть значение, то будет заполнено поле [`СумНал/СумНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239718>`_].
  Если передать значение равным -1, тогда будет заполнено поле [`СумНал/ДефНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239719>`_]

:WithoutVat:
  **Строка** - принимает значение либо "false", либо "true". Используется для заполнения [`СумНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239736>`_].
  Если указано значение "true", тогда будет заполнено [`БезНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239711>`_]

:Subtotal:
  **Число (19,2)** - стоимость товаров (работ, услуг), имущественных прав с налогом - всего [`СтТовУчНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239737>`_].
  Если не указано значение, тогда будет заполнено поле [`ДефСтТовУчНал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239738>`_].

:ItemMark:
  **Строка** - принимает значения "Property" (имущество), "Job" (работа), "Service" (услуга), "PropertyRights" (имущественные права), "Other" (иное), "NotSpecified" (Неопределено) [`ПрТовРаб <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239739>`_]

:AdditionalProperty:
  **Строка (1-4)** - дополнительная информация о признаке [`ДопПризн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239740>`_]

:ItemVendorCode:
  **Строка (1-100)** - код товара [`КодТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239741>`_]

:ItemToRelease:
  **Число (26,11)** - заказанное количество (количество надлежит отпустить) [`НадлОтп <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239742>`_]

:ItemCharact:
  **Строка (1-1000)** - характеристика/описание товара [`ХарактерТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239758>`_]

:ItemArticle:
  **Строка (1-50)** - артикул товара [`АртикулТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239759>`_]

:ItemKind:
  **Строка (1-10)** - сорт товара [`СортТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239760>`_]

:CatalogCode:
  **Строка (=27)** - код каталога [`КодКат <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239761>`_]

:ItemTypeCode:
  **Строка (=10)** - код вида товара [`КодВидТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239762>`_]

:CustomDeclarations:
  **Коллекция** :doc:`CustomDeclaration <../../objects/CustomDeclaration>` - сведения о таможенной декларации [`СвТД <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239764>`_]

:StructedAdditionalInfos:
  **Коллекция** :doc:`StructedAdditionalInfo <../../objects/StructedAdditionalInfo>` - информационное поле факта хозяйственной жизни 2 [`ИнфПолФХЖ2 <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239765>`_]

:ItemTracingInfos:
  **Коллекция** :doc:`ItemTracingInfo <../../objects/ItemTracingInfo>` - сведения о товаре, подлежащем прослеживаемости [`СведПрослеж <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239766>`_]

:ItemIdentificationNumbers:
  **Коллекция** :doc:`ItemIdentificationNumber <../../objects/ItemIdentificationNumber>` - номер средств идентификации товаров [`НомСредИдентТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239767>`_]
