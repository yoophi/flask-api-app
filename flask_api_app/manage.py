from flask_script import Manager as BaseManager


class ManagerWrapper(object):
    manager = None

    @classmethod
    def init(cls, app):
        if not cls.manager:
            cls.manager = BaseManager(app)

        return cls.manager


def Manager(app):
    return ManagerWrapper.init(app)
