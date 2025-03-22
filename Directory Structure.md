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



目录结构说明
data/: 数据存储目录。

raw/: 存放原始数据。
processed/: 存放处理后的数据。
pizza_steak_sushi/: 示例数据集，包括训练和测试数据。
models/: 模型相关文件目录。

tinyvgg/: 存放TinyVGG模型的不同版本。
logs/: 训练日志。
notebooks/: Jupyter Notebooks，用于数据探索、模型训练和评估。

scripts/: 独立脚本，用于数据处理、模型训练、评估和预测。

src/: 主要代码目录。

data/: 数据处理相关模块。
models/: 模型定义和相关工具模块。
training/: 训练和验证相关模块。
evaluation/: 评估和可视化相关模块。
utils/: 通用工具和配置模块。
tests/: 单元测试目录。

config/: 配置文件目录，包括项目配置和日志配置等。

requirements.txt: 项目依赖包列表。

README.md: 项目说明文档。

setup.py: 项目安装脚本。
