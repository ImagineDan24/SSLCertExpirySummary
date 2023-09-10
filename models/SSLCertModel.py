class SSLCert:
    def __init__(self, id, name, address, port, environment, environmentId, team, expiryDate = '', daysLeft = ''):
        self.id = id
        self.name = name
        self.address = address
        self.port = port
        self.environment = environment
        self.environmentId = environmentId
        self.team = team
        self.expiryDate = expiryDate
        self.daysLeft = daysLeft