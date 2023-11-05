import yaml
import pytest
import pandas as pd
from utils.logger import Logger
from utils.handler import DataHandler
from utils.helper import FilesHelper


config_file_path = './config/config.yaml'
log_file_path = './test/test_logs.log'

test_logger = Logger(log_file_path).get_logger('test_logger')

@pytest.fixture
def config_file():
    """
    Reads the configuration file (yaml format)
    Returns
    -------
    dict
    """
    with open(config_file_path, 'r+') as conf_file:
        config = yaml.safe_load(conf_file)
    return config


@pytest.fixture
def test_df(config_file):
    """
    Creates instance of the FilesHelper, reads raw data file (json format)
    Parameters
    ----------
    config_file (dict): Dictionary containing data_file configurations

    Returns
    -------
    dataframe instance (pd.DataFrame)
    """
    file_helper = FilesHelper(test_logger)
    data_file_conf = config_file['data_file']
    file_helper.read_data_file(
        file_name=data_file_conf['file_name'],
        file_path=data_file_conf['file_path'],
        file_type=data_file_conf['file_type'],
        orientation=data_file_conf['orientation']
    )
    return file_helper.data_df


def test_dataset_is_instance_df(config_file, test_df):
    """
    Test asserts dataset passed is of type pd.Dataframe
    Parameters
    ----------
    config_file (dict): Dictionary representing the
    test_df (pd.DataFrame): Dataset from the raw data yaml file
    """
    df = test_df.copy(deep=True)
    assert isinstance(df, pd.DataFrame)


def test_check_required_columns_missing_col(config_file, test_df):
    """
    Test asserts method with raise ValueError because of missing column in dataset
    Parameters
    ----------
    config_file (dict): Dictionary representing the
    test_df (pd.DataFrame): Dataset from the raw data yaml file
    """
    df = test_df.copy(deep=True)
    config = config_file
    config['data_file']['columns'].append('NonExistingColumn')
    data_handler = DataHandler('cars', test_logger, config['data_file'])
    with pytest.raises(ValueError):
        data_handler.check_required_columns(df)


def test_check_required_columns_no_missing_col(config_file, test_df, caplog):
    """
    Test asserts check passes successful
    Parameters
    ----------
    config_file (dict): Dictionary representing the
    test_df (pd.DataFrame): Dataset from the raw data yaml file
    caplog: used to access and control log capturing
    """
    df = test_df.copy(deep=True)
    config = config_file
    config['data_file']['columns'].pop()
    data_handler = DataHandler('cars', test_logger, config['data_file'])
    data_handler.check_required_columns(df)
    assert 'Data Quality Check Passed' in caplog.text


def test_get_unique_number_correct_col1(config_file, test_df, caplog):
    """
    Test asserts method returns correct number of unique values in the specified column
    Parameters
    ----------
    config_file (dict): Dictionary representing the
    test_df (pd.DataFrame): Dataset from the raw data yaml file
    caplog: used to access and control log capturing
    """
    df = test_df.copy(deep=True)
    config = config_file
    data_handler = DataHandler('cars', test_logger, config['data_file'])
    unique_vals = set(df['Origin'].values.tolist())
    data_handler.get_unique_number(df, column_name='Origin')
    assert f'The number of unique origin is {len(unique_vals)}' in caplog.text


def test_get_unique_number_correct_col2(config_file, test_df, caplog):
    """
    Test asserts method returns correct number of unique values in the specified column
    Parameters
    ----------
    config_file (dict): Dictionary representing the
    test_df (pd.DataFrame): Dataset from the raw data yaml file
    caplog: used to access and control log capturing
    """
    df = test_df.copy(deep=True)
    config = config_file
    data_handler = DataHandler('cars', test_logger, config['data_file'])
    data_handler.get_unique_number(df, column_name='Name')
    unique_vals = set(df['Name'].values.tolist())
    assert f'The number of unique name is {len(unique_vals)}' in caplog.text


def test_get_unique_number_exception_raised_no_col(config_file, test_df, caplog):
    """
    Test asserts method raises Exception because of missing column
    Parameters
    ----------
    config_file (dict): Dictionary representing the
    test_df (pd.DataFrame): Dataset from the raw data yaml file
    caplog: used to access and control log capturing
    """
    df = test_df.copy(deep=True)
    config = config_file
    data_handler = DataHandler('cars', test_logger, config['data_file'])
    with pytest.raises(Exception):
        data_handler.get_unique_number(df, column_name='NonExistingColumn')


""" TO DO:  Write tests for the other 4 methods of DataHandler """

