**深度学习项目框架**
deep_learning_project/
├── data/
│   ├── raw/                           # 原始数据
│   ├── processed/                     # 处理后的数据
│   └── pizza_steak_sushi/
│       ├── train/
│       │   ├── pizza/
│       │   │   ├── image01.jpeg
│       │   │   └── ...
│       │   ├── steak/
│       │   ├── sushi/
│       └── test/
│           ├── pizza/
│           ├── steak/
│           └── sushi/
├── models/                            # 训练好的模型
│   ├── tinyvgg/
│   │   ├── cell_mode/
│   │   │   └── model.pth
│   │   ├── script_mode/
│   │   │   └── model.pth
│   └── logs/                          # 训练日志
│       ├── run1/
│       └── run2/
├── notebooks/                         # Jupyter notebooks
│   ├── data_exploration.ipynb
│   ├── model_training.ipynb
│   └── model_evaluation.ipynb
├── scripts/                           # 独立脚本
│   ├── data_processing.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── predict.py
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── data_preprocessor.py
│   │   └── data_augmentation.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── tinyvgg.py
│   │   └── model_utils.py
│   ├── training/
│   │   ├── __init__.py
│   │   ├── train.py
│   │   ├── validate.py
│   │   └── metrics.py
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── evaluate.py
│   │   └── visualizations.py
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       ├── logger.py
│       └── helpers.py
├── tests/                             # 单元测试
│   ├── __init__.py
│   ├── test_data_loader.py
│   ├── test_model.py
│   ├── test_train.py
│   └── test_metrics.py
├── config/                            # 配置文件
│   ├── config.yaml
│   ├── logging.yaml
│   └── paths.yaml
├── requirements.txt                   # 依赖包
├── README.md                          # 项目说明
└── setup.py                           # 安装脚本
