email = input("Donner l'email: ")
prenom = email[:email.find(".")]
nom = email[email.find(".")+1:email.find("@")]
service = email[email.find("@")+1:]
print(prenom, nom, service)
