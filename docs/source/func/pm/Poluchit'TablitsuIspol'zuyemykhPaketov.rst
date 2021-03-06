
ПолучитьТаблицуИспользуемыхПакетов
==================================

**Синтаксис:**

      ПолучитьТаблицуИспользуемыхПакетов()

**Возвращает:**

      Таблица значений

      **Состав колонок возвращаемой таблицы:**

      * **ID** (тип Строка) — внутренний идентификатор для определения пакета в коде. Не использовать пробелы и другие служебные символы, кроме «_».
      * **Наименование** (тип Строка, 150) — пользовательское представление пакета в списке «Для отправки».
      * **СоставПакета** (тип Строка) — список идентификаторов видов документов, которые могут быть в составе вида пакета
      * **КатегорияПакета** (тип Строка) — внутреннее название категории пакета
      * **НаименованиеКатегории** (тип Строка) — пользовательское название категории пакета
      * **Шаблон** (тип Булево) — признак того, что пакет является пакетом-шаблоном.

**Описание:**

В функции определяются пакеты на отправку, которые будут формироваться в модуле.

Состав пакета, категория пакета и наименование пакета - используются для возможности настройки видов пакетов в пользовательском режиме.
Если нет необходимости в дальнейшем менять состав на отправку, то можно не заполнять.

Пример использования: :doc:`Как подготовить пакет документов для отправки <../../proc/pm/Podgotovka_Paketa_Dlya_Otpravki>`
