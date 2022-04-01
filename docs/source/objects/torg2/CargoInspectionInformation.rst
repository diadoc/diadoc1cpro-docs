CargoInspectionInformation
===========================

Сведения о событиях, связанных с осмотром груза `(СвОсмГруз) <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594284>`_

.. rubric:: Свойства

:AccompanyingDocumentInfo\*:
  **Структура** :doc:`AccompanyingDocument <../../objects/torg2/AccompanyingDocument>` — наименование, номер и дата сопроводительного документа [`СопрДок <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594285>`_]

:AdditionalInfoId:
  **Структура** :doc:`AdditionalInfos <../../objects/torg2/AdditionalInfos>` — информационное поле сведений о результатах осмотра [`ИнфПолСвОсм <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5638060>`_]

:CertificateConformityNumbers:
  **Коллекция** :doc:`CertificateConformityNumber <../../objects/torg2/CertificateConformityNumber>` — номер сертификата соответствия [`СертСоотв <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594286>`_]

:DeliveryDate:
  **Дата (ДД.ММ.ГГГГ)** — дата отправки груза со станции [`ДатаОтпр <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594287>`_]

:ReceptionDate:
  **Дата (ДД.ММ.ГГГГ)** — дата осмотра прибывшего груза [`ДатаОсм <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594288>`_]

:ReceptionFinishTime:
  **Строка (=8)** — время окончания приемки [`ВремяОконч <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594289>`_]

:ReceptionPlace:
  **Строка (1-100)** — место составления документа о приемке и расхождениях [`МестоСост <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594290>`_]

:ReceptionStartTime:
  **Строка (=8)** — время начала приемки [`ВремяНач <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594291>`_]


\*обязательные поля