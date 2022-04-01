ReceptionInformation
========================

Сведения о дате и времени событий, связанных с приемкой груза `(СвВремПрием) <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594482>`_

.. rubric:: Свойства

:CargoArrivalDateTime:
  **ДатаВремя (=19)** — прибытие на место назначения [`ПрибГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594483>`_]. Обязателен при отсутствии всех перечисленных элементов: `ВыдачГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594486>`_, `ВскрытГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594484>`_, `ДостГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594485>`_

:CargoOpeningDateTime:
  **ДатаВремя (=19)** — вскрытие вагона [`ВскрытГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594484>`_]. Обязателен при отсутствии всех перечисленных элементов: `ВыдачГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594486>`_, `ПрибГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594483>`_, `ДостГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594485>`_

:DeliveryDateTime:
  **ДатаВремя (=19)** — доставка на склад получателя [`ДостГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594485>`_]. Обязателен при отсутствии всех перечисленных элементов: `ВыдачГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594486>`_, `ВскрытГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594484>`_, `ПрибГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594483>`_

:DeliveryPoint:
  **ДатаВремя (=19)** — выдача груза транспортной организацией [`ВыдачГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594486>`_]. Обязателен при отсутствии всех перечисленных элементов: `ПрибГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594483>`_, `ДостГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594485>`_, `ВскрытГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594484>`_, `ДостГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5594485>`_
