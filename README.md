# GHDoc-temp

Шаблон для документації проекту Grasshopper

## Опис проекту

Цей проект містить документацію та приклади для роботи з Rhinoceros Grasshopper з використанням IronPython 2.7.

## Структура проекту

```
GHDoc-temp/
├── Doc/                    # Документація проекту
│   ├── ConduitRunsHeight.md
│   ├── Suspension.md
│   └── ...
├── Gh/                     # Файли Grasshopper
│   ├── ConduitRunsHeight.gh
│   ├── git_help.gh
│   ├── Suspension.gh
│   └── ...
├── Help/                   # Довідкова інформація
│   ├── Markdown.md
│   └── ...
├── Py/                     # Python скрипти
│   ├── git_help.py
│   └── ...
└── README.md              # README
```

## Документація

### Основна документація

- [**ConduitRunsHeight**](./Doc/ConduitRunsHeight.md) - Документація з роботи з висотою прокладки кабелів
- [**Suspension**](./Doc/Suspension.md) - Документація з системи підвіски

### Довідкова інформація

- [**Markdown Guide**](./Help/Markdown.md) - Посібник з використання Markdown

## Швидкий старт

1. Збережіть `.gh` файл у директорії `./Gh` (без використання в імені "_001", "v0.001" тощо)
2. Імпортуйте вміст з файлу `./Gh/git_help.gh` 
3. Імпортований скрипт має такі параметри:
    
    **Inputs:**
    
    - `OPEN_MAIN_BRANCH`: Boolean - відкриває основну гілку репозиторію на GitHub
    - `OPEN_HELP_IN_GITHUB`: Boolean - відкриває документацію поточного файлу на GitHub
    - `OPEN_LOCAL_HELP`: Boolean - відкриває локальний .md файл документації в редакторі
    
    **Output:**
    
    - `md`: String - вміст локального .md файлу документації

> [!important] 
> `OPEN_HELP_IN_GITHUB` відкриває документацію на поточній активній гілці репозиторію, а `OPEN_MAIN_BRANCH` завжди відкриває документацію на основній гілці `main`. Це дозволяє переглядати як поточну версію документації, так і стабільну версію з основної гілки.

1. Якщо натиснути `OPEN_HELP_IN_GITHUB` або `OPEN_LOCAL_HELP` і при цьому у директорії `./Doc` файлу з таким іменем не буде, то він буде створений автоматично

> [!important] 
> Ім'я Grasshopper файлу та Markdown файлу повинні збігатися!
