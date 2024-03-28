# o(n) space and time
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # posso usare lo stack
        ss = []
        st = []
        # ogni volta che trovo un elemento non # allora posso aggiungerlo
        # altrimenti faccio la pop dell'ultimo elemento
        for c in s:
            if c == '#' and len(ss) != 0:
                ss.pop()
            elif c != '#':
                ss.append(c)

        for c in t:
            if c == '#' and len(st) != 0:
                st.pop()
            elif c != '#':
                st.append(c)

        # poi passo a confrontare i due stack
        i = len(ss)
        j = len(st)
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            if ss.pop() != st.pop():
                return False

        if i > 0 or j > 0:
            return False
        return True


# soluzione due con O(1) space
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Funzione ausiliaria per trovare l'indice del prossimo carattere non annullato
        def next_valid_char_index(string: str, index: int) -> int:
            backspaces = 0
            while index >= 0:
                if string[index] == '#':
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1
                else:
                    break
                index -= 1
            return index

        # Inizializzazione degli indici per le due stringhe
        fs, ft = len(s) - 1, len(t) - 1

        # Scorrimento delle stringhe da destra verso sinistra
        while fs >= 0 or ft >= 0:
            # Trova l'indice del prossimo carattere non annullato per s
            fs = next_valid_char_index(s, fs)
            # Trova l'indice del prossimo carattere non annullato per t
            ft = next_valid_char_index(t, ft)

            # Se entrambe le stringhe sono terminate, restituisci True
            if fs < 0 and ft < 0:
                return True
            # Se solo una delle due stringhe è terminata, restituisci False
            if fs < 0 or ft < 0:
                return False
            # Se i caratteri corrispondenti sono diversi, restituisci False
            if s[fs] != t[ft]:
                return False

            # Passa al carattere precedente
            fs -= 1
            ft -= 1

        # Entrambe le stringhe sono state esaminate e non ci sono differenze
        return True


