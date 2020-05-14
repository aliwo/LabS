import sqlalchemy.sql.sqltypes as sqltypes
from libs.database.types import LaboratoryTypes
import yaml


def map_sqltypes(column_type):
    if isinstance(column_type, sqltypes.Integer):
        return 'integer'
    elif isinstance(column_type, sqltypes.SmallInteger) or isinstance(column_type, sqltypes.Boolean):
        return 'boolean'
    elif isinstance(column_type, sqltypes.String):
        return 'string'
    elif isinstance(column_type, sqltypes.DateTime):
        return 'string'
    elif isinstance(column_type, sqltypes.Date):
        return 'string'
    elif isinstance(column_type, sqltypes.Time):
        return 'string'
    elif isinstance(column_type, LaboratoryTypes.TextTuple):
        return 'string'
    elif isinstance(column_type, LaboratoryTypes.IntTuple):
        return 'string'
    else:
        raise TypeError(f'Mapping failed: Unknown Column Type: {column_type}')


def map_model(sa_model):
    mapped_fields = {}

    for column in sa_model.__table__.columns:
        mapped_fields[column.name] = {
            "type": map_sqltypes(column.type),
            "auto_increment": str(column.autoincrement) == "True",
            "nullable": bool(column.nullable),
            "default": bool(column.default),
        }

    return mapped_fields


def to_yaml(map, filepath):
    with open(filepath, 'w+') as outfile:
        yaml.dump(map, outfile, default_flow_style=False)
