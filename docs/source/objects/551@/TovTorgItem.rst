TovTorgItem
============

Сведения об ассортименте, количестве, стоимости товара `(СвТовТип) <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5932494>`_

.. rubric:: Свойства

:Feature:
  **Строка (1-1000)** — характеристика товара [`ХарактерТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993862>`_]. Обязателен при отсутствии всех перечисленных элементов: `НаимТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993798>`_, `АртикулТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993866>`_ и `КодТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993811>`_

:Gross:
  **Число (12.3)** — масса с упаковкой [`Брутто <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993860>`_]

:ItemAccountCredit:
  **Строка (=9)** — кредит корреспондирующих счетов [`КорСчКредит <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993857>`_]

:ItemAccountDebit:
  **Строка (=9)** — дебет корреспондирующих счетов [`КорСчДебет <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993856>`_]

:ItemToRelease:
  **Число (26.11)** — количество, которое надлежит отпустить [`НадлОтп <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993853>`_]

:Net\*:
  **Число (26.11)** — переданное количество или масса без упаковки [`НеттоПередано <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993850>`_]

:PackageType:
  **Строка (1-1000)** — вид упаковки товара [`ВидУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993846>`_]

:Price:
  **Число (26.11)** — цена за единицу измерения [`Цена <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993800>`_]

:Product:
  **Строка (1-1000)** — наименование товара (описание выполненных работ, оказанных услуг), имущественных прав [`НаимТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993798>`_]. Обязателен при отсутствии всех перечисленных элементов: `ХарактерТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993862>`_, `АртикулТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993866>`_ и `КодТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993811>`_

:ProductCode:
  **Строка (1-100)** — код товара [`КодТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993811>`_]. Обязателен при отсутствии всех перечисленных элементов: `НаимТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993798>`_, `АртикулТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993866>`_ и `ХарактерТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993862>`_

:Quantity:
  **Число (12)** — количество единиц товара [`КолТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993809>`_]
  
:QuantityInPack:
  **Число (12.3)** — количество мест в 1 упаковке [`Место <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993810>`_]
  
:Sort:
  **Строка (1-10)** — сорт товара [`СортТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993812>`_]

:StructedAdditionalInfos:
  **Коллекция** :doc:`AdditionalInfoItem <../../objects/551@/AdditionalInfoItem>` — информационное поле факта хозяйственной жизни 2 [`ИнфПолФХЖ2 <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993807>`_]

:Subtotal:
 **Число (19.2)** — стоимость с учетом НДС [`СтУчНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993806>`__]

:SubtotalWithVatExcluded:
  **Число (19.2)** — стоимость без учета налога на добавленную стоимость [`СтБезНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993805>`_]. Обязателен при отсутствии `СтУчНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993806>`__
  
:TaxRate:
  **Строка (1-35)** — налоговая ставка [`НалСт <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993804>`_]

:Unit\*:
  **Строка (3-4)** — код единицы измерения [`ОКЕИ_Тов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993803>`__]

:UnitName\*:
  **Строка (1-1000)** — наименование единицы измерения [`НаимЕдИзм <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993802>`_]
  
:Vat:
  **Число (19.2)** — сумма НДС [`СумНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993801>`_]

:VendorCode:
  **Строка (1-50)** — артикул товара [`АртикулТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993866>`_]. Обязателен при отсутствии всех перечисленных элементов: `ХарактерТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993862>`_, `НаимТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993798>`_ и `КодТов <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993811>`_

:СлужебнаяИнформация:
  **Структура с типом элементов Ссылка1С** — ссылки на следующие записи в системе 1С: Номенклатура, Характеристика, СтранаПроисхождения, Серия, Упаковка, СтавкаНДС, ДокументОтгрузки, НомерГТД, ЕдиницаИзмерения


\*обязательные поля