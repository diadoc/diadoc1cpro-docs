TovTorgBuyerContent
=======================

Содержание титула покупателя *Файла обмена документа о передаче товара* в формате приказа `ММВ-7-10/551@ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5994122>`_

.. rubric:: Свойства

:AcceptanceDate:
  **Дата (ДД.ММ.ГГГГ)** — дата принятия товара [`ДатаПолуч <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5997409>`_]. Обязателен, если дата получения груза не совпадает с датой составления документа

:AdditionalInfo:
  **Структура** :doc:`AdditionalInfoId <../../objects/551@/AdditionalInfoId>` — информация покупателя [`ИнфПолФХЖ4 <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5995853>`_]

:DocumentCreator\*:
  **Строка (1-1000)** —  составитель файла информации покупателя [`НаимЭконСубСост <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5994125>`_]

:DocumentCreatorBase:
  **Строка (1-120)** — основание, по которому экономический субъект является составителем информации покупателя [`ОснДоверОргСост <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5994126>`_]. Обязателен, если составитель информации покупателя не является покупателем

:Employee:
  **Структура** :doc:`Employee <../../objects/551@/Employee>` — сведения о лице, передавшем товар [`СвЛицОтпГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637285>`_]. Обязателен, если лицо, отпустившее груз, не совпадает с лицом, ответственным за оформление факта хозяйственной жизни

:OperationCode:
  **Строка (1-255)** — вид операции, определяющий в каком порядке использовать информацию документа у продавца [`ВидОперации <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995645>`_]

:OperationContent\*:
  **Строка (1-1000)** — содержание операции [`СодОпер <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5995644>`_]

:OtherIssuer\*:
  **Структура** :doc:`OtherIssuer <../../objects/551@/OtherIssuer>` — иное лицо, которому доверена передача груза [`ИнЛицо <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5995887>`_]

:Signers\*:
  **Коллекция** :doc:`ExtendedSigner <../../objects/551@/ExtendedSigner>` — подписанты документа [`Подписант <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5994128>`_]


\*обязательные поля