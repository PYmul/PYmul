pymul/
│
├── pymul/
│   ├── __init__.py
│   ├── cli.py              # Entrada principal
│   ├── core/
│   │   ├── dispatcher.py   # Decide o que fazer
│   │   ├── os_detect.py    # Detecta SO
│   │   └── executor.py     # Executa comandos
│   │
│   ├── managers/
│   │   ├── base.py         # Classe abstrata
│   │   ├── pip_manager.py
│   │   ├── apt_manager.py
│   │   ├── brew_manager.py
│   │   └── choco_manager.py
│   │
│   └── commands/
│       ├── install.py
│       ├── env.py
│       ├── run.py
│       └── sysinfo.py
│
├── pyproject.toml
├── README.md
└── LICENSE