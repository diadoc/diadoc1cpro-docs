ExtendedSignerDetails
=======================

Сведения о лице, подписавшем информацию продавца в электронном виде `(Подписант) <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637602>`_

.. rubric:: Свойства

:FirstName\*:
  **Строка (1-60)** — имя [`Имя <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637297>`_]

:Inn\*:
  **Строка (10-12)** — ИНН организации или индивидуального предпринимателя [`ИННЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993565>`_]/ [`ИННФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5993564>`_]

:JobTitle\*:
  **Строка (1-128)** — должность [`Должность <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5995648>`_]

:OrganizationName\*:
  **Строка (1-128)** — наименование организации [`НаимОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=6000930>`_]. Обязателен только для представителя юридического лица

:OrganizationsPowerBase:
  **Строка (1-255)** — основание полномочий организации [`ОснПолнОрг <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5638122>`_]. Обязателен для работника иной уполномоченной организации

:Patronymic:
  **Строка (1-60)** — отчество [`Отчество <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637588>`_]

:Powers\*:
  **Строка (=1)** — область полномочий [`ОблПолн <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5638115>`_] (|SignerDetails-SignerPowers|_)

:PowersBase\*:
  **Строка (1-255)** — основание полномочий подписанта [`ОснПолн <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5638121>`_]

:RegistrationCertificate:
  **Строка (1-100)** — реквизиты свидетельства о государственной регистрации индивидуального предпринимателя [`СвГосРегИП <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5995652>`_]

:SignerInfo:
  **Строка (1-255)** — иные сведения, идентифицирующие физическое лицо [`ИныеСвед <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5995656>`_]

:SignerType\*:
  **Строка** — тип подписанта (|SignerDetails-SignerType|_)

:Status\*:
  **Строка (=1)** — статус [`Статус <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5638117>`_] (|SignerDetails-SignerStatus|_)
 
:Surname\*:
  **Строка (1-60)** — фамилия [`Фамилия <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5637296>`_]


\*обязательные поля

.. rubric:: SignerPowers
.. |SignerDetails-SignerPowers| replace:: возможные значения
.. _SignerDetails-SignerPowers:

======================= ===========================================================================================================================
Значение                Описание
======================= ===========================================================================================================================
1                       лицо, совершившее сделку
2                       лицо, совершившее сделку и ответственное за ее оформление
3                       лицо, ответственное за оформление свершившегося события
======================= ===========================================================================================================================

.. rubric:: SignerStatus

.. |SignerDetails-SignerStatus| replace:: возможные значения
.. _SignerDetails-SignerStatus:

======================= ===========================================================================================================================
Значение                Описание
======================= ===========================================================================================================================
1                       работник организации — продавца
2                       работник организации — составителя информации продавца
3                       работник иной уполномоченной организации
4                       уполномоченное физическое лицо
======================= ===========================================================================================================================

.. rubric:: SignerType

.. |SignerDetails-SignerType| replace:: возможные значения
.. _SignerDetails-SignerType:

===================== ===========================================================================================================================
Значение              Описание
===================== ===========================================================================================================================
IndividualEntity      индивидуальный предприниматель [`ИП <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5995891>`_]
LegalEntity           представитель юридического лица [`ЮЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5995892>`_]
PhysicalPerson        физическое лицо [`ФЛ <https://normativ.kontur.ru/document?moduleId=1&documentId=339634&rangeId=5995893>`_]
===================== ===========================================================================================================================