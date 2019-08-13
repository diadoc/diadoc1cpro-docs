
Типы документов
===============

Поддерживаются следующие типы документов:

* **XmlTorg12** - товарная накладная ТОРГ-12 в XML-формате
* **XmlAcceptanceCertificate** - акт о выполнении работ / оказании услуг в XML-формате
* **Invoice** - счет-фактура
* **InvoiceRevision** - исправление счета-фактуры
* **InvoiceCorrection** - корректировочный счет-фактура
* **InvoiceCorrectionRevision** - исправление корректировочного счета-фактуры
* **UniversalTransferDocument** - универсальный передаточный документ
* **UniversalTransferDocumentRevision** - универсальный передаточный документ (исправление)
* **UniversalCorrectionDocument** - универсальный корректировочный документ
* **UniversalCorrectionDocumentRevision** - универсальный корректировочный документ (исправление)
* **ProformaInvoice** - счет на оплату
* **Nonformalized** - неформализованный документ
* **TrustConnectionRequest** - запрос на инициацию канала обмена документами через Диадок
* **Torg12** - товарная накладная ТОРГ-12 (неформализованная)
* **AcceptanceCertificate** - акт о выполении работ / оказании услуг (неформализованный)
* **PriceList** - ценовой лист
* **PriceListAgreement** - протокол согласования цены
* **CertificateRegistry** - реестр сертификатов
* **ReconciliationAct** - акт сверки
* **Contract** - договор
* **Torg13** - накладная ТОРГ-13
* **ServiceDetails** - детализация
* **SupplementaryAgreement** - дополнительное соглашение к договору
* **MesNotification** - уведомление о переходе на ЭДО
* **StorageInventoryAcceptanceCertificate** - акт МХ-1
* **ReturnInventoryAcceptanceCertificate** - акт МХ-3
* **Torg1** - акт о приемке товаров ТОРГ-1
* **Torg2** - акт об установленном расхождении ТОРГ-2
* **ForwarderAssignment** - поручение экспедитору
* **PerformedWorkAcceptanceCertificate** - акт приемки выполненных работ КС-2
* **PerformedWorkCostCertificate** - справка о стоимости выполненных работ и затрат КС-3

Список настраивается для конкретного ящика. Доступные типы вернет метод API `GetDocumentTypes <http://api-docs.diadoc.ru/ru/latest/http/GetDocumentTypes.html>`_

Автоматическая загрузка таких типов документов происходит при синхронизации организаций или контрагентов.

Сохраняются в справочник "Диадок_ДополнительныеСправочники" с именем справочника "ТипыДокументовAPI".
