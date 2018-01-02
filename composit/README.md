# Compositパターン

## パターンについて

階層構造を持つオブジェクトへアクセスしたいときに、  
親オブジェクトと子オブジェクトに同じインターフェースを定義することで、  
階層構造を意識せずにアクセスすることができる。  

## パターン構造

![composit_pattern](https://gist.githubusercontent.com/fujimisakari/83be99e9c64405c446842a20f2438f36/raw/d7c5ce307356ff6cd2bca09268780a3543c5f2f3/composit.png)

**構成要素**  
Component :　リーフノード,コンポジットノードの両方のインターフェースを定義します  
Leaf :　子要素(リーフノード)  
Composit :　子要素を持つコンポーネントの振舞いを定義し、子要素を格納する(コンポジットノード)  
Client :　Componetインタフェースを利用してコンポジション内のオブジェクトを操作する  
