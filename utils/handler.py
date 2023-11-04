import pandas as pd


class DataHandler:
    def __init__(self, data_logger, data_config: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_logger = data_logger
        self.data_config = data_config

    def check_data_completeness(self, df: pd.DataFrame) -> None:
        columns = self.data_config['columns']
        df_columns = df.columns.values.tolist()
        missing_cols = [x for x in columns if x not in df_columns]
        if missing_cols:
            msg = f'Data Quality Check Failed. Missing columns in dataframe: {missing_cols}'
        else:
            msg = 'Data Quality Check Passed'
        self.data_logger.info(msg)

    def validate_schema(self, df: pd.DataFrame) -> bool:
        """TO DO"""

    def get_unique_number(self, df: pd.DataFrame, column_name: str) -> None:
        try:
            unique_number_col = df[column_name].nunique()
            self.data_logger.info(msg=f'The number of unique cars is {unique_number_col}')
        except Exception as err:
            msg = f"The following exception occurred during the execution of the 'get_unique_number' function: {err}"
            self.data_logger.error(msg)
            raise Exception(msg)

    def get_average(self, df: pd.DataFrame, column_name: str) -> None:
        try:
            average_col = df[column_name].mean()
            self.data_logger.info(msg=f'The average horse power of all the cars is {average_col}')
        except Exception as err:
            msg = f"The following exception occurred during the execution of the 'get_average' function: {err}"
            self.data_logger.error(msg)
            raise Exception(msg)

    def get_top_max(self, df: pd.DataFrame, numeric_column_name: str, label_column: str, n_top: int) -> None:
        try:
            df[numeric_column_name].sort_values(ascending=False)
            res = df.nlargest(n_top, numeric_column_name, keep='first')
            self.data_logger.info(f'The top {n_top} most heaviest cars are {res[label_column].values}')
        except Exception as err:
            msg = f"The following exception occurred during the execution of the 'get_top_max' function: {err}"
            self.data_logger.error(msg)
            raise Exception(msg)

    def get_count_by_value(self, df: pd.DataFrame, column_name: str) -> None:
        try:
            res = df.groupby(column_name)[column_name].count()
            self.data_logger.info(f'The number of cars made by each manufacturer is {res.to_dict()}')
        except Exception as err:
            msg = f"The following exception occurred during the execution of the 'get_count_by_value' function: {err}"
            self.data_logger.error(msg)
            raise Exception(msg)

    def get_count_by_year(self, df: pd.DataFrame, column_name: str) -> None:
        try:
            df[column_name] = pd.to_datetime(df[column_name], format='%Y-%m-%d')
            df['Year'] = df[column_name].dt.year
            res = df.groupby('Year')['Year'].count()
            self.data_logger.info(f'The number of cars made each year is {res.to_dict()}')
        except Exception as err:
            msg = f"The following exception occurred during the execution of the 'get_count_by_year' function: {err}"
            self.data_logger.error(msg)
            raise Exception(msg)
