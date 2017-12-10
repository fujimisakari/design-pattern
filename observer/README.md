# Observerパターン

## パターンについて

状態が変化したときにオブジェクトへ通知します。  
あるオブジェクト（通知元）の状態変化を不特定多数のオブジェクト（通知先）に知らせたいときに利用します。  
監視対象オブジェクトを中継させることで、通知元オブジェクトは通知先オブジェクトのことを知らなくても定義できます。  

## パターン構造

![observer_pattern](https://gist.githubusercontent.com/fujimisakari/83be99e9c64405c446842a20f2438f36/raw/d7c5ce307356ff6cd2bca09268780a3543c5f2f3/observer.png)

**構成要素**  
Observer :　観測者のインタフェース。Subject から呼び出される update メソッドを定義する。  
ConcreteObserver :　Observerインタフェースを実装する具象クラス。update メソッドの中で自分の状態を変更する。  
Subject :　観測対象の抽象クラス。notifyObservers メソッドの中で登録している Observer に対して update を呼び出す。  
ConcreteSubject	:　Subjectクラスを継承する具象クラス。観測者の具体的なデータを保持する。  
