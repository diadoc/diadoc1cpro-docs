
BuyerInfoCircumPublicProc
=========================

Информация покупателя об обстоятельствах закупок для государственных и муниципальных нужд (для учета Федеральным казначейством денежных обязательств) (`ИнфПокГосЗакКазн <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239634>`_)

.. rubric:: Свойства

:ProcCode:
  **Строка (1-36)** - идентификационный код закупки [`ИдКодЗак <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239616>`_]

:PersonalAccountBuyer:
  **Строка (=11)** - номер лицевого счета покупателя [`ЛицСчетПок <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239617>`_]

:NameFinAuthority:
  **Строка (1-2000)** - наименование финансового органа покупателя [`НаимФинОргПок <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239618>`_]

:BuyerRegistryEntryNumber:
  **Строка (=8)** - номер реестровой записи покупателя [`НомРеестрЗапПок <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239619>`_]

:BuyerLiabNumber:
  **Строка (16-19)** - учетный номер бюджетного обязательства покупателя [`УчНомБюдОбязПок <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239620>`_]

:BuyerTreasuryCode:
  **Строка (=4)** - код территориального органа Федерального казначейства покупателя [`КодКазначПок <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239621>`_]

:SellerTreasuryName:
  **Строка (1-2000)** - наименование территориального органа Федерального казначейства покупателя [`НаимКазначПок <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239622>`_]

:OKTMOBuy:
  **Строка (8-11)** - код покупателя в Общероссийском классификаторе территорий муниципальных образований [`ОКТМОПок <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239623>`_]

:OKTMOPlaceDelivery:
  **Строка (8-11)** - код места поставки в Общероссийском классификаторе территорий муниципальных образований [`ОКТМОМесПост <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239624>`_]

:PayDeadLine:
  **Дата (ДД.ММ.ГГГГ)** - предельная дата оплаты [`ДатаОплПред <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239625>`_]

:NumberFundsLiab:
  **Строка (=22)** - учетный номер денежного обязательства [`УчНомДенОбяз <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239626>`_]

:PriorityPayment:
  **Строка (=1)** - очередность платежа [`ОчерПлат <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239628>`_]

:TypePayment:
  **Строка (=1)** - вид платежа [`ВидПлат <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239631>`_]

:InfoFundsLiab:
  **Коллекция** :doc:`InfoFundsLiab <../../objects/InfoFundsLiab>` - информация для сведений о денежном обязательстве [`ИнфСведДенОбяз <https://normativ.kontur.ru/document?moduleId=1&documentId=328588&rangeId=239632>`_]
