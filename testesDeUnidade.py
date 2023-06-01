import unittest
import ex5
from ex5 import *

class TestNode(unittest.TestCase):
    def testCriarNode(self):
        novoNode = Node(10)
        self.assertEqual(novoNode.valor, 10)

    def testNodeSemProximo(self):
        novoNode = Node(10)
        self.assertIsNone(novoNode.proximo)

    def testAdicionarProximo(self):
        novoNode = Node(10)
        novoNode2 = Node(15)
        novoNode.setProximo(novoNode2)
        self.assertEqual(novoNode.proximo.valor, 15)

class TestTree(unittest.TestCase):
    def testArvoreSemRaiz(self):
        arvore = Tree()
        self.assertIsNone(arvore.raiz)

    def testArvoreComRaiz(self):
        arvore = Tree()
        novoNode = Node(10)
        arvore.setRaiz(novoNode)
        self.assertEqual(arvore.raiz.valor, 10)

    def testArvoreJaTemRaiz(self):
        arvore = Tree()
        novoNode = Node(10)
        arvore.setRaiz(novoNode)
        self.assertEqual(arvore.setRaiz(novoNode), "Raiz já definida")
    
    def testArvoreComDuasCamadas(self):
        arvore = Tree()
        node1 = Node(10)
        node2 = Node(20)
        arvore.setRaiz(node1)
        arvore.raiz.setProximo(node2)
        self.assertEqual(arvore.raiz.proximo.valor, 20)

if __name__ == '__main__':
    unittest.main()