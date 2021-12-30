
ExtendedOrganizationInfo
========================

Сведения о продавце (покупателе) `(СвПродПокТип) <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969921>`_

.. rubric:: Свойства

:AdditionalInfo:
  **Строка (1-255)** — информация для участника документооборота [`ИнфДляУчаст <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969922>`_]

:Address:
  **Коллекция** :doc:`AddressInfo <../../objects/AddressInfo736>` — юридический адрес организации [`Адрес <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969923>`_]

:BankAccountNumber:
  **Строка (1-20)** — номер банковского счета организации [`НомерСчета <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969924>`_]

:BankId:
  **Строка (=9)** — БИК банка [`БИК <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969926>`_]

:BankName:
  **Строка (1-1000)** — наименование банка [`НаимБанк <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969928>`_]

:BoxId:
  **Строка** — идентификатор ящика организации

:CorrespondentAccount:
  **Строка (1-20)** — корреспондентский счет банка [`КорСчет <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969929>`_]

:Country\*:
  **Строка (1-255)** — страна [`Страна <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=2966201>`_]

:Department:
  **Строка (1-1000)** — структурное подразделение [`СтруктПодр <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969937>`_]

:Email:
  **Строка (1-255)** — адрес электронной почты [`ЭлПочта <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969938>`_]

:FnsParticipantId\*:
  **Строка** — идентификатор участника ЭДО [`ИдОтпр <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969960>`_/ `ИдПол <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969961>`_]

:IndividualEntityRegistrationCertificate:
  **Строка (1-100)** — реквизиты свидетельства о государственной регистрации физического лица в качестве индивидуального предпринимателя [`СвГосРегИП <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969941>`_]. Обязательны для случаев подписания корректировочного счета-фактуры непосредственно продавцом

:Inn\*:
  **Строка (10-12)** — ИНН организации [`ИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969965>`_]/ [`ИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969966>`_]

:Kpp:
  **Строка (=9)** — КПП организации [`КПП <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2970056>`_]

:LegalEntityId:
  **Строка (1-255)** — идентификатор юридического лица-нерезидента [`Идентиф <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2970057>`_]

:Name\*:
  **Строка** — наименование организации. Для индивидуального предпринимателя наименование задается в формате "Фамилия Имя Отчество" [`НаимОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2970058>`_]/ [`ФИО <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2970059>`_]

:Okdp:
  **Строка (1-7)** — код основного вида деятельности по ОКДП [`ОКДП <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=2966188>`_]

:Okopf:
  **Строка (=2)** — код организационно-правовой формы по ОКОПФ [`ОКОПФ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=2966193>`_]

:Okpo:
  **Строка (1-10)** — код в общероссийском классификаторе предприятий и организаций [`ОКПО <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2970060>`_]

:OrganizationOrPersonInfo:
  **Строка (1-255)** — иные сведения, идентифицирующие физическое или юридическое лицо [`ИныеСвед <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2970063>`_]

:Phone:
  **Строка (1-255)** — номер контактного телефона [`Тлф	<https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2970064>`_]

:Type\*:
  **Строка, чтение/запись** — тип организации  (|ExtendedOrganizationInfo-Type|_)


\*обязательные поля

.. rubric:: Дополнительная информация

.. |ExtendedOrganizationInfo-Type| replace:: возможные значения
.. _ExtendedOrganizationInfo-Type:

===================== ===========================================================================================================================
Значение *Type*       Описание
===================== ===========================================================================================================================
ForeignEntity         Сведения об иностранном лице, не состоящем на учете в налоговых органах в качестве налогоплательщика [`СвИнНеУч <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969957>`_]
IndividualEntity      Сведения об индивидуальном предпринимателе [`СвИП <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969958>`_]
LegalEntity           Сведения о юридическом лице, состоящем на учете в налоговых органах [`СвЮЛУч <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969959>`_]
===================== ===========================================================================================================================
