Torg2SenderTitle
==================

Содержание титула отправителя *Акта об установленном расхождении ТОРГ-2* в формате приказа  `ММВ-7-15/423@ <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594691>`_

.. rubric:: Свойства

:AdditionalInfosPurpose:
  **Строка (1-2000)** — назначение и подписанты дополнительных сведений [`НазнДопСв <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597524>`_]. Обязателен, если `ИнфДопСв <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5610703>`_ = [4,6,8]

:CircumstancesAcceptanceInfo\*:
  **Структура** :doc:`CircumstancesAcceptanceInfo <../../objects/torg2/CircumstancesAcceptanceInfo>` — cведения об обстоятельствах приемки [`СодФХЖ1 <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594693>`_]

:CircumDraft:
  **Строка (=1)** — обстоятельства составления документа [`ОбстСостДок <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5599348>`_]. |Torg2SenderTitle-CircumDraft|_

:DocumentAdditionalInfos\*:
  **Коллекция** :doc:`DocumentAdditionalInfo <../../objects/torg2/DocumentAdditionalInfo>` — информация о формировании дополнительных сведений к документу [`ИнфДопСв <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5610703>`_]

:DocumentCreator\*:
  **Строка (1-1000)** — наименование организации, от которой формируется документ [`НаимЭконСубСост <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597773>`_]

:DocumentCreatorBase:
  **Строка (1-120)** — основание, по которому организация является составителем файла обмена информации покупателя [`ОснДоверОргСост <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597716>`_]. Обязателен, если составитель информации покупателя не является покупателем

:DocumentDate\*:
  **Дата (ДД.ММ.ГГГГ)** — дата составления документа о приемке и расхождениях [`ДатаДокПР <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5599438>`_]

:DocumentName\*:
  **Строка (1-255)** — наименование документа, определенное организацией [`НаимДокОпр <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5597803>`_]

:DocumentNumber\*:
  **Строка (1-255)** — номер документа о приемке и расхождениях [`НомДокПР <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5599378>`_]

:EvidenceAcceptanceInfo\*:
  **Структура** :doc:`EvidenceAcceptanceInfo <../../objects/torg2/EvidenceAcceptanceInfo>` — cведения о факте приемки и о расхождениях [`СодФХЖ2 <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594912>`_] 

:RecipientFnsParticipantId\*:
  **Строка (4-46)** — идентификатор участника документооборота — получателя файла обмена информации покупателя [`ИдПол <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5636525>`_]

:RevisionInfo:
  **Структура** :doc:`RevisionInfo <../../objects/torg2/RevisionInfo>` — исправление документа о приемке и расхождениях [`ИспрДокПР <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594692>`_]

:SenderFnsParticipantId\*:
  **Строка (4-46)** — идентификатор участника документооборота — отправителя файла обмена информации покупателя [`ИдОтпр <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5636530>`_]

:Signers\*:
  **Коллекция** :doc:`SignerInfo <../../objects/torg2/SignerInfo>` — сведения о лице, подписавшем файл обмена информации покупателя в электронной форме [`Подписант <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594696>`_]


\*обязательные поля


.. rubric:: Дополнительная информация

.. |Torg2SenderTitle-DocumentAdditionalInfos| replace:: Возможные значения
.. _Torg2SenderTitle-DocumentAdditionalInfos:


.. |Torg2SenderTitle-CircumDraft| replace:: Возможные значения
.. _Torg2SenderTitle-CircumDraft:

================================== ===============================================================================================================================================================================================
Значение *CircumDraft*             Описание
================================== ===============================================================================================================================================================================================
1                                  документ составлен при приемке ценностей от продавца (отправителя, перевозчика)
2                                  документ составлен после приемки ценностей от продавца (отправителя, перевозчика) в течение согласованного сторонами периода
================================== ===============================================================================================================================================================================================
