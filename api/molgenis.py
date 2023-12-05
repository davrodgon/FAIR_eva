import molgenis.client as molgenis


class Molgenis():

    def __init__(self, url: str = "http://localhost/"):
        self.set_url(url)

    def connect(self):
        session = molgenis.Session(url + "/api/")
        session.login("username","password")

