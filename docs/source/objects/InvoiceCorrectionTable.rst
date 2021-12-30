
InvoiceCorrectionTable
======================

Сведения таблицы корректировочного счета-фактуры с дополнительной информацией (содержание события (факта хозяйственной жизни) 2 — сведения об изменении стоимости ранее отгруженных товаров (выполненных работ, оказанных услуг), переданных имущественных прав) `(ТаблКСчФ) <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611146>`_

.. rubric:: Свойства

:Items:
  **Коллекция** :doc:`ExtendedInvoiceCorrectionItem <../../objects/ExtendedInvoiceCorrectionItem>` — сведения о товаре (работе, услуге), имущественном праве [`СведТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611150>`_]

:TotalsDec:
  :doc:`Totals <../../objects/InvoiceTotalsDiff>` — реквизиты строки "Всего уменьшение" [`ВсегоУм <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611152>`_]

:TotalsInc:
  :doc:`Totals <../../objects/InvoiceTotalsDiff>` — реквизиты строки "Всего увеличение" [`ВсегоУвел <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611151>`_]
