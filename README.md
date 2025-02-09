# SGE_BLOC2
![image](https://github.com/user-attachments/assets/2cd0c476-c5a2-45bd-932b-9d8025dee015)
No se perque em dona error a la terminal, no l'entenc i no se com solucionar-ho, pero puc explicar el que fa el programa i la sortida d'aquest.

El programa utilitza un bucle for per recorrer cada fila dels resultats tornats per la consulta.
En cada iteració, imprimeix les dades d'una fila en un format estructurat:
Nom (i[1])
Direcció (i[2])
Teléfon (i[3])
Email (i[4]) 
Data naixement (i[5])
 
El resultat per exemple seria tal que així:
Nom: Joan Farssac
Adreça: Avinguda Major 54
telèfon: 987654321
email: joanfarssac@email.com
neixement: 09-05-2004
###################################################################
![image](https://github.com/user-attachments/assets/6f1afada-e338-4db1-81ce-b0f2d3dcfed3)
Aquest codi asigna un nou valor de telèfon (000000000) al client amb id_cliente = 1.
Retorna un missatge indicant que l'actualització és exitosa: {"Update successfuly"}.
###################################################################
![image](https://github.com/user-attachments/assets/f9986fbf-0901-4d15-a836-15cee7ade577)
Aquest codi és una funció que elimina un registre de la taula clients de la base de dades.
Es connecta a la base de dades utilitzant la funció connection_db().
Executa una consulta DELETE per eliminar el client 28 de la taula.
Aplica els canvis a la base de dades amb conn.commit().
Per últim retorna un missatge confirmant l'eliminació: {"Delete successfully"}.
