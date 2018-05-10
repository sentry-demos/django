from raven.contrib.django import DjangoClient as OriginalDjangoClient

class DjangoClient(OriginalDjangoClient):
    """
    Add user info from context.
    """
    def get_user_info(self, request, *args, **kwargs):
        user_info = super(DjangoClient, self).get_user_info(request, *args, **kwargs)
        if "user" in self.context.data:
            user_info.update(self.context.data["user"])
        return user_info