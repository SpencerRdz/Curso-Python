texto = "Hola, algo maravilloso está por suceder hoy"
sub_texto = texto[6:22] # Extrae el sub-string desde la posición 6 hasta la 21
print(sub_texto) # Imprime: algo maravilloso


sub_texto = texto[6:] # Extrae el sub-string desde la posición 6 hasta el final
print(sub_texto) # Imprime: algo maravilloso está por suceder hoy

sub_texto = texto[:4] # Extrae el sub-string desde el inicio hasta la posición 3
print(sub_texto) # Imprime: Hola

sub_texto = texto[6:22:2] # Extrae el sub-string desde la posición 6 hasta la 21, tomando cada 2 caracteres
print(sub_texto) # Imprime: ag aails

sub_texto = texto[::2] # Extrae el sub-string desde el inicio hasta el final, tomando cada 2 caracteres
print(sub_texto) # Imprime: Hl,ag aails sáprscdrhy

sub_texto = texto[::-1] # Extrae el sub-string desde el final hasta el inicio, invirtiendo el texto
print(sub_texto) # Imprime: yoh redecus rop átse osollivaram ogla ,aloH