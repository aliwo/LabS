from swagger_ui_bundle import swagger_ui_3_path
import connexion
import prance
from typing import Any, Dict
from pathlib import Path


app = connexion.App(__name__, specification_dir='spec/', options={'swagger_path': swagger_ui_3_path})


def get_bundled_specs(main_file: Path) -> Dict[str, Any]:
    parser = prance.ResolvingParser(str(main_file.absolute()),
                                    lazy = True, strict = True)
    parser.parse()
    return parser.specification


app.add_api(get_bundled_specs(Path("spec/main.yaml")),
            resolver = connexion.RestyResolver("cms_rest_api"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
