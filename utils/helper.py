import yaml
import pandas as pd


class FilesHelper:
    def __init__(self, file_logger, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config_file = ''
        self.data_df = ''
        self.file_logger = file_logger

    def read_config_file(self, file_path: str):
        file_type = file_path.split('.')[-1]
        try:
            if file_type == 'json':
                '''TO DO'''

            if file_type == 'csv':
                '''TO DO'''

            if file_type == 'yaml':
                with open(file_path, 'r') as conf_file:
                    config = yaml.safe_load(conf_file)
                    self.config_file = config
                self.file_logger.info(msg=f"Configuration file '{file_path.split('/')[-1]}' was successfully read.")

        except Exception as err:
            msg = f"The following exception occurred during the execution of 'read_config_file' function for file '{file_path}': {err}"
            self.file_logger.error(msg)
            raise Exception(msg)

    def read_data_file(self, file_name: str, file_path: str, file_type: str, orientation: str = None):
        full_file_path = f'{file_path}/{file_name}.{file_type}'
        try:
            if file_type == 'json':
                df = pd.read_json(full_file_path, orient=orientation)
                self.data_df = df
                self.file_logger.info(msg=f"Data file '{file_name}.{file_type}' was successfully read.")
            if file_type == 'csv':
                df = pd.read_csv(file_path)
                self.data_df = df
            if file_type == 'xlsx':
                df = pd.read_excel(file_path)
                self.data_df = df
        except Exception as err:
            msg = f"The following exception occurred during the execution of 'read_data_file' function for file '{file_path}': {err}"
            self.file_logger.error(msg)
            raise Exception(msg)

    def save_data_file(self, df: pd.DataFrame, file_name: str, file_path: str, file_type: str):
        full_file_path = f'{file_path}/{file_name}.{file_type}'
        try:
            msg = f"Dataframe was saved as '{file_type}' in the following location: '{full_file_path}'"
            if file_type == 'csv':
                df.to_csv(full_file_path)
                self.file_logger.info(msg)
            elif file_type == 'json':
                '''TO DO'''

        except Exception as err:
            msg = f"Exception occurred during the execution of 'save_data_file' function. Failed to save '{file_name}.{file_type}' to" \
                  f" '{full_file_path}': {err}"
            self.file_logger.error(msg)
            raise Exception(msg)



