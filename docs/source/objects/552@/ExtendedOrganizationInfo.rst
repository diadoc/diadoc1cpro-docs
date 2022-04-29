ExtendedOrganizationInfo
============================

 Сведения об участнике факта хозяйственной жизни `(УчастникТип) <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593348>`_

.. rubric:: Свойства

:Address:
  **Структура** :doc:`Address <../../objects/552@/Address>` — адрес [`Адрес <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998085>`_]

:BankAccountNumber:
  **Строка (1-20)** — номер банковского счета [`НомерСчета <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998086>`_]

:BankId:
  **Строка (=9)** — банковский идентификационный код в соответствии со "Справочником БИК РФ" [`БИК <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998087>`_]

:BankName:
  **Строка (1-1000)** — наименование банка [`НаимБанк <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998088>`_]

:CorrespondentAccount:
  **Строка (1-20)** — корреспондентский счет банка [`КорСчет <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998089>`_]

:Department:
  **Строка (1-1000)** — структурное подразделение [`СтруктПодр <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998090>`_]

:Email:
  **Строка (1-255)** — адрес электронной почты [`ЭлПочта <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998091>`_]

:IndividualEntityRegistrationCertificate:
  **Строка (1-100)** — реквизиты свидетельства о государственной регистрации индивидуального предпринимателя [`СвГосРегИП <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998093>`_]

:Inn\*:
  **Строка (10-12)** — ИНН организации [`ИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998095>`_ / `ИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998094>`_]

:Kpp:
  **Строка (=9)** — КПП организации [`КПП <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998096>`_]

:LegalEntityId:
  **Строка (1-50)** — идентификатор юридического лица [`Идентиф <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998098>`_]

:Okpo:
  **Строка (1-10)** — код в общероссийском классификаторе предприятий и организаций [`ОКПО <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998103>`_]

:OrganizationAdditionalInfo:
  **Строка (1-255)** — информация для участника документооборота [`ИнфДляУчаст <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998104>`_]

:OrgName\*:
  **Строка (1-1000)** — полное наименование организации [`НаимОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998105>`_]

:OrganizationOrPersonInfo:
  **Строка (1-255)** — иные сведения, идентифицирующие организацию [`ИныеСвед <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998106>`_]

:OrgType:
  **Строка** — тип организации  (|ExtendedOrganizationInfo_Torg2-Type|_)

:Phone:
  **Строка (1-255)** — номер контактного телефона, факс  [`Тлф <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998092>`_]


\*обязательные поля

.. rubric:: Type

.. |ExtendedOrganizationInfo_Torg2-Type| replace:: возможные значения
.. _ExtendedOrganizationInfo_Torg2-Type:

===================== ===========================================================================================================================
Значение              Описание
===================== ===========================================================================================================================
ForeignEntity         Сведения об иностранной организации [`ИнОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998110>`_]
IndividualEntity      Сведения об индивидуальном предпринимателе [`СвИП <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998108>`_]
LegalEntity           Сведения о российской организации [`СвЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998111>`_]
PhysicalEntity        Сведения о физическом лице [`СвФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=339635&rangeId=5998107>`_]
===================== ===========================================================================================================================
