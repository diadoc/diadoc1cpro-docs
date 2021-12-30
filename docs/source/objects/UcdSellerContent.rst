
Титул продавца UcdSellerContent
===============================

Содержание титула продавца *Универсального корректировочного документа* в формате приказа `ЕД-7-26/736@ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857#h546>`_

.. rubric:: Свойства

:AdditionalInfoId:
  **Коллекция** :doc:`AdditionalInfoId <../../objects/AdditionalInfoId736>` — информационное поле события [`ИнфПолФХЖ1 <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611137>`_]

:Buyer:
  **Коллекция** :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo>` — сведения о покупателе [`СвПокуп <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611132>`_]

:Creator:
  **Строка (1-1000)** — наименование экономического субъекта - составителя файла обмена корректировочного счета-фактуры с дополнительной информацией (информации продавца) [`НаимЭконСубСост <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611128>`_]

:CreatorBase:
  **Строка (1-120)** — основание, по которому экономический субъект является составителем файла обмена корректировочного счета-фактуры с дополнительной информацией (информации продавца) [`ОснДоверОргСост <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611129>`_]

:Currency:
  **Строка (=3)** — код валюты [`КодОКВ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611123>`_]

:CurrencyName:
  **Строка (1-100)** — наименование валюты [`НаимОКВ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611125>`_]

:CurrencyRate:
  **Число (10.4)** — курс валюты [`КурсВал <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611124>`_]

:Date:
  **Дата (ДД.ММ.ГГГГ)** — дата составления (выписки) корректировочного счета-фактуры и (или) документа о согласии покупателя на изменение стоимости отгрузки [`ДатаКСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611121>`_]

:EventContent:
  **Коллекция** :doc:`EventContent <../../objects/EventContent>` — сведения о факте согласования (уведомления)  [`СодФХЖ3 <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611136>`_]

:Function:
  **Строка (3-7)** — функция (|UсdSellerContent-Function|_) [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611043>`_]

:GovernmentContractInfo:
  **Строка (20-25)** — идентификатор государственного контракта [`ИдГосКон <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611130>`_]

:InvoiceCorrectionTable:
  **Коллекция** :doc:`InvoiceCorrectionTable <../../objects/InvoiceCorrectionTable>` — сведения таблицы корректировочного счета-фактуры с дополнительной информацией  [`ТаблКСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611134>`_]

:Invoices:
  **Коллекция** :doc:`InvoiceForCorrectionInfo <../../objects/InvoiceForCorrectionInfo>` — документ, к которому составлен корректировочный счет-фактура  [`СчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611135>`_]

:Name:
  **Строка (1-255)** — наименование документа, определенное организацией (согласованное сторонами сделки) [`НаимДокОпр <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611044>`_]

:Number:
  **Строка (1-1000)** — порядковый номер корректировочного счета-фактуры и (или) документа о согласии покупателя на изменение стоимости отгрузки [`НомерКСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611122>`_]

:RevisionDate:
  **Дата (ДД.ММ.ГГГГ)** — дата исправления [`ДатаИспрКСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611126>`_]

:RevisionNumber:
  **Число (3)** — номер исправления [`НомИспрКСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611127>`_]

:Seller:
  **Коллекция** :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo>` — сведения о продавце [`СвПрод <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611131>`_]

:Signers:
  **Коллекция** :doc:`ExtendedSigner <../../objects/ExtendedSigner>` — сведения о лице, подписывающем файл обмена корректировочного счета-фактуры с дополнительной информацией (информации продавца) в электронной форме [`Подписант <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611133>`_]


.. rubric:: Дополнительная информация

.. |UсdSellerContent-Function| replace:: Возможные значения
.. _UсdSellerContent-Function:

===================== ===========================================================================================================================
Значение *Function*   Описание
===================== ===========================================================================================================================
Basic                 документ, подтверждающий согласие (факт уведомления) покупателя на изменение стоимости отгруженных товаров (выполненных работ, оказанных услуг), переданных имущественных прав [`ДИС <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2967590>`_]
Invoice               корректировочный счет-фактура, применяемый при расчетах по налогу на добавленную стоимость; [`КСЧФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2967591>`_]
InvoiceAndBasic       корректировочный счет-фактура, применяемый при расчетах по налогу на добавленную стоимость, и документ, подтверждающий согласие (факт уведомления) покупателя на изменение стоимости отгруженных товаров (выполненных работ, оказанных услуг), переданных имущественных прав [`КСЧФДИС <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2967594>`_]
===================== ===========================================================================================================================