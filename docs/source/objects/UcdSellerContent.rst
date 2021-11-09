
Титул продавца UcdSellerContent
===============================

Содержание титула продавца *Универсального корректировочного документа* в формате приказа `ЕД-7-26/736@ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857#h546>`_

.. rubric:: Свойства

:Function:
  **Строка** — функция (Invoice/InvoiceAndBasic/Basic) [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611043>`_]

:Name:
  **Строка (1-255)** — наименование документа, определенное организацией (согласованное сторонами сделки) [`НаимДокОпр <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611044>`_]

:Date:
  **Дата (ДД.ММ.ГГГГ)** — дата составления (выписки) корректировочного счета-фактуры и (или) документа о согласии покупателя на изменение стоимости отгрузки [`ДатаКСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611121>`_]

:Number:
  **Строка (1-1000)** — порядковый номер корректировочного счета-фактуры и (или) документа о согласии покупателя на изменение стоимости отгрузки [`НомерКСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611122>`_]

:Currency:
  **Строка (=3)** — код валюты [`КодОКВ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611123>`_]

:CurrencyRate:
  **Строка** — курс валюты [`КурсВал <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611124>`_]

:CurrencyName:
  **Строка** — наименование валюты [`НаимОКВ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611125>`_]

:RevisionDate:
  **Дата (ДД.ММ.ГГГГ)** — дата исправления [`ДатаИспрКСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611126>`_]

:RevisionNumber:
  **Строка (1-256)** — номер исправления [`НомИспрКСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611127>`_]

:Creator:
  **Строка (1-1000)** — составителя файла обмена корректировочного счета-фактуры с дополнительной информацией (информации продавца) [`НаимЭконСубСост <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611128>`_]

:CreatorBase:
  **Строка (1-120)** — основание, по которому экономический субъект является составителем файла обмена корректировочного счета-фактуры с дополнительной информацией (информации продавца) [`ОснДоверОргСост <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611129>`_]

:GovernmentContractInfo:
  **Строка (20-25)** — идентификатор государственного контракта, договора [`ИдГосКон <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611130>`_]

:Seller:
  :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo>` — сведения о продавце [`СвПрод <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611131>`_]

:Buyer:
  :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo>` — сведения о покупателе [`СвПокуп <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611132>`_]

:Signers:
  **Коллекция** :doc:`ExtendedSigner <../../objects/ExtendedSigner>` — сведения о лице, подписывающем файл обмена корректировочного счета- фактуры с дополнительной информацией (информации продавца) в электронной форме [`Подписант <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611133>`_]

:InvoiceCorrectionTable:
  :doc:`InvoiceCorrectionTable <../../objects/InvoiceCorrectionTable>` — сведения таблицы корректировочного счета-фактуры с дополнительной информацией  [`ТаблКСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611134>`_]

:Invoices:
  **Коллекция** :doc:`InvoiceForCorrectionInfo <../../objects/InvoiceForCorrectionInfo>` — документ, к которому составлен корректировочный счет-фактура  [`СчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611135>`_]

:EventContent:
  :doc:`EventContent <../../objects/EventContent>` — сведения о факте согласования (уведомления)  [`СодФХЖ3 <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611136>`_]

:AdditionalInfoId:
  :doc:`AdditionalInfoId <../../objects/AdditionalInfoId>` — информационное поле события [`ИнфПолФХЖ1 <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611137>`_]
