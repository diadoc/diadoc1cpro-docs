
ExtendedSignerDetails
=====================

Сведения о лице, подписывающем файл обмена счета-фактуры в электронной форме `(Подписант) <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242170>`_

.. rubric:: Свойства

:FirstName:
  **Строка (1-60)** — имя [`Имя <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239860>`_]

:Inn:
  **Строка (10-12)** — ИНН юридического лица или индивидуального предпринимателя [`ИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242174>`_]/[`ИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242177>`_]

:JobTitle:
  **Строка (0-128)** — должность [`Должн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242173>`_]

:OrganizationName:
  **Строка (1-1000)** — наименование организации [`НаимОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242182>`_]

:OrganizationPowersBase:
  **Строка (1-255)** — основание полномочий (доверия) организации [`ОснПолнОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242188>`_]

:Patronymic:
  **Строка (1-60)** — отчество [`Отчество <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239859>`_]

:Powers:
  **Строка (1-2)** — область полномочий |ExtendedSignerDetails-Powers|_ [`ОблПолн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242185>`_].

:PowersBase:
  **Строка (1-255)** — основание полномочий (доверия) [`ОснПолн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242187>`_]

:RegistrationCertificate:
  **Строка (1-100)** — реквизиты свидетельства о государственной регистрации индивидуального предпринимателя, выдавшего доверенность организации на подписание счета-фактуры [`ГосРегИПВыдДов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242178>`_]

:SignerInfo:
  **Строка (1-255)** — иные сведения, идентифицирующие физическое лицо [`ИныеСвед <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242183>`_]

:SignerType:
  **Строка** — тип подписанта |ExtendedSignerDetails-SignerType|_

:Status:
  **Строка (1-2)** — статус |ExtendedSignerDetails-Status|_ [`Статус <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242186>`_].

:Surname:
  **Строка (1-60)** — фамилия [`Фамилия <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239858>`_]


.. rubric:: Дополнительная информация

.. |ExtendedSignerDetails-SignerType| replace:: Возможные значения
.. _ExtendedSignerDetails-SignerType:

===================== ===========================================================================================================================
Значение *SignerType* Описание
===================== ===========================================================================================================================
IndividualEntity      индивидуальный предприниматель [`ИП <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242180>`_]
LegalEntity           представитель юридического лица [`ЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242181>`_]
PhysicalPerson        физическое лицо [`ФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242179>`_]
===================== ===========================================================================================================================

.. |ExtendedSignerDetails-Powers| replace:: Возможные значения
.. _ExtendedSignerDetails-Powers:

============================================== =================================================================================================
Значение *Powers*                              Описание
============================================== =================================================================================================
InvoiceSigner                                  лицо, ответственное за подписание счетов-фактур
MadeAndResponsibleForOperationAndSignedInvoice лицо, совершившее сделку, операцию и ответственное за её оформление и за подписание счетов-фактур
MadeAndSignOperation                           лицо, совершившее сделку, операцию и ответственное за её оформление
MadeOperationAndSignedInvoice                  лицо, совершившее сделку, операцию и ответственное за подписание счетов-фактур
PersonDocumentedOperation                      лицо, ответственное за оформление свершившегося события
PersonMadeOperation                            лицо, совершившее сделку, операцию
ResponsibleForOperationAndSignerForInvoice     лицо, ответственное за оформление свершившегося события и за подписание счетов-фактур
============================================== =================================================================================================

.. |ExtendedSignerDetails-Status| replace:: Возможные значения
.. _ExtendedSignerDetails-Status:

=============================== ==================================================================================================================================================
Значение *Status*               Описание
=============================== ==================================================================================================================================================
AuthorizedPerson                уполномоченное физическое лицо (в том числе индивидуальный предприниматель)
BuyerEmployee                   работник организации покупателя товаров (работ, услуг, имущественных прав)
InformationCreatorBuyerEmployee работник организации - составителя файла обмена информации покупателя, если составитель файла обмена информации покупателя не является покупателем
InformationCreatorEmployee      работник организации - составителя информации продавца
OtherOrganizationEmployee       работник иной уполномоченной организации
SellerEmployee                  работник организации продавца товаров (работ, услуг, имущественных прав)
=============================== ==================================================================================================================================================
