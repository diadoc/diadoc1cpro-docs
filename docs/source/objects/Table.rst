
Table
=====

Сведения таблицы счета-фактуры (содержание факта хозяйственной жизни 2 - наименование и другая информация об отгруженных товарах (выполненных работах, оказанных услугах), о переданных имущественных правах `(ТаблСчФакт) <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239700>`_

.. rubric:: Свойства

:TotalWithVatExcluded:
  **Число (19,2)** - всего к оплате, стоимость товаров (работ, услуг), имущественных прав без налога - всего [`СтТовБезНДСВсего <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239703>`_]

:Total:
  **Число (19,2)** - всего к оплате, стоимость товаров (работ, услуг), имущественных прав с налогом - всего [`СтТовУчНалВсего <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239708>`_].Если значение не заполнено, то будет установлено значение "-" в поле [`ДефСтТовУчНалВсего <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239712>`_]

:HyphenTotal:
  **Булево** - признак того, что всего к оплате, стоимость товаров (работ, услуг), имущественных прав с налогом не указана. Если Истина, то будет указано значение "-" в поле [`ДефСтТовУчНалВсего <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239712>`_]

:TotalNet:
  **Число (26,11)** - количество (масса нетто/количество) - всего по документу [`КолНеттоВс <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239717>`_]

:Vat:
  **Число (19,2)** - всего к оплате, сумма налога, предъявляемая покупателю [`СумНалВсего <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239715>`_].

:HyphenVat:
  **Булево** - признак того, что всего к оплате, сумма налога, предъявляемая покупателю не указана. Если Истина, то будет указано значение "-" в поле [`ДефНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239719>`_]

:WithoutVat:
  **Строка** - принимает значение либо "false", либо "true". Используется для заполнения [`СумНалВсего <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239715>`_].
  Если указано значение "true", тогда будет заполнено [`БезНДС <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239711>`_]

:Items:
  **Коллекция** :doc:`Item <../../objects/Item>` - сведения об отгруженных товарах (о выполненных работах, оказанных услугах), переданных имущественных правах [`СведТов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239720>`_]
