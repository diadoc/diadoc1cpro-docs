
EventContent
============

Содержание события (факта хозяйственной жизни) 3 — сведения о факте согласования (уведомления) `(СодФХЖ3) <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611305>`_

.. rubric:: Свойства

:CostChangeInfo:
  **Строка (1-2000)** — иные сведения об изменении стоимости [`ИныеСвИзмСтоим <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611306>`_]

:OperationContent:
  **Строка (1-255)** — содержание операции [`СодОпер <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611309>`_]

:NotificationDate:
  **Дата** — дата направления на согласование (дата уведомления) [`ДатаНапр <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611311>`_]

:TransferDocDetails736:
  **Коллекция** :doc:`BaseDocumentName <../../objects/BaseDocumentName>` — реквизиты передаточных (отгрузочных) документов, к которым относится корректировка [`ПередатДокум <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611312>`_]

:CorrectionBases:
  **Коллекция** :doc:`BaseDocumentName <../../objects/BaseDocumentName>` — реквизиты документов, являющихся основанием корректировки [`ДокумОснКор <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611320>`_]
