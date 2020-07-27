scriptPath = nuke.root().knob('name').value()
scriptName = ((scriptPath.split('/'))[(len((scriptPath.split('/')))-1)]).split('.')[0]

cap = scriptName.split('_')[0]
sec = scriptName.split('_')[1]
plano = scriptName.split('_')[2]
dep = scriptName.split('_')[3]
op = scriptName.split('_')[4]
vCliente = (scriptName.split('_')[5])[1]
vOp = ((scriptName.split('_')[5])[2]) + ((scriptName.split('_')[5])[3])

nuke.thisNode()['cap'].setValue(cap)
nuke.thisNode()['sec'].setValue(sec)
nuke.thisNode()['plano'].setValue(plano)
nuke.thisNode()['dep'].setValue(dep)
nuke.thisNode()['op'].setValue(op)
nuke.thisNode()['vCliente'].setValue(vCliente)
nuke.thisNode()['vOp'].setValue(vOp)
nuke.thisNode()['scriptName'].setValue(scriptName)

pixAspect = nuke.thisNode()['pixAspect'].getValue()
pixAspRnd = float(int(pixAspect*100))/100

if pixAspect == 1:
   nuke.thisNode()['pixAspectTxt'].setValue('Square Pixel')
else:
   if pixAspect == 2:
      nuke.thisNode()['pixAspectTxt'].setValue('Anamorphic')
   else:
      nuke.thisNode()['pixAspectTxt'].setValue(str(pixAspRnd)+':1')