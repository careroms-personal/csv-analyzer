import pandas as pd
from pathlib import Path
from models.analyzer_config_models import *

class StatsAnalyzeExecutor:
  def __init__(self, analyzer_config: AnalyzerConfig):
    self.analyzer_config = analyzer_config
    self.stats_config = analyzer_config.stats_config

  def _analyze_data(self):
    for file in self.analyzer_config.csv_files:
      df = pd.read_csv(Path(self.analyzer_config.base_directory) / file)

      for keys, group_df in df.groupby(self.analyzer_config.export_column_name):
        result = {}
        series = group_df["value"]
        
        for col, key in zip(self.analyzer_config.export_column_name, keys):
          result[col] = key
        
        if self.stats_config.avg:
          result["avg"] = series.mean()
        if self.stats_config.std:
          result["std"] = series.std()
        if self.stats_config.min:
          result["min"] = series.min()
        if self.stats_config.max:
          result["max"] = series.max()
        if self.stats_config.cov:
          result["cov"] = series.std() / series.mean()
        if self.stats_config.percentiles:
          for pct in self.stats_config.percentiles:
            result[f"p{pct}"] = series.quantile(pct/100)

        print(result)


  def execute(self):
    self._analyze_data()