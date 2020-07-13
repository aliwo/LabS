from api.app import app as api_app
from admin.app import app as admin_app

if __name__ == '__main__':
    admin_app.run(host='0.0.0.0', port=8000)
