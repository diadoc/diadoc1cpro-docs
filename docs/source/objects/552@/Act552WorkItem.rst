Act552WorkItem
================

Сведения о выполненной работе `(Работа) <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000941>`_

.. rubric:: Свойства

:Description:
  **Строка (1-10000)** — описание работы [`Описание <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000944>`_]. Обязателен, если присутствует `НаимРабот <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000947>`_

:ItemAccountCredit:
  **Строка (9)** — кредит корреспондирующих счетов [`КорСчКредит <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000946>`_]

:ItemAccountDebit:
  **Строка (9)** — дебет корреспондирующих счетов [`КорСчДебет <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000945>`_]

:Name:
  **Строка (1-1000)** — наименование работ [`НаимРабот <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000947>`_]. Обязателен, если отсутствует `Описание <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000944>`_

:Price:
  **Число (26.11)** — цена  [`Цена <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000949>`_]

:Quantity:
  **Число (26.11)** — количество единиц товара [`КолТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000950>`_]. Обязателен при наличии `НаимРабот <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000947>`_

:StructedAdditionalInfos:
  **Коллекция** :doc:`AdditionalInfoItem <../../objects/552@/AdditionalInfoItem>` — информационное поле сведений о работе [`ИнфПолеОписРабот <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000954>`_]

:Subtotal:
 **Число (19.2)** — стоимость с учетом НДС [`СтоимУчНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000955>`__]

:SubtotalWithVatExcluded:
  **Число (19.2)** — стоимость без учета НДС [`СтоимБезНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000957>`_]

:TaxRate:
  **Строка (1-35)** — налоговая ставка [`НалСт <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000958>`_]. Принимает значение: 0% \| 10% \| 18% \| 20% \| 10/110 \| 18/118 \| 20/120 \| без НДС \| ИсчНалАг. ИсчНалАг означает, что НДС исчисляется налоговым агентом.

:UnitCode:
  **Строка (3-4)** — код единицы измерения [`ОКЕИ <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000959>`__]

:UnitName:
  **Строка (1-1000)** — наименование единицы измерения [`НаимЕдИзм <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000960>`_]

:Vat:
  **Число (19.2)** — сумма НДС [`СумНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=6000961>`_]

:СлужебнаяИнформация:	
  **ItemСлужебнаяИнформация** —  содержит ПрослеживаемыйТовар с типом Булево и ссылки на следующие записи в системе 1С: Номенклатура, Характеристика, СтранаПроисхождения, Серия, Упаковка, СтавкаНДС, ДокументОтгрузки, НомерГТД, ЕдиницаИзмерения
