ExtendedOrganizationInfo_Torg2
================================

Сведения об участнике факта хозяйственной жизни `(УчастникТип) <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593348>`_

.. rubric:: Свойства

:Address:
  **Структура** :doc:`Address <../../objects/torg2/Address>` — адрес [`Адрес <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593066>`_]

:BankAccountNumber:
  **Строка (1-20)** — номер банковского счета [`НомерСчета <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593363>`_]

:BankId:
  **Строка (=9)** — банковский идентификационный код в соответствии со "Справочником БИК РФ" [`БИК <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593382>`_]

:BankName:
  **Строка (1-1000)** — наименование банка [`НаимБанк <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593364>`_]

:CorrespondentAccount:
  **Строка (1-20)** — корреспондентский счет банка [`КорСчет <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593387>`_]

:Department:
  **Строка (1-1000)** — структурное подразделение [`СтруктПодр <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5592720>`_]

:Email:
  **Строка (1-255)** — адрес электронной почты [`ЭлПочта <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593350>`_]

:IndividualEntityRegistrationCertificate:
  **Строка (1-100)** — реквизиты свидетельства о государственной регистрации индивидуального предпринимателя [`СвГосРегИП <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5636377>`_]

:Inn:
  **Строка (10-12)** — ИНН организации [`ИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5636359>`_/`ИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5636360>`_]

:Kpp:
  **Строка (=9)** — КПП организации [`КПП <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5636361>`_]

:LegalEntityId:
  **Строка (1-255)** — идентификатор юридического лица [`Идентиф <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5636364>`_]

:Okpo:
  **Строка (1-10)** — код в общероссийском классификаторе предприятий и организаций [`ОКПО <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5592719>`_]

:OrganizationAdditionalInfo:
  **Строка (1-255)** — информация для участника документооборота [`ИнфДляУчаст <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5592721>`_]

:OrgName\*:
  **Строка (1-1000)** — полное наименование организации [`НаимОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5636367>`_]

:OrganizationOrPersonInfo:
  **Строка (1-255)** — иные сведения, идентифицирующие организацию [`ИныеСвед <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5636370>`_]

:OrgType:
  **Строка** — тип организации  (|ExtendedOrganizationInfo_Torg2-Type|_)

:Phone:
  **Строка (1-255)** — номер контактного телефона, факс  [`Тлф <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593352>`_]


\*обязательные поля

.. rubric:: Дополнительная информация

.. |ExtendedOrganizationInfo_Torg2-Type| replace:: возможные значения
.. _ExtendedOrganizationInfo_Torg2-Type:

===================== ===========================================================================================================================
Значение *Type*       Описание
===================== ===========================================================================================================================
ForeignEntity         Сведения об иностранном лице, не состоящем на учете в налоговых органах в качестве налогоплательщика [`СвИнНеУч <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593676>`_]
IndividualEntity      Сведения об индивидуальном предпринимателе [`СвИП <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593673>`_]
LegalEntity           Сведения об организации, состоящей на учете в налоговом органе [`СвОргУч <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593676>`_]
PhysicalEntity        Сведения о физическом лице [`СвФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593674>`_]
===================== ===========================================================================================================================
