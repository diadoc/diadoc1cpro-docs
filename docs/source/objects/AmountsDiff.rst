
AmountsDiff
===========

Итоговые поля табличной части корректировочного счета-фактуры, показывающиеся увеличение или уменьшение показателей.

.. rubric:: Свойства

:Excise:
  **Число (19.2)** — сумма акциза [`АкцизРазн.СумУвел/СумУм <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611304>`_]

:Total:
  **Число (19.2)** — стоимость товаров (работ, услуг), имущественных прав - всего [`СтТовУчНал.СтоимУм/СтоимУвел <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611298>`_]

:TotalWithVatExcluded:
  **Число (19.2)** — стоимость товаров (работ, услуг), имущественных прав без налога - всего [`СтТовБезНДС.СтоимУм/СтоимУвел <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2968157>`_]

:Vat:
  **Число (19.2)** — сумма налога, увеличение (уменьшение) [`СумНалРазн.СумУвел/СумУм <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611302>`_]. Обязательна при НалСтДо [`НалСтДо <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=4427248>`_] не =  "НДС исчисляется налоговым агентом"
