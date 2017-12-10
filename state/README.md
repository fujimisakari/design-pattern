# Stateパターン

## パターンについて

状態が変化が多数ある場合に条件分岐を使うことなく状態変化を実現できます  
状態毎のオブジェクトを作っておいて、状態を変えたいときは  
コンテキスト内の状態オブジェクトを変更するだけで振舞いを容易に変更できます  

## パターン構造

![state_pattern](https://gist.githubusercontent.com/fujimisakari/83be99e9c64405c446842a20f2438f36/raw/d7c5ce307356ff6cd2bca09268780a3543c5f2f3/state.png)

**構成要素**  
Context :　多数の内部状態を持つことができるクラス  
State :　すべての具象状態クラス用の共通インタフェース  
ConcreteState :　各ConcreteStateは、Contextからの要求に対する独自の振舞いを実装する  
