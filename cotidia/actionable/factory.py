import factory


class ActionableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'actionable.actionable'
