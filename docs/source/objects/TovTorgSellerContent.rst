TovTorgSellerContent
=======================

Содержание титула продавца файла обмена о передаче товара в формате приказа `ММВ-7-10/551@ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5636962>`_

.. rubric:: Свойства

:Currency\*:
  **Строка (=3)** — код валюты [`КодОКВ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5636967>`_]

:CurrencyRate:
  **Число (10.4)** — курс валюты [`КурсВал <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5636969>`_]

:DocumentCreator\*:
  **Строка (1-1000)** — наименование экономического субъекта - составителя информации продавца [`НаимЭконСубСост <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5610491>`_]

:DocumentCreatorBase:
  **Строка (1-120)** — основание, по которому экономический субъект является составителем информации продавца [`ОснДоверОргСост <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5610499>`_]. Обязательно, если составитель информации продавца не является продавцом

:DocumentDate\*:
  **Дата (ДД.ММ.ГГГГ)** — дата составления документа о передаче товара [`ДатаДокПТ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5610684>`_]

:DocumentName:
  **Строка (1-255)** — наименование первичного документа, определенное организацией[`НаимДокОпр <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5610681>`_]

:DocumentNumber\*:
  **Строка (1-255)** — номер документа о передаче товара [`НомДокПТ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5610688>`_]

:ExtendedSignerDetails\*:
  **Коллекция** :doc:`ExtendedSignerDetails <../../objects/551@/ExtendedSignerDetails>` — сведения о лице, подписавшем информацию продавца в электронном виде [`Подписант <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637601>`_]

:RevisionDate\*:
  **Дата (ДД.ММ.ГГГГ)** — дата исправления документа о передаче товара [`ДатаИспрДокПТ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5636966>`_]

:TovTorgTransferInfo\*:
  :doc:`TovTorgTransferInfo <../../objects/551@/TovTorgTransferInfo>` — содержание факта хозяйственной жизни (3) — сведения о факте передачи [`СодФХЖ3 <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5636971>`_]
