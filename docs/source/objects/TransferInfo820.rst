
TransferInfo
============

Сведения о передаче (сдаче) товаров (результатов работ), имущественных прав (о предъявлении оказанных услуг) `(СвПер) <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239791>`_

.. rubric:: Свойства

:OperationInfo:
  **Строка (1-255)** — содержание операции [`СодОпер <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239831>`_]

:OperationType:
  **Строка (1-255)** — вид операции [`ВидОпер <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239832>`_]

:TransferDate:
  **Дата (ДД.ММ.ГГГГ)** — дата отгрузки товаров (передачи результатов работ), передачи имущественных прав (предъявления оказанных услуг) [`ДатаПер <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239833>`_]

:TransferTextInfo:
  **Строка (1-1000)** — сведения о транспортировке и грузе [`СвТранГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239843>`_]

:Carrier:
  :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo820>` — перевозчик [`Перевозчик <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239834>`_]

:Employee:
  :doc:`Employee <../../objects/Employee>` — работник организации продавца [`РабОргПрод <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239835>`_]

:OtherIssuer:
  :doc:`OtherIssuer <../../objects/OtherIssuer>` — иное лицо [`ИнЛицо <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239836>`_]

:CreatedThingTransferDate:
  **Дата (ДД.ММ.ГГГГ)** — дата передачи вещи, изготовленной по договору подряда [`ДатаПерВещ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239833>`_]

:CreatedThingInfo:
  **Строка** — сведения о передаче [`СвПерВещ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239837>`_]

:AdditionalInfoId:
  :doc:`AdditionalInfoId <../../objects/AdditionalInfoId>` — информационное поле факта хозяйственной жизни 3 [`ИнфПолФХЖЗ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239844>`_]

:TransferBases:
  **Коллекция** :doc:`TransferBase <../../objects/TransferBase>` — основание отгрузки товаров (передачи результатов работ), передачи имущественных прав (предъявления оказанных услуг) [`ОснПер <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239845>`_]

:Waybills:
  **Коллекция** :doc:`Waybill <../../objects/Waybill>` — транспортная накладная [`ТранНакл <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239846>`_]

:TransferStartDate:
  **Дата (ДД.ММ.ГГГГ)** — дата начала периода оказания услуг (выполнения работ, поставки товаров) [`ДатаНач <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239793>`_]

:TransferEndDate:
  **Дата (ДД.ММ.ГГГГ)** — дата окончания периода оказания услуг (выполнения работ, поставки товаров) [`ДатаОкон <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239794>`_]
