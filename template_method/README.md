# TemplateMethodパターン

## パターンについて

アルゴリズム実現するためのテンプレート作成するパターンになります。  
同じような処理が複数あるとき、基本操作(primitiveOperation)をサブクラスでオーバーライドすることで、  
全体を共通化しながら、バリエーションによる影響を局所的に抑えられます  

## パターン構造

![templatemethod_pattern](https://gist.githubusercontent.com/fujimisakari/83be99e9c64405c446842a20f2438f36/raw/d7c5ce307356ff6cd2bca09268780a3543c5f2f3/templatemethod.png)

**構成要素**  
AbstractClass :　templateMethodは基本操作(primitiveOperation)を利用しますが実装がサブクラスに任せます  
ConcreteClass :　抽象操作の実装します  
