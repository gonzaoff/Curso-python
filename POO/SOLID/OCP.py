# Principio de abirto/cerrado (open/close principle)
# La nocion de que las "entidades de software" deben estar abiertas para su extencion
# pero cerradas para su modificacion 

class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    def notificar(self):
        raise NotImplementedError

# Casa clase hereda de notificador agregando
## o modificando la funcion "notificar"
class NotificadorMail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.email}")

class NotificadorFace(Notificador):
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.face}")

class NotificadorWSP(Notificador):
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.whatsapp}")

class NotificadorTW(Notificador):
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.twitter}")







