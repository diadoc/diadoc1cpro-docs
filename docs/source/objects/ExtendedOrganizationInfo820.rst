
ExtendedOrganizationInfo
========================

Сведения об участнике факта хозяйственной жизни `(УчастникТип) <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241534>`_

.. rubric:: Свойства

:AdditionalInfo
  **Строка (1-255)** — информация для участника документооборота [`ИнфДляУчаст <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241864>`_]

:Address
  :doc:`AddressInfo <../../objects/AddressInfo>` — юридический адрес организации [`Адрес <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241843>`_]. Обязателен для [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427421>`_] = СЧФ и [`Функция <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427421>`_] = СЧФДОП

:BankAccountNumber
  **Строка (1-20)** — номер банковского счета организации [`НомерСчета <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241859>`_]

:BankId
  **Строка (1-9)** — БИК банка [`БИК <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241862>`_]

:BankName
  **Строка (1-1000)** — наименование банка [`НаимБанк <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241861>`_]

:BoxId
  **Строка** — идентификатор ящика организации

:CorrespondentAccount
  **Строка (1-20)** — корреспондентский счет банка [`КорСчет <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241853>`_]

:Country*
  **Строка (1-255)** — страна [`Страна <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=2966201>`_]

:Department
  **Строка (1-1000)** — структурное подразделение [`СтруктПодр <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241863>`_]

:Email
  **Строка (1-255)** — адрес электронной почты [`ЭлПочта <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241852>`_]

:FnsParticipantId*
  **Строка (4-46)** — идентификатор участника ЭДО [`ИдОтпр <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241844>`_/`ИдПол <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241845>`_]

:HyphenInn
  **Булево** — признак того, что ИНН организации не указан. Если Истина, то будет указано значение "-" в поле [`ДефИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241841>`_/`ДефИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241840>`_]. Обязателен при отсутствии [`ИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427422>`__/`ИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427423>`__]

:IndividualEntityRegistrationCertificate
  **Строка (1-100)** — реквизиты свидетельства о государственной регистрации индивидуального предпринимателя [`СвГосРегИП <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241870>`_]. Обязательны для случаев подписания счета-фактуры непосредственно продавцом

:Inn
  **Строка (10-12)** — ИНН организации [`ИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241835>`_/`ИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241836>`_].
  Если не заполнено, то будет указано значение "-" в поле [`ДефИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241841>`_/`ДефИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241840>`_].  Обязателен при отсутствии [`ИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427422>`__/`ИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=4427423>`__]

:Kpp
  **Строка (=9)** — КПП организации [`КПП <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241842>`_]

:LegalEntityId
  **Строка (1-255)** — идентификатор юридического лица-нерезидента [`Идентиф <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=396450>`_]

:Name*
  **Строка** — наименование организации. Для индивидуального предпринимателя наименование задается в формате "Фамилия Имя Отчество" [`НаимОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241731>`_/`ФИО <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241839>`_]

:Okdp
  **Строка (1-7)** — код основного вида деятельности по ОКДП [`ОКДП <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=2966188>`_]

:Okopf
  **Строка (=2)** — код организационно-правовой формы по ОКОПФ [`ОКОПФ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=2966193>`_]

:Okpo
  **Строка (1-10)** — код в общероссийском классификаторе предприятий и организаций [`ОКПО <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241850>`_]

:OrganizationOrPersonInfo
  **Строка (1-255)** — иные сведения, идентифицирующие физическое или юридическое лицо [`ИныеСвед <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241869>`_]

:Phone
  **Строка (1-255)** — номер контактного телефона [`Тлф	<https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241851>`_]

:Type*
  **Строка, чтение/запись** — тип организации  (|ExtendedOrganizationInfo-Type|_)


\*обязательные поля

.. rubric:: Дополнительная информация

.. |ExtendedOrganizationInfo-Type| replace:: возможные значения
.. _ExtendedOrganizationInfo-Type:

===================== ===========================================================================================================================
Значение *Type*       Описание
===================== ===========================================================================================================================
ForeignEntity         Сведения об иностранном лице, не состоящем на учете в налоговых органах в качестве налогоплательщика ([`СвИнНеУч <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=2966705>`_])
IndividualEntity      Сведения об индивидуальном предпринимателе ([`СвИП <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=2966707>`_])
LegalEntity           Сведения о юридическом лице, состоящем на учете в налоговых органах ([`СвЮЛУч <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=2966708>`_])
PhysicalEntity        Сведения о физическом лице ([`СвФЛУчастФХЖ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=2966710>`_])
===================== ===========================================================================================================================
