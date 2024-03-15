from django.apps import AppConfig


class PaymentMethodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payment_method'


    def ready(self):
        # Creating standard payment methods on initialization

        from payment_method.models import PaymentMethod

        methods_list = [
            'BOLETO',
            'CARTÃO DE CRÉDITO',
            'PIX',
            'CARTÃO DE DÉBITO',
        ]

        for method in methods_list:
            try:
                PaymentMethod.objects.create(
                    name = method
                )
            except:
                pass
