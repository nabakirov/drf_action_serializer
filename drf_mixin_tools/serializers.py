from rest_framework import serializers
from collections.abc import Iterable


class ChoiceField(serializers.ChoiceField):

    def __init__(self, choices, multi=False, **kwargs):
        self.multi = multi
        super().__init__(choices, **kwargs)

    def _multi_choice_string_to_values(self, data, allow_default=False):
        if isinstance(data, str):
            items = data.split(',')
        elif isinstance(data, Iterable):
            items = data
        else:
            items = (data,)
        values = []
        for item in items:
            if allow_default:
                value = self.choice_strings_to_values.get(item, item)
            else:
                try:
                    value = self.choice_strings_to_values[item]
                except KeyError:
                    self.fail('invalid_choice', input=item)
            values.append(value)
        return values

    def to_internal_value(self, data):
        if not self.multi:
            return super().to_internal_value(data)
        if data == '' and self.allow_blank:
            return ''
        return self._multi_choice_string_to_values(data)

    def to_representation(self, value):
        if not self.multi:
            return super().to_representation(value)
        if value in ('', None):
            return value
        return self._multi_choice_string_to_values(value, allow_default=True)



