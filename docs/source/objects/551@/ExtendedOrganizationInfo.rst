ExtendedOrganizationInfo
=========================

Сведения об участнике факта хозяйственной жизни `(УчастникТип) <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993549>`_

.. rubric:: Свойства

:AdditionalInfo:
  **Строка (1-255)** — информация для участника документооборота [`ИнфДляУчаст <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993550>`_]

:Address:
  **Структура** :doc:`Address <../../objects/551@/Address>` — юридический адрес организации [`Адрес <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993551>`_]

:BankAccountNumber:
  **Строка (1-20)** — номер банковского счета организации [`НомерСчета <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993552>`_]

:BankId:
  **Строка (=9)** — банковский идентификационный код [`БИК <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993555>`_]

:BankName:
  **Строка (1-1000)** — наименование банка [`НаимБанк <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993554>`_]

:BoxId:
  **Строка** — идентификатор ящика организации

:CorrespondentAccount:
  **Строка (1-20)** — корреспондентский счет банка [`КорСчет <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993556>`_]

:Country\*:
  **Строка (1-255)** — страна [`Страна <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993558>`_]

:Department:
  **Строка (1-1000)** — структурное подразделение [`СтруктПодр <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993557>`_]

:Email:
  **Строка (1-255)** — адрес электронной почты [`ЭлПочта <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993559>`_]

:FnsParticipantId\*:
  **Строка (4-46)** — идентификатор участника ЭДО [`ИдОтпр <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993560>`_/ `ИдПол <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993561>`_]

:IndividualEntityRegistrationCertificate:
  **Строка (1-100)** — реквизиты свидетельства о государственной регистрации физического лица в качестве индивидуального предпринимателя [`СвГосРегИП <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993563>`_]

:Inn\*:
  **Строка (10-12)** — ИНН организации или индивидуального предпринимателя [`ИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993565>`_]/ [`ИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993564>`_]

:Kpp:
  **Строка (=9)** — код причины постановки на учет организации [`КПП <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993567>`_]

:LegalEntityId:
  **Строка (1-50)** — идентификатор юридического лица [`Идентиф <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993570>`_]

:Name\*:
  **Строка** — наименование организации или ФИО индивидуального предпринимателя [`НаимОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993571>`_]/[`ФИО <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993573>`_]

:Okdp:
  **Строка (1-7)** — код основного вида деятельности [`ОКДП <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=2966188>`_]

:Okopf:
  **Строка (=2)** — код организационно — правовой формы [`ОКОПФ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=2966193>`_]

:Okpo:
  **Строка (1-10)** — код в общероссийском классификаторе предприятий и организаций [`ОКПО <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993574>`_]

:OrganizationOrPersonInfo:
  **Строка (1-255)** — иные сведения, идентифицирующие физическое или юридическое лицо [`ИныеСвед <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993576>`_]

:Phone:
  **Строка (1-255)** — номер контактного телефона или факс [`Тлф	<https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993577>`_]

:Type\*:
  **Строка, чтение/запись** — тип организации. Возможные значения см. ниже.

:Ссылка:
  **Ссылка 1С** — ссылка на запись в системе 1С


\*обязательные поля

.. rubric:: Type

.. |ExtendedOrganizationInfo-Type| replace:: возможные значения
.. _ExtendedOrganizationInfo-Type:

===================== ===========================================================================================================================
Значение              Описание
===================== ===========================================================================================================================
ForeignEntity         Сведения об иностранном лице, не состоящем на учете в налоговых органах в качестве налогоплательщика [`ИнОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993579>`_]
IndividualEntity      Сведения об индивидуальном предпринимателе [`СвИП <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993578>`_]
LegalEntity           Сведения о юридическом лице, состоящем на учете в налоговых органах [`СвЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993580>`_]
===================== ===========================================================================================================================
