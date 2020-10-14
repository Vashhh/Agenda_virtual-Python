import csv
# Importamos csv para importar y exportar documentos csv para guardar nuestros contactos.

class Contact:
# Generamos la clase contacto la cual tendra los parametros basicos e cada contacto a agregar.
    def __init__(self, name, number, email, direccion, codigo_postal):
        self.name = name
        self.number = number
        self.email = email
        self.direccion = direccion
        self.codigo_postal = codigo_postal

class ContactBook:

    def __init__(self):
        self._contacts = []
#creamos el metodo para agregar el contacto.
    def add(self, name, number, email, direccion, codigo_postal):
        contact = Contact(name, number, email, direccion, codigo_postal)
        self._contacts.append(contact)
        self._save()
#metodo para mostrar contactos
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
#metodo para borrar contactos, iterando en el idice de los contactos e indicando que todas las letras sean minusculas
    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

#metodo para buscar el contacto por el nombre enviando la solicitud al sistema en minusculas.
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()
#metodo para guardar el contacto en archivo con la extenc csv.
    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f,lineterminator = '\r')
            writer.writerow ( ('name', 'number', 'email', 'direccion', 'codigo_postal') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.number, contact.email, contact.direccion, contact.codigo_postal) )
    
    def _print_contact(self, contact):
        print("/////*****-----.....-----*****//////////*****-----.....-----*****/////")
        print("Nombre: {}".format(contact.name))
        print("Numero: {}".format(contact.number))
        print("Correo electronico: {}".format(contact.email))
        print("Direccion: {}".format(contact.direccion))
        print("Codigo Postal: {}". format(contact.codigo_postal))
        print("/////*****-----.....-----*****//////////*****-----.....-----*****/////")

    def _not_found(self):
        print("*******")
        print("¡¡No encontrado!!")
        print("*******")

def run():

    contact_book = ContactBook()
    
    with open ('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            contact_book.add(row[0], row[1], row[2], row[3], row[4])


    while True:
        command = str(input('''
                ¿Que deseas hacer?
                
                [a]ñadir contacto
                [ac]tualizar contacto
                [b]uscar contacto
                [e]liminar contacto
                [l]istar contacto
                [s]alir
        '''))
        if command == 'a':
            name = str(input("Escribe el nombre del contacto. "))
            number = str(input("Escribe el numero del contacto. "))
            email = str(input("Escriba el correo electronico del contacto. "))
            direccion = str(input("Escriba la direccion del contacto. "))
            codigo_postal = str(input("Escriba el codigo postal del contacto. "))
           
            contact_book.add(name, number, email, direccion, codigo_postal)
        
        elif command == 'ac':
            print("CONTACTO ACTUALIZADO")
        elif command =='b':
             name = str(input("Escribe el nombre del contacto. "))

             contact_book.search(name)

        elif command == 'e':
            name = str(input("Escribe el nombre del contacto. "))

            contact_book.delete(name)

        elif command == 'l':
            
            contact_book.show_all()

        elif command =='s':
            break
        else:
            print("Comando no encontrado.")


if __name__ =='__main__':
    print("B I E N V E N I D O   A   L A   A G E N D A")
    run()