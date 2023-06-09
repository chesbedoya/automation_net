from sqlalchemy import MetaData, create_engine
import os

engine_automation_netsuite = create_engine(os.getenv('ENV_CONNECTION_STRING_AUTOMATION_LOCAL'))
metadata = MetaData()
