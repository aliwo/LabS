from swagger_ui_bundle import swagger_ui_3_path
import connexion
import prance
from typing import Any, Dict
from pathlib import Path
import sentry_sdk
import os
from migration import migrate # 지우지마


if os.environ.get('SY_STAGE', '') == 'PRODUCTION':
    sentry_sdk.init("https://ff3db8501cc749f194820a7f4719d689@o390454.ingest.sentry.io/5233605")


app = connexion.App(__name__, specification_dir='api/spec/', options={'swagger_path': swagger_ui_3_path})


def get_bundled_specs(main_file: Path) -> Dict[str, Any]:
    parser = prance.ResolvingParser(str(main_file.absolute()),
                                    lazy = True, strict = True)
    parser.parse()
    return parser.specification


app.add_api(get_bundled_specs(Path("api/spec/main.yaml")),
            resolver = connexion.RestyResolver("cms_rest_api"))


