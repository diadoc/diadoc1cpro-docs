OtherCircumstancesAcceptanceInfo
=================================

Другие обстоятельства приемки ценностей `(ДрОбстПрием) <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594292>`_

.. rubric:: Свойства

:AccompanyingTransferDocumentInfo:
  **Структура** :doc:`AccompanyingDocument <../../objects/torg2/AccompanyingDocument>` — наименование, номер и дата сопроводительного транспортного документа [`СопрТрансДок <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594293>`_]

:AdditionalInfo:
  **Структура** :doc:`AdditionalInfo <../../objects/torg2/AdditionalInfo>` — текстовая информация [`ТекстИнфТип <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593745>`_]

:CargoActualState:
  **Строка (1-1000)** — состояние тары и упаковки в момент осмотра ценностей [`СостТара <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594294>`_]

:Carrier:
  **Структура** :doc:`OrganizationDetails <../../objects/torg2/OrganizationDetails>` — перевозчик ценностей, представитель которого передает груз [`Перевозчик <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594295>`_]

:MissingAssets:
  **Строка (1-200)** — тип определения недостающих ценностей [`ОпредНедост <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594296>`_]

:StorageConditions:
  **Строка (1-1000)** — условия хранения ценностей на складе получателя [`УсловХран <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594298>`_]
