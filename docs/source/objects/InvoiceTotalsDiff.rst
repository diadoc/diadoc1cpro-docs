
Totals
======

Реквизиты строки "Всего увеличение" или "Всего увеличение" `(ВсегоУвел) <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611154>`_ и `(ВсегоУм) <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611155>`_

.. rubric:: Свойства

:Total:
  **Число (19.2)** — всего увеличение/уменьшение, стоимость товаров (работ, услуг), имущественных прав с налогом [`СтТовУчНалВсего <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611157>`_]. Обязательно, кроме случая, когда все элементы [`НалСтДо <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=4427463>`_] из множественной `таблицы 5.11 <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=4427286>`_ = "НДС исчисляется налоговым агентом"

:TotalWithVatExcluded\*:
  **Число (19.2)** — всего увеличение/уменьшение, стоимость товаров (работ, услуг), имущественных прав без налога [`СтТовБезНДСВсего <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611156>`_]

:Vat:
  **Число (19.2)** — всего увеличение/уменьшение, сумма налога  [`СумНал <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611159>`_]. Обязательно, кроме случая, когда все элементы [`НалСтДо <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=4427532>`__] из множественной `таблицы 5.11 <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=4427286>`_ = "НДС исчисляется налоговым агентом"

:WithoutVat:
  **Строка (1-7)** — без НДС. Принимает значение либо "false", либо "true". Используется для заполнения [`СумНал <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611159>`_].
  Если указано значение "true", тогда будет заполнено [`БезНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611160>`_]. Обязательно, кроме случая, когда все элементы [`НалСтДо <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=4427532>`__] из множественной `таблицы 5.11 <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=4427286>`_ = "НДС исчисляется налоговым агентом"


\*обязательные поля