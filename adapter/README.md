# Adapterパターン

## パターンについて

オブジェクトをラップし、別のインタフェースを提供します。   

※ アダプタ、デコレータ、ファサードパターンの違い  
アダプタは、オブジェクトのインタフェースを変更するためにラップします。  
デコレータは、新しい振舞いや責務を追加するためにラップします  
ファサードは、簡素化のために一連オブジェクトを「ラップ」します  

## パターン構造

![adapter_pattern](https://gist.githubusercontent.com/fujimisakari/83be99e9c64405c446842a20f2438f36/raw/d7c5ce307356ff6cd2bca09268780a3543c5f2f3/adapter.png)

**構成要素**  
Client :　Tragetインタフェースを利用する処理  
Target :　変換時に実装したいインタフェース  
Adapter :　TargetクラスのインタフェースをAdapteeクラスの処理利用して実装します  
Adaptee	:　インタフェースの変換を行う元クラス  
