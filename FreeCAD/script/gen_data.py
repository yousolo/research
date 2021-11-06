# FreeCADファイルの読み込み
import FreeCAD
FreeCAD.open(u"C:\report\FreeCAD\doc\pit.FCStd")
# parameters = [dx, dy, dz, r, cx, cy, s1, s2, m]

# Sketchから変更可能なparameters
# 金属板のx方向の長さ
# 金属板のy方向の長さ
# 穴の半径
# 穴のx座標
# 穴のy座標

# change dx
index = {'dx':7, 'dy':8, 'r':9, 'cx':10, 'cy':11}
dx = 100

idx = index['dx']
quantity = str(dx) + 'mm'

App.getDocument('pit').getObject('Sketch').setDatum(idx,App.Units.Quantity(quantity))
App.ActiveDocument.recompute()


# Padから変更可能なparameter
# 金属板のz方向の長さ
# change dz
dz = 10
App.getDocument('pit').getObject('Pad').Length = dz
App.getDocument('pit').recompute()

# Default
# App.getDocument('pit').getObject('Pad').Length2 = 100.000000
# App.getDocument('pit').getObject('Sketch').Visibility = False
# App.getDocument('pit').getObject('Pad').UseCustomVector = 0
# App.getDocument('pit').getObject('Pad').Direction = (1, 1, 1)
# App.getDocument('pit').getObject('Pad').Type = 0
# App.getDocument('pit').getObject('Pad').UpToFace = None
# App.getDocument('pit').getObject('Pad').Reversed = 0
# App.getDocument('pit').getObject('Pad').Midplane = 0
# App.getDocument('pit').getObject('Pad').Offset = 0
# App.getDocument('pit').recompute()

# 荷重を変更したい！
# s1 = ConstraintForce
# s2 = ConstraintForce001
s1 = 5
s2 = 3
# 荷重s1：Face3
App.ActiveDocument.ConstraintForce.Force = s1
App.ActiveDocument.ConstraintForce.References = [(App.ActiveDocument.Pad, "Face3")]

# 荷重s2:Face2
App.ActiveDocument.ConstraintForce001.Force = s2
App.ActiveDocument.ConstraintForce.References = [(App.ActiveDocument.Pad, "Face2")]
App.ActiveDocument.recompute()

# Default
# 分からなければ以下の記述も足しておけばよさそう
# Scaleが何をしてるか知りたい

# App.ActiveDocument.ConstraintForce.Direction = None
# App.ActiveDocument.ConstraintForce.Reversed = False
# App.ActiveDocument.ConstraintForce.Scale = 6
# App.ActiveDocument.ConstraintForce.References = [(App.ActiveDocument.Pad,"Face2")]
# App.ActiveDocument.recompute()

# メッシュの切り方
# メッシュのサイズ
# 六面体メッシュをどう切るか

# 流れを整理
# データ生成をgen_data.py
# メッシュはnetgenで切ってしまう
# FrontISTRに渡す
# 計算結果を取得。一旦は最大フォンミーゼス応力を引っ張ってくる。
