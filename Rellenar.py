scriptPath = nuke.root().knob('name').value()
scriptName = scriptPath.split('/')[-1].split('.')[0]

[cap, sec, plano, dep, op, version] = scriptName.split('_')
vCliente = version[1]
vCliente = scriptNameSections[5][1]
vOp = version[2:]

nukeNode = nuke.thisNode()
nukeNode['cap'].setValue(cap)
nukeNode['sec'].setValue(sec)
nukeNode['plano'].setValue(plano)
nukeNode['dep'].setValue(dep)
nukeNode['op'].setValue(op)
nukeNode['vCliente'].setValue(vCliente)
nukeNode['vOp'].setValue(vOp)
nukeNode['scriptName'].setValue(scriptName)

pixAspect = nukeNode['pixAspect'].getValue()
pixAspRnd = round(pixAspect, 2)

if pixAspect == 1:
  nukeNode['pixAspectTxt'].setValue('Square Pixel')
elif pixAspect == 2:
  nukeNode['pixAspectTxt'].setValue('Anamorphic')
else:
  nukeNode['pixAspectTxt'].setValue(str(pixAspRnd) + ':1')