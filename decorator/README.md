# Decoratorパターン

## パターンについて

新しい振舞いを提供するために、オブジェクトをラップします。  
オブジェクト毎に機能を追加したいときや機能を動的に付け外ししたいとき、同じインターフェース  
を持つオブジェクトで被せるようにすることで、既存クラスに手を加えずに機能追加ができます。  

## パターン構造

![decorator_pattern](https://gist.githubusercontent.com/fujimisakari/83be99e9c64405c446842a20f2438f36/raw/d7c5ce307356ff6cd2bca09268780a3543c5f2f3/decorator.png)

**構成要素**  
Component :　拡張される機能を定義した抽象クラス(abstractかinterfaceを利用する)  
ConcreteComponent :　Componentクラスで定義した機能を基本実装する、装飾される具象クラス。  
Decorator :　Componentを継承して装飾される具象クラスと型の一致を実現するためクラス。振舞いを取得するために継承してるわけではない  
ConcreteDecoratorA, B :　具象クラスに機能の拡張(飾り付け)を行う具象クラス。  
