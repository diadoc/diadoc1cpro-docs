
ПолучитьТаблицуИспользуемыхВидовДокументов
==========================================

**Синтаксис:**

      ПолучитьТаблицуИспользуемыхВидовДокументов()

**Возвращает:**

      Таблица значений

      **Состав колонок возвращаемой таблицы:**

      * **ID** (тип Строка) — внутренний идентификатор для определения документа в коде. Не использовать пробелы и другие служебные символы, кроме «_».
      * **Наименование** (тип Строка, 150) — пользовательское представление вида документа в списках "Для отправки" и "Исходящие".
      * **ТипДокументаAPI** (тип Строка) — один из :doc:`типов документов <../../objects/Tipy_Dokumentov>`.
      * **ТипКонтентаAPI** (тип Строка) - один из :doc:`форматов документов <../../objects/Tipy_Kontenta>`.
      * **ФункцияДокументаAPI** - (тип Строка) - функция в УПД или УКД.
          * Для первичных документов: *СЧФ*, *ДОП*, *СЧФДОП*.
          * Для корректировочных: *КСЧФ*, *ДИС*, *КСЧФДИС*.
      * **БазовыйВидДокумента** (тип Строка) - идентификатор вида документа, формат которого будет основным.

**Описание:**

В функции определяется название видов документов на отправку и их характеристики.

Тип документа - название документа в терминах АПИ Диадока

Тип контента - определяет какую предопределенную структуру модуля надо заполнить, чтобы получить на отправку документ в нужном формате

Базовый вид документа - его заполнение показывает зависимость формата текущего вида документа от другого. В модуле используется для определения формата исправительных документов.

Пример использования: :doc:`Как подготовить пакет документов для отправки <../../proc/pm/Podgotovka_Paketa_Dlya_Otpravki>`
