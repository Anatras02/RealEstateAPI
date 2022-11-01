import os


def upload_to(path):
    def inner_upload_to(instance, filename):
        return os.path.join(path, instance.id)

    return inner_upload_to
