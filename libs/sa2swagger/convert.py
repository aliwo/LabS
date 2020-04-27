from .utils import map_model, to_yaml


def convert(model, filepath, template=None):
    model_name = model.__name__.lower()
    if template is None:
        template = {model_name: {'description': '', 'properties':{}}}

    map = map_model(model)
    for key, val in map.items():
        if key in template[model_name]['properties']:
            template[model_name]['properties'][key]['type'] = val['type']
            continue

        template[model_name]['properties'][key] = {
            'type': val['type']
        }

    to_yaml(template, filepath)
    return template
