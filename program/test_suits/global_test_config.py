from models.analyzer_config_models import *

CONFIG_TEMPLATES_PATH = "../config_templates/config.yaml"

SAMPLE_ANALYZER_CONFIG = AnalyzerConfig(
  base_directory="./",
  csv_files=[
    "sample_data.csv",
  ],
  value_column_name=[
    "value",
  ],
  export_column_name=[
    "namespace",
    "app_name",
  ],
  output_config=AnalyzerOutputConfig(
    print_output=True
  ),
  stats_config=AnalyzerStatsConfig(
    percentiles=[
      25,
      50,
      95,
    ],
  )
)