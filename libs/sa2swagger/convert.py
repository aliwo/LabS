from .utils import map_model, to_yaml


def convert(model, filepath, template=None):
    if template is None:
        template = {'description': '', 'properties':{}}

    map = map_model(model)
    for key, val in map.items():
        if key in template['properties']:
            template['properties'][key]['type'] = val['type']
            continue

        template['properties'][key] = {
            'type': val['type']
        }

    to_yaml(template, filepath)
    return template
