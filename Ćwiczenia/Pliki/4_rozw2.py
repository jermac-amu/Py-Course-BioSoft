available_fruits = ["Lychee", "Apple", "Mango", "Pear", "Pineapple", "Peach",
                    "Nectarine", "Orange","Lychee", "Papaya", "Pineapple",
                    "Peach", "Pear", "Pineapple", "Apple", "Mandarine", "Plum",
                    "Melon", "Passionfruit", "Nectarine", "Plum"]

wrong_fruits1 = {"Peach", "Nectarine", "Orange", "Pineapple", "Melon"}
wrong_fruits2 = {"Mandarine", "Plum", "Lychee", "Orange", "Peach", "Papaya"}

available_set = set(available_fruits)

liked_fruits1 = available_set.difference(wrong_fruits1)
# Również poprawne:
liked_fruits1 = available_set - wrong_fruits1

liked_fruits_both = liked_fruits1.difference(wrong_fruits2)
# lub
liked_fruits_both = liked_fruits1 - wrong_fruits2

print(liked_fruits_both)
# {'Passionfruit', 'Mango', 'Apple', 'Pear'}
# To bedzie bardzo słodka sałatka...
