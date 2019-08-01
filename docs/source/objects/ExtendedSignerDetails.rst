
ExtendedSignerDetails
=====================

Сведения о лице, подписывающем файл обмена счета-фактуры в электронной форме `(Подписант) <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242170>`_

.. rubric:: Свойства

:Surname:
  **Строка (1-60)** - фамилия [`Фамилия <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239858>`_]

:FirstName:
  **Строка (1-60)** - имя [`Имя <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239860>`_]

:Patronymic:
  **Строка (1-60)** - отчество [`Отчество <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239859>`_]

:JobTitle:
  **Строка (1-128)** - должность [`Должн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242173>`_]

:Inn:
  **Строка (10-12)** - ИНН юридического лица или индивидуального предпринимателя [`ИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242174>`_]/[`ИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242177>`_]

:RegistrationCertificate:
  **Строка** - реквизиты свидетельства о государственной регистрации индивидуального предпринимателя, выдавшего доверенность организации на подписание счета-фактуры [`ГосРегИПВыдДов <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242178>`_]

:SignerType:
  **Строка** - тип подписанта |ExtendedSignerDetails-SignerType|_

:OrganizationName:
  **Строка (1-1000)** - наименование организации [`НаимОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242182>`_]

:SignerInfo:
  **Строка (1-255)** - иные сведения, идентифицирующие физическое лицо [`ИныеСвед <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242183>`_]

:Powers:
  **Строка** - область полномочий |ExtendedSignerDetails-Powers|_ [`ОблПолн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242185>`_].

:Status:
  **Строка** - статус |ExtendedSignerDetails-Status|_ [`Статус <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242186>`_].

:PowersBase:
  **Строка (1-255)** - основания полномочий (доверия) [`ОснПолн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242187>`_]

:OrganizationPowersBase:
  **Строка (1-255)** - основания полномочий (доверия) организации [`ОснПолнОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242188>`_]


.. rubric:: Дополнительная информация

.. |ExtendedSignerDetails-SignerType| replace:: Возможные значения
.. _ExtendedSignerDetails-SignerType:

===================== ===========================================================================================================================
Значение *SignerType* Описание
===================== ===========================================================================================================================
LegalEntity           представитель юридического лица ([`ЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242181>`_])
IndividualEntity      индивидуальный предприниматель ([`ИП <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242180>`_])
PhysicalPerson        физическое лицо ([`ФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=242179>`_])
===================== ===========================================================================================================================

.. |ExtendedSignerDetails-Powers| replace:: Возможные значения
.. _ExtendedSignerDetails-Powers:

============================================== =================================================================================================
Значение *Powers*                              Описание
============================================== =================================================================================================
InvoiceSigner                                  лицо, ответственное за подписание счетов-фактур
PersonMadeOperation                            лицо, совершившее сделку, операцию
MadeAndSignOperation                           лицо, совершившее сделку, операцию и ответственное за её оформление
PersonDocumentedOperation                      лицо, ответственное за оформление свершившегося события
MadeOperationAndSignedInvoice                  лицо, совершившее сделку, операцию и ответственное за подписание счетов-фактур
MadeAndResponsibleForOperationAndSignedInvoice лицо, совершившее сделку, операцию и ответственное за её оформление и за подписание счетов-фактур
ResponsibleForOperationAndSignerForInvoice     лицо, ответственное за оформление свершившегося события и за подписание счетов-фактур
============================================== =================================================================================================

.. |ExtendedSignerDetails-Status| replace:: Возможные значения
.. _ExtendedSignerDetails-Status:

=============================== ==================================================================================================================================================
Значение *Status*               Описание
=============================== ==================================================================================================================================================
SellerEmployee                  работник организации продавца товаров (работ, услуг, имущественных прав)
InformationCreatorEmployee      работник организации - составителя информации продавца
OtherOrganizationEmployee       работник иной уполномоченной организации
AuthorizedPerson                уполномоченное физическое лицо (в том числе индивидуальный предприниматель)
BuyerEmployee                   работник организации покупателя товаров (работ, услуг, имущественных прав)
InformationCreatorBuyerEmployee Работник организации - составителя файла обмена информации покупателя, если составитель файла обмена информации покупателя не является покупателем
=============================== ==================================================================================================================================================
