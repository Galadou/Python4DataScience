def ft_filter(function, iterable):
    for item in iterable:
        if (function(item)):
            yield (item)

#yield = renvoie la valeur, et attend qu'on reappel la fonction
#pour refaire la fonction la ou il s'etait arreter