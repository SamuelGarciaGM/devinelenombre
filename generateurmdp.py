# Import the random library.
import random

# Définissez une fonction pour générer un mot de passe aléatoire.
def generate_password(length):
  """Génère un mot de passe aléatoire de la longueur donnée.

  Arguments :
    longueur : La longueur du mot de passe.

  Retour:
    Un mot de passe aléatoire de la longueur donnée.
  """

  # Créez une liste de tous les caractères possibles.
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}|:<>?,./;'[]"

  # Créez un mot de passe aléatoire de la longueur donnée.
  password = ""
  for i in range(length):
    password += random.choice(characters)

  # Renvoyez le mot de passe.
  return password

# Si le programme est exécuté en tant que programme principal, exécutez la fonction principale.
if __name__ == "__main__":

  # Obtenez la longueur du mot de passe de l'utilisateur.
  length = int(input("Saisissez la longueur du mot de passe : "))

  # Générez un mot de passe de la longueur donnée.
  password = generate_password(length)

  # Print le mot de passe
  print("Votre mot de passe est :", password)