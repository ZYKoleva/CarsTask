import logging
import numpy as np
import pandas as pd


class DataHandler:
    def __init__(self, scope: str, data_logger: logging.Logger, data_config: dict):
        """

        Parameters
        ----------
        scope (str) - String representing the scope of data. To be used in log messages
        data_logger (logging.Logger) - Represents instance of the data logger
        data_config (dict) - Dictionary holding the config[data_file].yaml data
        """
        self.scope = scope
        self.data_logger = data_logger
        self.data_config = data_config

    def has_column_numeric_values(self, df: pd.DataFrame, column_name: str) -> None:
        check = np.issubdtype(df[column_name].dtype, np.number)
        if check:
            self.data_logger.info(f'Values in column {column_name} are numeric')
        else:
            self.data_logger.info(f'Values in column {column_name} are NOT numeric')
            raise ValueError(f'Values in column {column_name} are NOT numeric')

    def has_column_string_values(self, df: pd.DataFrame, column_name: str) -> None:
        check = np.issubdtype(df[column_name].dtype, np.str)
        if check:
            self.data_logger.info(f'Values in column {column_name} are strings')
        else:
            self.data_logger.info(f'Values in column {column_name} are NOT strings')
            raise ValueError(f'Values in column {column_name} are NOT strings')

    def check_required_columns(self, df: pd.DataFrame) -> None:
        """
        This methods checks if the dataframe contains all required columns that are passed as params to methods.
        If there are missing columns in the dataframe, raise ValueError

        Parameters
        ----------
        df (pd.DataFrame) - dataframe containing the input raw data
        Returns
        -------
        None
        """
        columns = self.data_config['columns']
        df_columns = df.columns.values.tolist()
        missing_cols = [x for x in columns if x not in df_columns]
        if missing_cols:
            msg = f'Data Quality Check Failed. Missing columns in dataframe: {missing_cols}'
            self.data_logger.info(msg)
            raise ValueError(msg)
        else:
            msg = 'Data Quality Check Passed'
            self.data_logger.info(msg)

    def get_unique_number(self, df: pd.DataFrame, column_name: str) -> None:
        """
        This method counts unique values in the specified column
        No restriction of value types
        Parameters
        ----------
        df (pd.DataFrame) - dataframe containing the input raw data
        column_name (str) - String representing the name of the specified column

        Returns
        -------
        None
        """
        try:
            unique_number_col = df[column_name].nunique()
            self.data_logger.info(msg=f'The number of unique {column_name.lower()} is {unique_number_col}')
        except Exception as err:
            msg = f"The following exception occurred during the execution of the 'get_unique_number' function: {err}"
            self.data_logger.error(msg)
            raise Exception(msg)

    def get_average(self, df: pd.DataFrame, column_name: str) -> None:
        """
        This method calculates the average value for values in the specified column
        Values should be numeric
        Parameters
        ----------
        df (pd.DataFrame) - dataframe containing the input raw data
        column_name (str) - String representing the name of the specified column

        Returns
        -------
        None
        """
        try:
            self.has_column_numeric_values(df, column_name)
            average_col = df[column_name].mean()
            self.data_logger.info(msg=f'The average {column_name.lower()} of all the {self.scope} is {average_col}')
        except Exception as err:
            msg = f"The following exception occurred during the execution of the 'get_average' function: {err}"
            self.data_logger.error(msg)
            raise Exception(msg)

    def get_top_max(self, df: pd.DataFrame, numeric_column_name: str, name_column: str, n_top: int) -> None:
        """
        Method gets the first n rows with the largest values in columns, in descending order and returns
         the values for the name_column.

        Parameters
        ----------
        df (pd.DataFrame) - dataframe containing the input raw data
        numeric_column_name (str) - String representing the name of a specified column holding numeric values
        column_name (str) - String representing the name of the specified column

        Returns
        -------
        None
        """
        try:
            self.has_column_numeric_values(df, numeric_column_name)
            res = df.nlargest(n_top, numeric_column_name, keep='first')
            self.data_logger.info(f'The top {n_top} most {numeric_column_name.lower()} {self.scope} are {res[name_column].values}')
        except Exception as err:
            msg = f"The following exception occurred during the execution of the 'get_top_max' function: {err}"
            self.data_logger.error(msg)
            raise Exception(msg)

    def get_count_by_value(self, df: pd.DataFrame, column_name: str) -> None:
        """
        Method counts the occurrence of a value in a specified column.

        Parameters
        ----------
        df (pd.DataFrame) - dataframe containing the input raw data
        column_name (str) - String representing the name of the specified column

        Returns
        -------
        None
        """
        try:
            res = df.groupby(column_name)[column_name].count()
            self.data_logger.info(f'The number of {self.scope} made by each {column_name.lower()} is {res.to_dict()}')
        except Exception as err:
            msg = f"The following exception occurred during the execution of the 'get_count_by_value' function: {err}"
            self.data_logger.error(msg)
            raise Exception(msg)

    def get_count_by_year(self, df: pd.DataFrame, column_name: str) -> None:
        """
        Method creates additional column Ýear' from the column specified as param and counts the occurrence of a value
         in 'Ýear' column.

        Parameters
        ----------
        df (pd.DataFrame) - dataframe containing the input raw data
        column_name (str) - String representing the name of the specified column holding dates as strings in format '%Y-%m-%d'

        Returns
        -------
        None
        """
        try:
            # Will throw an error if not in correct format
            df[column_name] = pd.to_datetime(df[column_name], format=self.data_config['date_format'])
            df['Year'] = df[column_name].dt.year
            res = df.groupby('Year')['Year'].count()
            self.data_logger.info(f'The number of {self.scope} made each {column_name.lower()} is {res.to_dict()}')
        except Exception as err:
            msg = f"The following exception occurred during the execution of the 'get_count_by_year' function: {err}"
            self.data_logger.error(msg)
            raise Exception(msg)
