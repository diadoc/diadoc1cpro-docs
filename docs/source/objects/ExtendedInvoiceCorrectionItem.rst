
ExtendedInvoiceCorrectionItem
=============================

Сведения о товаре (работе, услуге), имущественном праве `(СведТов) <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611262>`_

.. rubric:: Свойства

:Product:
  **Строка (1-1000)** — наименование отгруженных товаров (выполненных работ, оказанных услуг), переданных имущественных прав [`НаимТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611263>`_]

:OriginalValues:
  :doc:`InvoiceItemFields <../../objects/InvoiceItemFields>` — поля до изменения

:CorrectedValues:
  :doc:`InvoiceItemFields <../../objects/InvoiceItemFields>` — поля после изменения

:AmountsInc:
  :doc:`AmountsDiff <../../objects/AmountsDiff>` — стоимость товаров (работ, услуг), имущественных прав - увеличение

:AmountsDec:
  :doc:`AmountsDiff <../../objects/AmountsDiff>` — стоимость товаров (работ, услуг), имущественных прав - уменьшение

:OriginalNumber:
  **Число (1-6)** — порядковый номер товара (выполненных работ, оказанных услуг) и пр. [`ПорНомТовВСЧФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611268>`_]

:ItemArticle:
  **Строка (1-50)** — артикул товара [`АртикулТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611278>`_]

:ItemTypeCode:
  **Строка (=10)** — код вида товара [`КодВидТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611279>`_]

:ItemVendorCode:
  **Строка (1-100)** — код товара [`КодТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611277>`_]

:ItemKind:
  **Строка (1-10)** — сорт товара [`СортТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611280>`_]

:ItemCharact:
  **Строка (1-1000)** — характеристика/описание товара [`ХарактерТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611281>`_]

:StructedAdditionalInfos:
  **Коллекция** :doc:`StructedAdditionalInfo <../../objects/StructedAdditionalInfo>` — информационное поле факта хозяйственной жизни 2 [`ИнфПолФХЖ2 <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611270>`_]

:OriginalItemIdentificationNumbers:
  **Коллекция** :doc:`ItemIdentificationNumber <../../objects/ItemIdentificationNumber>` — номер средства идентификации товаров до изменения [`НомСредИдентТовДо <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611273>`_]

:CorrectedItemIdentificationNumbers:
  **Коллекция** :doc:`ItemIdentificationNumber <../../objects/ItemIdentificationNumber>` — номер средства идентификации товаров после изменения [`НомСредИдентТовПосле <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611275>`_]

:ItemTracingInfos:
  **Коллекция** :doc:`ItemTracingInfo <../../objects/ItemTracingInfo>` — сведения о товаре, подлежащем прослеживаемости [`СведПрослеж <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611276>`_]
