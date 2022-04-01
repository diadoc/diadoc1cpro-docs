AccompanyingDocumentTable
===============================

Сведения о грузе по сопроводительным транспортным документам `(СвСопрДок) <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593679>`_

.. rubric:: Свойства

:AdditionalInfo:
  **Структура** :doc:`AdditionalInfo <../../objects/torg2/AdditionalInfo>` — информационное поле сведений о грузе по сопроводительным транспортным документам [`ИнфПолСопрДок <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593687>`_]

:CargoName\*:
  **Строка (1-1000)** — наименование груза [`НаимГруз <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593697>`_]

:DocumentWeight:
  **Структура** :doc:`WeightCargo <../../objects/torg2/WeightCargo>` — масса в пункте отправления по документам грузоотправителя [`МассаДок <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593721>`_]

:FactWeight:
  **Структура** :doc:`WeightCargo <../../objects/torg2/WeightCargo>` — масса в пункте прибытия [`МассаФакт <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593722>`_]

:PackingType:
  **Строка (1-100)** — вид упаковки [`ВидУпак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593724>`_]

:Quantity:
  **Число (12)** — количество мест [`КолМест <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593727>`_]

:SealingMark:
  **Строка (1-20)** — отметка об опломбировании [`ОтмПломб <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593729>`_]

:Unit:
  **Строка (3-4)** — код единицы измерения [`ОКЕИ_Тов <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593731>`_]

:UnitName:
  **Строка (1-255)** — наименование единицы измерения [`НаимЕдИзм <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593732>`_]. 	Обязателен при наличии `ОКЕИ_Тов <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593731>`_


\*обязательные поля