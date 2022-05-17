TovTorgTransferInfo
====================

Содержание факта хозяйственной жизни (3) — сведения о факте передачи `(СодФХЖ3) <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637282>`_

.. rubric:: Свойства

:Attachment:
  **Строка (1-255)** — количество листов приложения: паспорт, сертификат и т.д. [`КолПрил <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637284>`_]

:Employee:
  **Структура** :doc:`Employee <../../objects/551@/Employee>` — сведения о лице, передавшем товар [`СвЛицОтпГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637285>`_]. Обязателен, если лицо, отпустившее груз, не совпадает с лицом, ответственным за оформление факта хозяйственной жизни

:OperationInfo\*:
  **Строка (1-255)** — содержание операции [`СодОпер <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637288>`_]

:OtherIssuer\*:
 **Структура** :doc:`OtherIssuer <../../objects/551@/OtherIssuer>` — представитель организации или физическое лицо, которому доверена передача товара [`ИнЛицо <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637292>`_]

:StructedAdditionalInfos:
  **Коллекция** :doc:`AdditionalInfoItem <../../objects/551@/AdditionalInfoItem>` — информационное поле факта хозяйственной жизни (3) [`ИнфПолФХЖ3 <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637283>`_]

:TransferDate:
  **Дата (ДД.ММ.ГГГГ)** — дата отпуска груза [`ДатаОтпуск <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637286>`_]. Обязателен, если `ДатаОтпуск <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637286>`_ не совпадает с `ДатаДокПТ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5995900>`_

:Waybills:
  **Коллекция** :doc:`Waybills <../../objects/551@/Waybills>` — транспортная накладная [`ТранНакл <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637287>`_]


\*обязательные поля