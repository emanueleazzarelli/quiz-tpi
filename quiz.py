# # Gli studenti dovranno creare un semplice gioco a quiz in cui le domande e le risposte vengono lette da un file di testo. Il programma dovrebbe: * Leggere le domande e le
# risposte dal file. * Presentare le domande all’utente. * Verificare se la risposta dell’utente è corretta. *
# Tenere traccia del punteggio dell’utente. * Visualizzare il punteggio finale al termine del quiz. 



file_path="quiz.txt"

with open(file_path, "r", encoding="utf-8") as file:
    quiz = []

    while True:
        domanda = file.readline()
        if domanda == "":
            break

        domanda = domanda.strip()
        if domanda == "":
            break

        opzioni = []
        for i in range(4):
            opzione = file.readline().strip()
            opzioni.append(opzione)

        risposta_line = file.readline()
        riga = risposta_line.strip()

        if "Risposta corretta:" in riga:
            risposta_corretta = riga.split("Risposta corretta:")[1].strip()
        else:
            risposta_corretta = ""

        file.readline()

        quiz.append((domanda, opzioni, risposta_corretta))

punteggio = 0
for i, (domanda, opzioni, risposta_corretta) in enumerate(quiz):
    print("\nDomanda" , i + 1, ":" , domanda)
    for opzione in opzioni:
        print(opzione)

    risposta_utente = input("La tua risposta (a/b/c/d): ").strip().lower()

    if risposta_utente == risposta_corretta.lower():
        print(" Risposta corretta!")
        punteggio += 1
    else:
        print(" Risposta sbagliata! La risposta giusta era: ",risposta_corretta)

print("\nHai totalizzato" ,punteggio," punti su" ,len(quiz),".")

 
 