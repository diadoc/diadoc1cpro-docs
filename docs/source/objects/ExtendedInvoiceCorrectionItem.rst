
ExtendedInvoiceCorrectionItem
=============================

Сведения о товаре (работе, услуге), имущественном праве `(СведТов) <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611262>`_

.. rubric:: Свойства

:AmountsDec:
  **Коллекция** :doc:`AmountsDiff <../../objects/AmountsDiff>` — стоимость товаров (работ, услуг), имущественных прав - уменьшение

:AmountsInc:
  **Коллекция** :doc:`AmountsDiff <../../objects/AmountsDiff>` — стоимость товаров (работ, услуг), имущественных прав - увеличение

:CorrectedItemIdentificationNumbers:
  **Коллекция** :doc:`ItemIdentificationNumber <../../objects/ItemIdentificationNumber>` — номер средства идентификации товаров после изменения [`НомСредИдентТовПосле <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611275>`_]

:CorrectedValues:
  **Коллекция** :doc:`InvoiceItemFields <../../objects/InvoiceItemFields>` — поля после изменения

:ItemAccountCredit:
  **Число (9)** — корреспондирующие счета: кредит [`КорСчКредит <https://normativ.kontur.ru/document?moduleId=1&documentId=402523&rangeId=2969309>`_]

:ItemAccountDedit:
  **Число (9)** — корреспондирующие счета: дебет [`КорСчДебет <https://normativ.kontur.ru/document?moduleId=1&documentId=402523&rangeId=2969308>`_]

:ItemArticle:
  **Строка (1-50)** — артикул товара [`АртикулТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611278>`_]

:ItemCharact:
  **Строка (1-1000)** — характеристика/описание товара [`ХарактерТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611281>`_]

:ItemKind:
  **Строка (1-10)** — сорт товара [`СортТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611280>`_]

:ItemTracingInfos:
  **Коллекция** :doc:`ItemTracingInfo <../../objects/ItemTracingInfo>` — сведения о товаре, подлежащем прослеживаемости [`СведПрослеж <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611276>`_]

:ItemTypeCode:
  **Строка (=10)** — код вида товара [`КодВидТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611279>`_]

:ItemVendorCode:
  **Строка (1-100)** — код товара [`КодТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611277>`_]

:OriginalItemIdentificationNumbers:
  **Коллекция** :doc:`ItemIdentificationNumber <../../objects/ItemIdentificationNumber>` — номер средства идентификации товаров до изменения [`НомСредИдентТовДо <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611273>`_]

:OriginalNumber:
  **Число (6)** — порядковый номер товара (выполненных работ, оказанных услуг) и пр. [`ПорНомТовВСЧФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611268>`_]

:OriginalValues:
**Коллекция** :doc:`InvoiceItemFields <../../objects/InvoiceItemFields>` — поля до изменения

:Product:
  **Строка (1-1000)** — наименование отгруженных товаров (выполненных работ, оказанных услуг), переданных имущественных прав [`НаимТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611263>`_]

:StructedAdditionalInfos:
  **Коллекция** :doc:`StructedAdditionalInfo <../../objects/StructedAdditionalInfo>` — информационное поле факта хозяйственной жизни 2 [`ИнфПолФХЖ2 <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611270>`_]
