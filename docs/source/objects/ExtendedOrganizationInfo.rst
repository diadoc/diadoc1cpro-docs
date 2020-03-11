
ExtendedOrganizationInfo
========================

Сведения об участнике факта хозяйственной жизни `(УчастникТип) <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241534>`_

.. rubric:: Свойства

:Name:
  **Строка** - наименование организации. Для индивидуального предпринимателя наименование задается в формате "Фамилия Имя Отчество" [`НаимОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241731>`_/`ФИО <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241839>`_]

:Inn:
  **Строка (10-12)** - ИНН организации [`ИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241835>`_]/ [`ИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241836>`_].
  Если не заполнено, то будет указано значение "-" в поле [`ДефИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241841>`_]/ [`ДефИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241840>`_].

:HyphenInn:
  **Булево** - Если Истина, то будет указано значение "-" в поле [`ДефИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241841>`_]/ [`ДефИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241840>`_].

:Kpp:
  **Строка (=9)** - КПП организации [`КПП <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241842>`_]

:Address:
  :doc:`AddressInfo <../../objects/AddressInfo>` - юридический адрес организации [`Адрес <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241843>`_]

:FnsParticipantId:
  **Строка** - идентификатор участника ЭДО [`ИдОтпр <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241844>`_/`ИдПол <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241845>`_]

:Type:
  **Строка, чтение/запись** - тип организации "LegalEntity" ([`СвЮЛУч <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241846>`_]),
  "IndividualEntity" ([`СвИП <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241847>`_]),
  "ForeignEntity" ([`СвИнНеУч <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241848>`_]),
  "PhysicalEntity" ([`СвФЛУчастФХЖ <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241849>`_])

:Okpo:
  **Строка (1-10)** - код в общероссийском классификаторе предприятий и организаций [`ОКПО <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241850>`_]

:Phone:
  **Строка (1-255)** - номер контактного телефона [`Тлф	<https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241851>`_]

:Email:
  **Строка (1-255)** - адрес электронной почты [`ЭлПочта <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241852>`_]

:CorrespondentAccount:
  **Строка (1-20)** - корреспондентский счет банка [`КорСчет <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241853>`_]

:BankAccountNumber:
  **Строка (1-20)** - номер банковского счета организации [`НомерСчета <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241859>`_]

:BankName:
  **Строка (1-1000)** - наименование банка [`НаимБанк <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241861>`_]

:BankId:
  **Строка (1-9)** - БИК банка [`БИК <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241862>`_]

:Department:
  **Строка (1-1000)** - структурное подразделение [`СтруктПодр <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241863>`_]

:AdditionalInfo:
  **Строка (1-255)** - информация для участника документооборота [`ИнфДляУчаст <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241864>`_]

:OrganizationOrPersonInfo:
  **Строка (1-255)** - иные сведения, идентифицирующие физическое или юридическое лицо [`ИныеСвед <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241869>`_]

:IndividualEntityRegistrationCertificate:
  **Строка (1-100)** - реквизиты свидетельства о государственной регистрации индивидуального предпринимателя [`СвГосРегИП <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=241870>`_]
