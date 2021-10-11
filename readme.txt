AAC(Aggregate Array Computation)の実験で用いた漸増化システムです～

incrementalization.pyとdevide_index_module.pyはセットで使います。
incrementalization.pyに入力を記述し、devide_index_module.pyをモジュールとして使うことで漸増化が行われるという流れです。
incrementalization.pyからdevide_index_module.pyを呼び出せるようにして実行してください。
特に手を加えずにincrementalization.pyを実行すると論文中のプログラムBの例が実行されます。


他の入力を試すだけであればincrementalization.pyのみを操作すれば良いです。
なお、incrementalization.pyにあるproblem=0～10は正しく動くと思われます。

独自の入力を試す際はincrementalization.pyのコメントを参考にしてください。
漸増化した出力コードの実行結果ansと通常実行の結果inc_ansを全て比較し、ans==inc_ansなら"漸増化コードと通常実行の結果一致： True"と表示されます。