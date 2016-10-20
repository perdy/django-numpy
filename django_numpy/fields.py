from django.contrib.postgres.fields import ArrayField

try:
    from numpy import array
except ImportError:
    array = list


class NumpyArrayField(ArrayField):
    def __init__(self, base_field, size=None, **kwargs):
        super(NumpyArrayField, self).__init__(base_field, size, **kwargs)

    @property
    def description(self):
        return 'Numpy array of %s' % self.base_field.description

    def get_db_prep_value(self, value, connection, prepared=False):
        return super(NumpyArrayField, self).get_db_prep_value(list(value), connection, prepared)

    def deconstruct(self):
        name, path, args, kwargs = super(NumpyArrayField, self).deconstruct()
        kwargs.update({
            'base_field': self.base_field,
            'size': self.size,
        })
        return name, path, args, kwargs

    def to_python(self, value):
        return super(NumpyArrayField, self).to_python(array(value))

    def value_to_string(self, obj):
        return super(NumpyArrayField, self).value_to_string(list(obj))
