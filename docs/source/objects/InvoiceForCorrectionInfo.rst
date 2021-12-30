
InvoiceForCorrectionInfo
========================

Счет-фактура, счет-фактура с дополнительной информацией, документ о передаче товаров (работ, услуг, имущественных прав), в результате которой изменяется финансовое состояние передающей и принимающей стороны, к которому составлен корректировочный счет-фактура, корректировочный счет-фактура и документ о согласии покупателя на изменение стоимости отгрузки, документ о согласии покупателя на изменение стоимости отгрузки `(СчФ) <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611322>`_

.. rubric:: Свойства

:InvoiceDate*
  **Дата (ДД.ММ.ГГГГ)** — дата составления (выписки) счета-фактуры и пр. [`ДатаСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611323>`_]

:InvoiceNumber*
  **Строка (1-1000)** — порядковый номер счета-фактуры [`НомерСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611324>`_]

:InvoiceRevisions
  **Коллекция** :doc:`InvoiceRevisionInfo <../../objects/InvoiceRevisionInfo>` — с учетом исправления счета-фактуры [`ИспрСчФ <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2611325>`_]


\*обязательные поля