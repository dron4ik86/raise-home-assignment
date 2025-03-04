from dotenv import load_dotenv
import requests
from faker import Faker


def before_all(context):
    """
    This function is called once at the start of test execution and sets up:
    - Environment variables from .env file
    - Persistent HTTP session
    - Fake data generator for test data
    """
    load_dotenv()
    context.session = requests.Session()
    context.fake = Faker()


def after_all(context):
    """Runs once after all tests complete"""
    ...


def before_feature(context, feature):
    """Runs before each feature file executes"""
    ...


def after_feature(context, feature):
    """Runs after each feature completes"""
    ...


def before_scenario(context, scenario):
    """Runs before each scenario"""
    ...


def after_scenario(context, scenario):
    """Runs after each scenario"""
    ...


def before_step(context, step):
    """Runs before each test step"""
    ...


def after_step(context, step):
    ...
