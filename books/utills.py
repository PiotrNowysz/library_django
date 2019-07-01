import hashlib
import os


def make_md5(file_obj):
    return hashlib.md5(file_obj.read()).hexdigest()


def get_upload_file_hashdir(instance, filename):
    """Returns file path, for example 06e8fe4cd21df53c27ec038f66ed691a will return:
         06/e8/fe/06e8fe4cd21df53c27ec038f66ed691a.jpg"""

    hash_md5 = instance.md5  # make_md5(instance.stream.file)
    # print('hash_md5', hash_md5)
    ext = instance.cover.file.name.split('.')[-1]
    return os.path.join(hash_md5[:2], hash_md5[2:4], hash_md5[4:6],
                        '%s.%s' % (hash_md5, ext.lower()))  # instance.stream.name)
