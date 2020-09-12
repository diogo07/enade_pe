
class Universidade:

    def __init__(self, codigoIES, codigoCategoria, codigoOrganizacaoAcademica, municipio, uf):
        self.id = None
        self.codigoIES = codigoIES
        self.codigoCategoria = codigoCategoria
        self.codigoOrganizacaoAcademica = codigoOrganizacaoAcademica
        self.municipio = municipio
        self.uf = uf

    def getValues(self):
        return (
            self.codigoIES,
            self.codigoCategoria,
            self.codigoOrganizacaoAcademica,
            self.municipio,
            self.uf
        )