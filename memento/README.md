# Mementoパターン


## パターンについて

このパターンは、あるオブジェクトの任意の時点の状態を覚えておき(保存)、 後でその状態にオブジェクトを戻すための工夫を提供するパターンです。(カプセル化を破壊せずに、状態を元に戻せる)つまり、テキストエディタ等で実装されているような「アンドゥ」(操作をキャンセルして操作前の状態に戻す)機能を提供するためのパターンです。

注意すべきことは状態を元に戻すための必要最小限の情報(フィールド値)のみを保存すると言うことです。

参照先: http://www.itsenka.com/contents/development/designpattern/memento.html
