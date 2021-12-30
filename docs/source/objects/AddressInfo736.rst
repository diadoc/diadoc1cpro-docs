
AddressInfo
===================

Сведения об адресе `(АдресТип) <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969463>`_

.. rubric:: Свойства

:AddressCode*
  **Строка (1-36)** — уникальный номер адреса объекта адресации в государственном адресном реестре [`КодГАР <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969464>`_]

:AddressText*
  **Строка (1-1000)** — адрес [`АдрТекст <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969465>`_]

:Apartment
  **Строка (1-20)** — квартира [`Кварт <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969468>`_]

:Block
  **Строка (1-20)** — корпус [`Корпус <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969467>`_]

:Building
  **Строка (1-20)** — дом [`Дом <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969493>`_]

:City
  **Строка (1-50)** — город [`Город <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969499>`_]

:CountryCode*
  **Строка (=3)** — код страны (для адреса за пределами РФ) [`КодСтр <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969498>`_]

:IsForeign*
  **Булево** — признак того, что адрес является иностранным (за пределами РФ). Если установлен признак Истина, тогда будет заполнен [`АдрИнф <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969497>`_]

:Locality
  **Строка (1-50)** — населенный пункт [`НаселПункт <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969469>`_]

:RegionCode*
  **Строка (=2)** — код региона РФ [`КодРегион <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969471>`_]

:Street
  **Строка (1-50)** — улица [`Улица <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969496>`_]

:Territory
  **Строка (1-50)** — район [`Район <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969494>`_]

:ZipCode
  **Строка (=6)** — индекс [`Индекс <https://normativ.kontur.ru/document?moduleId=1&documentId=375857&rangeId=2969470>`_]


\*обязательные поля