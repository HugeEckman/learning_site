### Структура проекта 

На данный момент структура следующая:

Класс ***Category*** - категория, к которой принадлежит курс.

Класс ***Course*** - основная структурная еденица проекта. Каждый курс может принадлежать только к одной категории.

Класс ***Teacher*** - учитель/лектор. Каждый лектор может вести только один курс (возможно не совсем корректно, далее по ходу разработки проекта возможно придется переделать эту модель).

Класс ***Catalog*** - каталог, содержащий в себе все доступные курсы.

Класс ***Lesson*** - урок. Каждый курс содержит множество уроков. Каждый урок может вести только один лектор.