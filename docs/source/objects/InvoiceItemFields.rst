
InvoiceItemFields
=================

Поля табличной части корректировочного счета-фактуры, принимающие значения до и после корректировки.

.. rubric:: Свойства

:UnitCode:
  **Строка (3-4)** - код единицы измерения [`ОКЕИ_Тов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611283>`_]

:UnitName:
  **Строка (1-255)** - наименование единицы измерения [`НаимЕдИзм <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611284>`_]

:Quantity:
  **Число (26,11)** - количество (объем) [`КолТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611285>`_]

:Price:
  **Число (26,11)** - цена (тариф) за единицу измерения [`ЦенаТов <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611286>`_]

:Excise:
  **Число (19,2)** - сумма акциза [`СумАкциз <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611287>`_].
  Если не указано значение, тогда будет заполнено поле [`БезАкциз <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611288>`_].

:TaxRate:
  **Строка (1-35)** - налоговая ставка, принимает одно из значений [`НалСт <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611289>`_]

:Vat:
  **Число (19,2)** - сумма налога, предъявляемая покупателю [`СумНал <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611293>`_].

:WithoutVat:
  **Строка** - принимает значение либо "false", либо "true". Используется для заполнения [`СумНал <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611295>`_].
  Если указано значение "true", тогда будет заполнено [`БезНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611294>`_]

:Total:
  **Число (19,2)** - стоимость товаров (работ, услуг), имущественных прав - всего [`СтТовУчНал <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611298>`_].

:TotalWithVatExcluded:
  **Число (19,2)** - стоимость товаров (работ, услуг), имущественных прав без налога - всего [`СтТовБезНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611299>`_]
