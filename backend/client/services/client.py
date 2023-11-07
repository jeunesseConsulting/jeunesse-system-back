from client.models import Client


class ClientServices:


    @staticmethod
    def query_all():
        return Client.objects.all()
    
    @staticmethod
    def get(id):
        try:
            client = Client.objects.get(id=id)
            return client
        except Client.DoesNotExist:
            return None

