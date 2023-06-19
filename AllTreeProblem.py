from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterator, TypeVar, Generic, Optional, Callable

from yogi import read, tokens

T = TypeVar('T')


@dataclass
class _Node(Generic[T]):
    """Internal node of a binary tree"""
    data: T
    left: Bintree[T]
    right: Bintree[T]


class Bintree(Generic[T]):
    _node: Optional[_Node[T]]

    def __init__(self, data: Optional[T] = None,
                 left: Optional[Bintree[T]] = None,
                 right: Optional[Bintree[T]] = None):
        if data is None:
            self._node = None
        else:
            if left is None:
                left = Bintree()
            if right is None:
                right = Bintree()
            self._node = _Node(data, left, right)

    @property
    def empty(self) -> bool:
        return self._node is None

    @property
    def data(self) -> T:
        assert self._node
        return self._node.data

    @data.setter
    def data(self, v: T) -> None:
        assert self._node
        self._node.data = v

    @property
    def left(self) -> Bintree[T]:
        assert self._node
        return self._node.left

    @left.setter
    def left(self, t: Bintree[T]) -> None:
        assert self._node
        self._node.left = t

    @property
    def right(self) -> Bintree[T]:
        assert self._node
        return self._node.right

    @right.setter
    def right(self, t: Bintree[T]) -> None:
        assert self._node
        self._node.right = t

    def size(self) -> int:
        return 0 if self.empty else 1 + self.left.size() + self.right.size()
    
    def max_width(self) -> int:
        if self.empty: return 0
        return max(self.width(i) for i in range(1, self.num_levels()+1))
    
    def width(self, lvl: int) -> int:
        if self.empty: return 0
        if lvl == 1: return 1
        return self.left.width(lvl-1) + self.right.width(lvl-1)


    def num_levels(self) -> int:
        if self.empty:
            return 0
        return 1 + max(self.left.num_levels(), self.right.num_levels())

    def levels(self) -> Iterator[T]:
        q: deque[Bintree[T]] = deque([self])
        while q:
            n = q.popleft()
            if not n.empty:
                q.append(n.left)
                q.append(n.right)
                yield n.data


    def preorder(self) -> Iterator[T]:
        if not self.empty:
            yield self.data
            yield from self.left.preorder()
            yield from self.right.preorder()

    def visit_preorder(self, f: Callable[[T], T]):
        if not self.empty:
            self.data = f(self.data)
            self.left.visit_preorder(f)
            self.right.visit_preorder(f)

    def print_preorder(self) -> None:
        print('\n'.join(str(value) for value in self.preorder()))


    def inorder(self) -> Iterator[T]:
        if not self.empty:
            yield from self.left.inorder()
            yield self.data
            yield from self.right.inorder()

    def visit_inorder(self, f: Callable[[T], T]):
        if not self.empty:
            self.left.visit_inorder(f)
            self.data = f(self.data)
            self.right.visit_inorder(f)

    def print_inorder(self) -> None:
        s = ' '.join(str(value) for value in self.inorder())
        if len(s)>0: print('ino: '+s)
        else: print('ino:')


    def postorder(self) -> Iterator[T]:
        if not self.empty:
            yield from self.left.postorder()
            yield from self.right.postorder()
            yield self.data

    def visit_postorder(self, f: Callable[[T], T]):
        if not self.empty:
            self.data = f(self.data)
            self.left.visit_postorder(f)
            self.right.visit_postorder(f)
    
    def print_postorder(self) -> None:
        s = ' '.join(str(value) for value in self.postorder())
        if len(s)>0: print('pos: '+s)
        else: print('pos:')

    
    def search_binTree(self, n: T) -> bool:
        if self.empty: return False
        if self.data == n: return True
        return self.left.search_binTree(n) if self.data > n else self.right.search_binTree(n)

    def insert_binTree(self, node: _Node[T]) -> None:
        if self.empty: self._node = node
        if self.data < node.data:
            self.right.insert_binTree(node)
        elif self.data > node.data:
            self.left.insert_binTree(node)


    def show(self, lvl):
        if self.empty: return
        self.right.show(lvl+1)
        print(self.data.rjust(10*lvl))
        self.left.show(lvl+1)



def read_bintree() -> Bintree:
    data = read(int)
    return Bintree() if data == -1 else Bintree(data, read_bintree(), read_bintree())

def main() -> None:
    tree: Bintree = read_bintree()
    tree.print_postorder()
    tree.print_inorder()

if __name__ == "__main__":
    main()
