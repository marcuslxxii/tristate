#!/usr/bin/env python3

# Lunghezza tot: 79 caratteri
# 34567890123456789012345678901234567890123456789012345678901234567890123456789

# Lunghezza delle Docstring: 72 caratteri
# 3456789012345678901234567890123456789012345678901234567890123456789012

__author__ = 'Marco Garipoli marcuslxxii@gmail.com'

__version__ = "$Revision: 000000000001 $"  # 17/12/2017
# $Source$


class Tristate():
    """
    Implementa la classe Tristate, ovvero un valore booleano che, oltre
    ai valori True e False,gestisce anche il valore None che corrisponde
    a 'sconosciuto'. Dunque può assure i valori [True, False, None].
    Dunque questa classe implementa la logica a tre valori di Kleene.
    
    La funzione not si può fare usando istanza.not_().
    Le funzioni and, or e xor si possono fare usando rispettivamente &,
    | e ^.
    La funzione implica si può fare usando istanza.imp(altro).
    
    esempi:
    a = Tristate(True)
    b = a.not_()  # Equivale a b=Tristate(False)
    c = Tristate()  # Equivale a c=Tristate(None)
    print(a & b)  # a and b
    print(a | c)  # a or c
    print(a ^ c)  # a xor c
    print(a.imp(b))  # "a -> b" cioè "a implica b" o "IMP(a, b)"

    Tabelle di verità (dove 0 è False, 1 è True, ? è None):
    a|b|a and b|a or b|a xor b|not a|a->b
    -+-+-------+------+-------+-----+----
    0|0|   0   |   0  |   0   |  1  |  1
    0|1|   0   |   1  |   1   |  1  |  1
    0|?|   0   |   ?  |   ?   |  1  |  1
    1|0|   0   |   1  |   1   |  0  |  0
    1|1|   1   |   1  |   0   |  0  |  1
    1|?|   ?   |   1  |   ?   |  0  |  ?
    ?|0|   0   |   ?  |   ?   |  ?  |  ?
    ?|1|   ?   |   1  |   ?   |  ?  |  1
    ?|?|   ?   |   ?  |   ?   |  ?  |  ?
    
    Se trasformo la classe in intero con int(), avrò 1 per True, -1 per
    False e 0 per sconosciuto (None). Di conseguenza, andando a creare
    una nuova istanza, se passo un intero verrà interpretato così:
    Tristate(-1) == Tristate(False)  # o altro intero < 0
    Tristate( 0) == Tristate() == Tristate(None)
    Tristate( 1) == Tristate(True)   # o altro intero > 0
    
    esempi:
    a = Tristate(True)   # Equivale a a=Tristate(1)
    print(int(a))  # 1
    print(+a)      # 1
    print(-a)      # -1
    b = Tristate(False)  # Equivale a b=Tristate(-1)
    print(int(b))  # -1
    print(+b)      # -1
    print(-b)      # 1
    c = Tristate()       # Equivale a c=Tristate(0)
    print(int(c))  # 0
    print(+c)      # 0
    print(-c)      # 0
    """
    
    __slots__ = ['valore']  # Lista attributi permessi alle istanze
    
    def __init__(self, value=None):
        if not value is None:
            if type(value) is int:
                #-1 --> False (mentre in Python bool(-1)=True)
                # 0 --> None  (mentre in Python bool( 0)=False)
                # 1 --> True  (mentre in Python bool( 1)=True)
                if value < 0:
                    value = False
                elif value == 0:
                    value = None
                else:  #elif value > 0:
                    value = True
            else:
                value = bool(value)
        #if value is None or value == True or value == False:
        self.valore = value
    
    def isknown(self) -> bool:
        """
        Restituisce True se il valore è True o False, False se è
        sconosciuto (None)
        """
        return not self.valore is None
    
    def isunknown(self) -> bool:
        """
        Restituisce True se il valore è sconosciuto (None), False se è
        conosciuto (True o False)
        """
        return self.valore is None
    
    def istrue(self) -> bool:
        """
        Restituisce True se il valore è True, False altrimenti (False o
        None)
        """
        return not self.valore is None and self.valore
    
    def isfalse(self) -> bool:
        """
        Restituisce True se il valore è False, False altrimenti (True o
        None)
        """
        return not self.valore is None and not self.valore
    
    def not_(self):  # -> Tristate
        """
        Restituisce una nuova istanza Tristate, il cui valore è True se
        il valore è False, False se il valore è True, None se il valore
        è sconosciuto (None).
        :rtype: Tristate
        """
        if self.valore is None:
            return Tristate(self.valore)
        else:
            return Tristate(not self.valore)
    
    def imp(self, altro):  # -> Tristate
        """self->altro
        Funzione implica
        :rtype: Tristate
        """
        if self.isfalse():
            return Tristate(True)
        else:
            if not type(altro) is Tristate:
                altro = Tristate(altro)
            if self.istrue() or altro.istrue():
                return altro
            else:
                return Tristate()
    
    def __bool__(self) -> bool:
        """
        Restituisce True se il valore è True, False altrimenti.
        """
        return self.valore
    
    def __int__(self) -> int:
        """
        int(x) essendo x un'istanza di Tristate
        Restituisce -1 se il valore è False, 0 se il valore è None e
        1 se il valore è True.
        """
        out = 0
        if not self.valore is None:
            out = -1
            if self.valore:
                out = 1
        return out
    
    def __pos__(self) -> int:
        """+x essendo x un'istanza di Tristate"""
        return self.__int__()
    
    def __neg__(self) -> int:
        """-x essendo x un'istanza di Tristate"""
        return -self.__int__()
    
    def __str__(self) -> str:
        return str(self.valore)
    
    def __repr__(self):
        """
        Restituirà o un booleano o None
        """
        return self.valore
    
    def __and__(self, altro):  # -> Tristate  
        """x & altro essendo x un'istanza di Tristate
        :rtype: Tristate
        """
        if self.isfalse():
            return Tristate(False)
        else:
            if not type(altro) is Tristate:
                altro = Tristate(altro)
            if altro.isfalse():
                return Tristate(False)
            elif self.istrue() and altro.istrue():
                return Tristate(True)
            else:
                return Tristate()
    
    def __or__(self, altro):  # -> Tristate
        """x | altro essendo x un'istanza di Tristate
        :rtype: Tristate
        """
        if self.istrue():
            return Tristate(True)
        else:
            if not type(altro) is Tristate:
                altro = Tristate(altro)
            if altro.istrue():
                return Tristate(True)
            elif self.isfalse() and altro.isfalse():
                return Tristate(False)
            else:
                return Tristate()
    
    def __xor__(self, altro):  # -> Tristate
        """x ^ altro essendo x un'istanza di Tristate
        :rtype: Tristate
        """
        if self.isunknown():
            return Tristate()
        else:
            if not type(altro) is Tristate:
                altro = Tristate(altro)
            if altro.isunknown():
                return Tristate()
            elif self.isfalse():
                return altro
            else:
                return Tristate(altro.not_())
    
    def __eq__(self, altro) -> bool:
        """x == altro essendo x un'istanza di Tristate"""
        if not type(altro) is Tristate:
            altro = Tristate(altro)
        return self.valore == altro.valore
    
    def __ne__(self, altro) -> bool:
        """x != altro essendo x un'istanza di Tristate"""
        if not type(altro) is Tristate:
            altro = Tristate(altro)
        return self.valore != altro.valore


if __name__ == "__main__":
    vero = Tristate(True)
    falso = Tristate(False)
    boh = Tristate()
    s = [falso, vero, boh]
    for a in s:
        #print('not {} = {}'.format(a, a.not_()))
        for b in s:
            #print('{} xor {} = {}'.format(a, b, a ^ b))
            #print('{:<5s} and {:<5s} = {}'.format(str(a), str(b), a & b))
            #print('{:<5s} or {:<5s} = {}'.format(str(a), str(b), a | b))
            print('{:<5s} --> {:<5s} = {}'.format(str(a), str(b), a.imp(b)))
    #print(str(-vero))
