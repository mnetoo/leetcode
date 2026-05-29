class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # LISTA 1
        vet1 = []

        # enquanto tiver proximo
        while(l1 != None):
            # pegar o valor do nodo
            vet1.append(l1.val)
            # vai para o proximo nodo
            l1 = l1.next
                

        # LISTA 2
        vet2 = []

        # enquanto tiver proximo
        while(l2 != None):
            # pegar o valor do nodo
            vet2.append(l2.val)
            # vai para o proximo nodo
            l2 = l2.next
           

        numero = 0
        for i in range(len(vet1)):
            numero += vet1[i] * pow(10, i)    

        numero2 = 0
        for i in range(len(vet2)):
            numero2 += vet2[i] * pow(10, i)

        resultado = numero + numero2

        l3 = ListNode(resultado % 10)
        resultado = resultado // 10
        atual = l3
        while resultado > 0:
            atual.next = ListNode(resultado % 10)
            atual = atual.next
            resultado = resultado // 10     

        return l3