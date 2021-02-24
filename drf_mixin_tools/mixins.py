

class ActionSerializerClassMixin:
    action_serializer_class = {}

    def get_serializer_class(self):
        if self.action_serializer_class and self.action in self.action_serializer_class:
            return self.action_serializer_class[self.action]
        return super(ActionSerializerClassMixin, self).get_serializer_class()


class ActionPermissionClassesMixin:
    action_permission_classes = {}

    def get_permissions(self):
        if self.action_permission_classes and self.action in self.action_permission_classes:
            permissions = self.action_permission_classes[self.action]
            return [permission() for permission in permissions]

        return super(ActionPermissionClassesMixin, self).get_permissions()
