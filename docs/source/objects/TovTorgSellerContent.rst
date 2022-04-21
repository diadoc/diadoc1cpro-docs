TovTorgSellerContent
=======================

Содержание титула продавца файла обмена о передаче товара в формате приказа `ММВ-7-10/551@ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5636962>`_

.. rubric:: Свойства

:AdditionalInfoId:
  **Структура** :doc:`AdditionalInfoId <../../objects/551@/AdditionalInfoId>` — информационное поле документа [`ИнфПолФХЖ1 <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5930676>`_]

:Buyer\*:
  **Структура** :doc:`ExtendedOrganizationInfo <../../objects/551@/ExtendedOrganizationInfo>` — сведения о покупателе [`Покупатель <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5704143>`_]

:Carrier:
  **Структура** :doc:`ExtendedOrganizationInfo <../../objects/551@/ExtendedOrganizationInfo>` — сведения о перевозчике [`Перевозчик <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5704232>`_]

:Consignee:
  **Структура** :doc:`ExtendedOrganizationInfo <../../objects/551@/ExtendedOrganizationInfo>` — сведения о грузополучателе [`ГрузПолуч <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5704210>`_]

:Currency\*:
  **Строка (=3)** — код валюты [`КодОКВ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5636967>`_]

:CurrencyRate:
  **Число (10.4)** — курс валюты [`КурсВал <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5636969>`_]

:DocumentCreator\*:
  **Строка (1-1000)** — составитель информации продавца [`НаимЭконСубСост <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5610491>`_]

:DocumentCreatorBase:
  **Строка (1-120)** — основание, по которому экономический субъект является составителем информации продавца [`ОснДоверОргСост <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5610499>`_]. Обязателен, если составитель информации продавца не является продавцом

:DocumentDate\*:
  **Дата (ДД.ММ.ГГГГ)** — дата составления документа о передаче товара [`ДатаДокПТ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5610684>`_]

:DocumentName\*:
  **Строка (1-255)** — наименование первичного документа, определенное организацией [`НаимДокОпр <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5610681>`_]

:DocumentNumber:
  **Строка (1-255)** — номер документа о передаче товара [`НомДокПТ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5610688>`_]

:GovernmentContractInfo:
  **Строка (1-255)** — идентификатор государственного контракта [`ИдГосКон <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5704647>`_]

:Grounds\*:
  **Коллекция** :doc:`GroundInfo <../../objects/551@/GroundInfo>` — основание факта хозяйственной жизни [`Основание <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5704508>`_]

:OperationType:
  **Строка (1-255)** — вид операции, определяющий в каком порядке использовать информацию документа у продавца [`ВидОперации <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5704630>`_]

:RevisionDate\*:
  **Дата (ДД.ММ.ГГГГ)** — дата исправления документа о передаче товара [`ДатаИспрДокПТ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5636966>`_]

:RevisionNumber\*:
  **Число (3)** — номер исправления документа о передаче товара [`НомИспрДокПТ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5704569>`_]

:Seller\*:
  **Структура** :doc:`ExtendedOrganizationInfo <../../objects/551@/ExtendedOrganizationInfo>` — сведения о продавце [`Продавец <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5704126>`_]

:Shipper:
  **Структура** :doc:`ExtendedOrganizationInfo <../../objects/551@/ExtendedOrganizationInfo>` — сведения о грузоотправителе [`ГрузОтпр <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5704193>`_]

:Signers\*:
  **Коллекция** :doc:`ExtendedSigner <../../objects/551@/ExtendedSigner>` — подписанты документа [`Подписант <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5995885>`_]

:Table\*:
  **Структура** :doc:`TovTorgTable <../../objects/551@/TovTorgTable>` — сведения об ассортименте, количестве, стоимости и другой информации о товарных позициях [`СодФХЖ2 <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5704677>`_]

:TransferInfo\*:
  **Структура** :doc:`TovTorgTransferInfo <../../objects/551@/TovTorgTransferInfo>` — сведения о факте передачи товара [`СодФХЖ3 <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5636971>`_]


\*обязательные поля