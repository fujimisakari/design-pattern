# Strategyパターン

## パターンについて

Strategyパターンは交換可能な振舞いをカプセル化し、委譲を使って使用すべき振舞いを決定します。  
主要な処理を行っているコードの中で一部動的に振舞いを変更させたい場合に利用し、  
コードの中で動的に振舞い変更したい場合は、if文なので条件分岐しがちになりますが  
Strategyを利用することで主要な処理に対して影響を与えず、1つのステートメントで動的な振舞いを定義することができます。  

## パターン構造

![strategy_pattern](https://gist.githubusercontent.com/fujimisakari/83be99e9c64405c446842a20f2438f36/raw/d7c5ce307356ff6cd2bca09268780a3543c5f2f3/strategy.png)

**構成要素**  
Context :　インタフェース Strategy を利用するクラス。  
Strategy :　アルゴリズムに共通のインタフェース。Context オブジェクトはこのインタフェースを使用する。  
ConcreteStrategy :　インタフェース Strategy を実現する具象クラス。様々なアルゴリズムを実装する。  
