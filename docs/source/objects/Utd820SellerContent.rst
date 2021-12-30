
Титул продавца Utd820SellerContent
==================================
 
Содержание титула продавца *Универсального передаточного документа* в формате приказа `ММВ-7-15/820@ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588#h344>`_
 
.. rubric:: Свойства
 
:AdditionalInfoId:
  :doc:`AdditionalInfoId <../../objects/AdditionalInfoId>` — информационное поле документа [`ИнфПолФХЖ1 <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239671>`_]
 
:ApprovedStructureAdditionalInfoFields:
  **Строка (=14)** — информация о наличии согласованной структуры дополнительных информационных полей [`СоглСтрДопИнф <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239649>`_]
 
:Buyers\*:
  **Коллекция** :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo820>` — сведения о покупателе [`СвПокуп <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239665>`_]
 
:CircumFormatInvoice:
  **Строка (=1)** — обстоятельства формирования счета-фактуры, применяемого при расчетах по налогу на добавленную стоимость [`ОбстФормСЧФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239661>`_]
 
:Consignees:
  **Коллекция** :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo820>` — грузополучатель и его адрес [`ГрузПолуч <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239667>`_]

:Currency\*:
  **Строка (=3)** — код валюты [`КодОКВ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239653>`_]

:CurrencyRate:
  **Строка** — курс валюты [`КурсВал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239655>`_]

:DocumentCreator\*:
  **Строка (1-1000)** — составитель файла обмена счета-фактуры (информации продавца) [`НаимЭконСубСост <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239658>`_]

:DocumentCreatorBase:
  **Строка (1-120)** — основание, по которому экономический субъект является составителем файла обмена счета-фактуры (информации продавца) [`ОснДоверОргСост <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239659>`_]. Обязательно, если составитель информации продавца не является продавцом

:DocumentDate\*:
  **Дата (ДД.ММ.ГГГГ)** — дата составления (выписки) счета-фактуры [`ДатаСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239651>`_]

:DocumentName:
  **Строка (1-255)** — наименование первичного документа, определенное организацией [`НаимДокОпр <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239648>`_]

:DocumentNumber\*:
  **Строка (1-1000)** — порядковый номер счета-фактуры [`НомерСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239652>`_]

:DocumentShipments:
  **Коллекция** :doc:`DocumentShipment <../../objects/DocumentShipment>` — реквизиты документа, подтверждающего отгрузку товаров (работ, услуг, имущественных прав) [`ДокПодтвОтгр <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239682>`_]

:FactorInfo:
  :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo820>` — сведения о факторе [`СвФактор <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239678>`_]

:Function\*:
  **Строка (1-6)** — функция (СЧФ/СЧФДОП/ДОП) [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239646>`_]

:GovernmentContractInfo:
  **Строка (20-25)** — идентификатор государственного контракта, договора [`ИдГосКон <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239660>`_]. Обязателен при наличии государственного контракта на поставку товаров (выполнение работ, оказание услуг), договора о предоставлении из федерального бюджета юридическому лицу субсидий, бюджетных инвестиций, взносов в уставный капитал.

:HyphenRevisionDate:
  **Булево** — признак того, что в графе "Исправление" не указана дата исправленного счета-фактуры. Если Истина, то будет указано значение "-" в поле [`ДефДатаИспрСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=318899>`_]. Обязателен при отсутствии [`ДатаИспрСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427373>`__]

:HyphenRevisionNumber:
  **Булево** — признак того, что в графе "Исправление" не указан номер исправленного счета-фактуры. Если Истина, то будет указано значение "-" в поле [`ДефНомИспрСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=318900>`__]. Обязателен при отсутствии [`НомИспрСЧФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427375>`__]

:MainAssignMonetaryClaim:
  :doc:`TransferBase <../../objects/TransferBase820>` — основание уступки денежного требования [`ОснУстДенТреб <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239679>`_]

:PaymentDocuments:
  **Коллекция** :doc:`PaymentDocumentInfo <../../objects/PaymentDocumentInfo>` — сведения о платежно-расчетном документе [`СвПРД <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239669>`_]

:RevisionDate:
  **Дата (ДД.ММ.ГГГГ)** — дата исправления [`ДатаИспрСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239656>`_]. Обязательна при отсутствии [`ДефДатаИспр <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427381>`_]


:RevisionNumber:
  **Число (3)** — номер исправления [`НомИспрСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239657>`_]. Обязателен при отсутствии [`ДефНомИспрСЧФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427384>`_]

:SellerInfoCircumPublicProc:
  :doc:`SellerInfoCircumPublicProc <../../objects/SellerInfoCircumPublicProc>` — информация продавца об обстоятельствах закупок для государственных и муниципальных нужд [`ИнфПродГосЗакКазн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239681>`_]. Обязательна при осуществлении закупок для обеспечения государственных и муниципальных нужд и для учета Федеральным казначейством денежных обязательств
  
:Sellers\*:
  **Коллекция** :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo820>` — сведения о продавце [`СвПрод <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239664>`_]


:Shippers:
  **Коллекция** :doc:`Shipper <../../objects/Shipper820>` — сведения о грузоотправителе [`ГрузОт <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239666>`_]


:Signers\*:
  **Коллекция** :doc:`ExtendedSigner <../../objects/ExtendedSigner>` — подписанты документа [`Подписант <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239668>`_]

:Table:
  :doc:`Table <../../objects/InvoiceTable820>` — сведения таблицы счета-фактуры  [`ТаблСчФакт <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239676>`_]. Обязательны при [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239646>`_] = СЧФ или [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239646>`_ ]= СЧФДОП

:TransferInfo\*:
  :doc:`TransferInfo <../../objects/TransferInfo820>` — сведения о передаче (сдаче) [`СвПер <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239677>`_]


\*обязательные поля