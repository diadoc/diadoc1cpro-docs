AcceptanceResults
=======================

Результаты приемки ценностей `(РезПрием) <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595167>`_

.. rubric:: Свойства

:AcceptanceDiscrepancyInfo:
  **Строка (1-2000)** — информация о расхождениях, выявленных при приемке результатов выполненных работ (при документировании факта оказания услуг) или при получении имущественных прав [`РасхРабУслПрав <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595177>`_]. Обязателен при отсутствии всех перечисленных элементов: `ПоДокум <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595179>`_, `ПоФакту <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595182>`_, `Брак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595184>`_, `Бой <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5637425>`_, `Недостача <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595185>`_, `Излишки <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595186>`_, `ЦенОтклон <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595188>`_

:AccordingToSellerDocument:
  **Структура** :doc:`AcceptedProductData <../../objects/torg2/AcceptedProductData>` — информация по документам поставщика [`ПоДокум <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595179>`_]

:ActuallyAccepted:
  **Структура** :doc:`AcceptedProductData <../../objects/torg2/AcceptedProductData>` — фактически принятый товар [`ПоФакту <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595182>`_]. Обязателен при отсутствии всех перечисленных элементов: `ПоДокум <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595179>`_, `Брак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595184>`_, `Бой <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5637425>`_, `Недостача <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595185>`_, `Излишки <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595186>`_, `ЦенОтклон <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595188>`_, `РасхРабУслПрав <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595177>`_

:AdditionalInfos:
  **Коллекция** :doc:`AdditionalInfo <../../objects/torg2/AdditionalInfo>` — информационное поле сведений о результатах приемки ценностей [`ТекстИнфТип <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239850>`_]

:Assets\*:
  **Структура** :doc:`Assets <../../objects/torg2/Assets>` — товарно-материальные ценности [`Ценности <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595178>`_]

:Breakage:
  **Структура** :doc:`DiscrepancyData <../../objects/torg2/DiscrepancyData>` — бой [`Бой <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5637425>`_]. Обязателен при отсутствии всех перечисленных элементов: `ПоДокум <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595179>`_, `ПоФакту <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595182>`_, `Брак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595184>`_, `Недостача <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595185>`_, `Излишки <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595186>`_, `ЦенОтклон <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595188>`_, `РасхРабУслПрав <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595177>`_

:PriceDeviations:
  **Структура** :doc:`PriceDeviations <../../objects/torg2/PriceDeviations>` — ценовые отклонения [`ЦенОтклон <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595188>`_]

:Reject:
  **Структура** :doc:`DiscrepancyData <../../objects/torg2/DiscrepancyData>` — брак [`Брак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595184>`_]. Обязателен при отсутствии всех перечисленных элементов: `ПоДокум <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595179>`_, `ПоФакту <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595182>`_, `Бой <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5637425>`_, `Недостача <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595185>`_, `Излишки <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595186>`_, `ЦенОтклон <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595188>`_, `РасхРабУслПрав <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595177>`_

:Shortfall:
  **Структура** :doc:`DiscrepancyData <../../objects/torg2/DiscrepancyData>` — недостача [`Недостача <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595185>`_]. Обязателен при отсутствии всех перечисленных элементов: `ПоДокум <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595179>`_, `ПоФакту <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595182>`_, `Брак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595184>`_, `Бой <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5637425>`_, `Излишки <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595186>`_, `ЦенОтклон <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595188>`_, `РасхРабУслПрав <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595177>`_

:Surplus:
  **Структура** :doc:`DiscrepancyData <../../objects/torg2/DiscrepancyData>` — излишки [`Излишки <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595186>`_]. Обязателен при отсутствии всех перечисленных элементов: `ПоДокум <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595179>`_, `ПоФакту <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595182>`_, `Брак <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595184>`_, `Бой <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5637425>`_, `Недостача <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595185>`_, `ЦенОтклон <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595188>`_, `РасхРабУслПрав <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5595177>`_

:Unit:
  **Строка (3-4)** — код единицы измерения [`ОКЕИ_Тов <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593731>`_]. Обязателен при наличии натурального измерителя факта хозяйственной жизни

:UnitName:
  **Строка (1-255)** — наименование единицы измерения [`НаимЕдИзм <https://normativ.kontur.ru/document?moduleId=1&documentId=348230&rangeId=5593732>`_]


\*обязательные поля