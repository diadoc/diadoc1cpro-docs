
CustomDeclaration
=================

Сведения о таможенной декларации `(СвТД) <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239768>`_

.. rubric:: Свойства

:CountryCode:
  **Строка (=3)** - цифровой код страны происхождения товара [`КодПроисх <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239769>`_]. Если значение не заполнено, то будет установлено значение "-" в поле [`ДефКодПроисх <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239771>`_]

:HyphenCountry:
  **Булево** - признак того, что цифровой код страны отсутствует. Если Истина, то будет установлено значение "-" в поле [`ДефКодПроисх <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239771>`_]

:DeclarationNumber:
  **Строка (1-29)** - регистрационный номер таможенной декларации  [`НомерТД <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239770>`_]
