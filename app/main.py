import datetime
from utils.logger import Logger
from utils.helper import FilesHelper
from utils.handler import DataHandler


log_file_path = './logs/app_logs.log'
config_file_path = './config/config.yaml'

file_logger = Logger(log_file_path).get_logger('file_logger')
run_logger = Logger(log_file_path).get_logger('run_logger')
data_logger = Logger(log_file_path).get_logger('data_logger')


def run():

    file_handler = FilesHelper(file_logger)
    file_handler.read_config_file(file_path=config_file_path)
    file_handler.read_config_file(file_path=config_file_path)

    try:
        start_time = datetime.datetime.now()
        run_logger.info(f'Program execution started: {start_time}')
        data_file_conf = file_handler.config_file['data_file']
        file_handler.read_data_file(
            file_name=data_file_conf['file_name'],
            file_path=data_file_conf['file_path'],
            file_type=data_file_conf['file_type'],
            orientation=data_file_conf['orientation']
        )

        df = file_handler.data_df
        data_handler = DataHandler('cars', data_logger, data_file_conf)
        data_handler.check_required_columns(df)

        fn_params = file_handler.config_file['functions_params']
        data_handler.get_unique_number(
            df=df,
            column_name=fn_params['get_unique_number']['column']
        )
        data_handler.get_average(
            df=df,
            column_name=fn_params['get_average']['column'])

        data_handler.get_top_max(
            df=df,
            numeric_column_name=fn_params['get_top_max']['sort_by'],
            name_column=fn_params['get_top_max']['group_by'],
            n_top=fn_params['get_top_max']['top_n']
        )
        data_handler.get_count_by_value(
            df=df,
            column_name=fn_params['get_count_by_value']['column']
        )
        data_handler.get_count_by_year(
            df=df,
            column_name=fn_params['get_count_by_year']['column']
        )

        output_file_conf = file_handler.config_file['output_file']
        file_handler.save_data_file(
            df=df,
            file_name=output_file_conf['name'],
            file_path=output_file_conf['file_path'],
            file_type=output_file_conf['file_type']
        )

        end_time = datetime.datetime.now()
        total_exec = end_time - start_time

        run_logger.info(f'Program execution ended: {start_time}')
        run_logger.info(f'Overall execution time: {total_exec}')

    except Exception as err:
        msg = f'The following exception occurred during execution of the program: {err}'
        run_logger.error(msg)
        raise Exception(msg)

