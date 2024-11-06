class DataMixin:

    def get_mixin_context(self, context, **kwargs):
        context.update(kwargs)
        return context