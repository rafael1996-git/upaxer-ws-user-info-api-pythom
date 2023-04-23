class UserBank:
    def __init__(self, idUser, idBank, depositAccount, clabe, paypalAccount, cardNumber, userModified):
        self.idUser = idUser
        self.idBank = idBank
        self.depositAccount = depositAccount
        self.clabe = clabe
        self.paypalAccount = paypalAccount
        self.cardNumber = cardNumber
        self.userModified = userModified

    def create(self):
        return {
            "idUser": self.idUser,
            "idBank": self.idBank,
            "depositAccount": self.depositAccount,
            "clabe": self.clabe,
            "paypalAccount": self.paypalAccount,
            "cardNumber": self.cardNumber,
            "userModified": self.userModified

        }
