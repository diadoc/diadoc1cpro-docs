
Титул продавца Utd820SellerContent
==================================

Содержание титула продавца *Универсального передаточного документа* в формате приказа `ММВ-7-15/820@ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588#h344>`_

.. rubric:: Свойства

:Function:
  **Строка (1-6)** - функция (СЧФ/СЧФДОП/ДОП) [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239646>`_]

:ApprovedStructureAdditionalInfoFields:
  **Строка (=14)** - информация о наличии согласованной структуры дополнительных информационных полей [`СоглСтрДопИнф <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239649>`_]

:DocumentName:
  **Строка (1-255)** - наименование первичного документа, определенное организацией [`НаимДокОпр <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239648>`_]

:DocumentDate:
  **Дата (ДД.ММ.ГГГГ)** - дата составления (выписки) счета-фактуры [`ДатаСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239651>`_]

:DocumentNumber:
  **Строка (1-1000)** - порядковый номер счета-фактуры [`НомерСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239652>`_]

:Currency:
  **Строка (=3)** - код валюты [`КодОКВ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239653>`_]

:CurrencyRate:
  **Строка** - курс валюты [`КурсВал <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239655>`_]

:RevisionDate:
  **Дата (ДД.ММ.ГГГГ)** - дата исправления [`ДатаИспрСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239656>`_]

:HyphenRevisionDate:
  **Булево** - признак того, что в графе "Исправление" не указана дата исправленного счета-фактуры. Если Истина, то будет указано значение "-" в поле [`ДефДатаИспрСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=318899>`_]

:RevisionNumber:
  **Число (3)** - номер исправления [`НомИспрСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239657>`_]

:HyphenRevisionNumber:
  **Булево** - признак того, что в графе "Исправление" не указан номер исправленного счета-фактуры. Если Истина, то будет указано значение "-" в поле [`ДефНомИспрСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=318900>`_]

:DocumentCreator:
  **Строка (1-1000)** - составитель файла обмена счета-фактуры (информации продавца) [`НаимЭконСубСост <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239658>`_]

:DocumentCreatorBase:
  **Строка (1-120)** - основание, по которому экономический субъект является составителем файла обмена счета-фактуры (информации продавца) [`ОснДоверОргСост <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239659>`_]

:GovernmentContractInfo:
  **Строка (20-25)** - Идентификатор государственного контракта, договора [`ИдГосКон <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239660>`_]

:CircumFormatInvoice:
  **Строка (=1)** - обстоятельства формирования счета-фактуры, применяемого при расчетах по налогу на добавленную стоимость [`ОбстФормСЧФ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239661>`_]

:Sellers:
  **Коллекция** :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo>` - сведения о продавце [`СвПрод <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239664>`_]

:Buyers:
  **Коллекция** :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo>` - сведения о покупателе [`СвПокуп <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239665>`_]

:Shippers:
  **Коллекция** :doc:`Shipper <../../objects/Shipper>` - сведения о грузоотправителе [`ГрузОт <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239666>`_]

:Consignees:
  **Коллекция** :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo>` - грузополучатель и его адрес [`ГрузПолуч <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239667>`_]

:Signers:
  **Коллекция** :doc:`ExtendedSigner <../../objects/ExtendedSigner>` - подписанты документа [`Подписант <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239668>`_]

:PaymentDocuments:
  **Коллекция** :doc:`PaymentDocumentInfo <../../objects/PaymentDocumentInfo>` - сведения о платежно-расчетном документе [`СвПРД <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239669>`_]

:AdditionalInfoId:
  :doc:`AdditionalInfoId <../../objects/AdditionalInfoId>` - информационное поле документа [`ИнфПолФХЖ1 <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239671>`_]

:Table:
  :doc:`Table <../../objects/Table>` - сведения таблицы счета-фактуры  [`ТаблСчФакт <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239676>`_]

:TransferInfo:
  :doc:`TransferInfo <../../objects/TransferInfo>` - сведения о передаче (сдаче) [`СвПер <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239677>`_]

:FactorInfo:
  :doc:`ExtendedOrganizationInfo <../../objects/ExtendedOrganizationInfo>` - сведения о факторе [`СвФактор <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239678>`_]

:MainAssignMonetaryClaim:
  :doc:`TransferBase <../../objects/TransferBase>` - основание уступки денежного требования [`ОснУстДенТреб <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239679>`_]

:SellerInfoCircumPublicProc:
  :doc:`SellerInfoCircumPublicProc <../../objects/SellerInfoCircumPublicProc>` - информация продавца об обстоятельствах закупок для государственных и муниципальных нужд [`ИнфПродГосЗакКазн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239681>`_]

:DocumentShipments:
  **Коллекция** :doc:`DocumentShipment <../../objects/DocumentShipment>` - реквизиты документа, подтверждающего отгрузку товаров (работ, услуг, имущественных прав) [`ДокПодтвОтгр <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239682>`_]
