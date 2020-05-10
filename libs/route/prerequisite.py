from functools import wraps

class prerequisites:

    def __init__(self, inspector, func_name):
        '''
        주의! 반드시 @route 아래에 설치해야 합니다.
        '''
        self.inspector = inspector()
        self.inspect_func_name = func_name

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            getattr(self.inspector, self.inspect_func_name)()
            g.pr_result = self.inspector.get_result()
            return func(*args, **kwargs)
        return decorated

