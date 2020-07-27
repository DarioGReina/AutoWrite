scriptPath = nuke.root().knob('name').value()
scriptName = ((scriptPath.split('/'))[(len((scriptPath.split('/')))-1)]).split('.')[0]

###    METADATA PATH START
#x=0
#metadataPath = ''
#while x < len(scriptPath.split('/'))-2:
#    metadataPath += scriptPath.split('/')[x]+'/'
#    print(metadataPath)
#    x += 1
#metadataPath += 'metadata.csv'
###    METADATA PATH END

#import csv
#meta = metadataPath
#with open(meta, 'r') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#        proyecto = row['PROYECTO']
#        descripcion = row['DESCRIPCION']
#        tarea = row['TAREA']

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
#nuke.thisNode()['proyecto'].setValue(proyecto)
#nuke.thisNode()['tarea'].setValue(tarea)
#nuke.toNode('notasRele')['label'].setValue(descripcion)

pixAspect = nuke.thisNode()['pixAspect'].getValue()
pixAspRnd = float(int(pixAspect*100))/100

if pixAspect == 1:
   nuke.thisNode()['pixAspectTxt'].setValue('Square Pixel')
else:
   if pixAspect == 2:
      nuke.thisNode()['pixAspectTxt'].setValue('Anamorphic')
   else:
      nuke.thisNode()['pixAspectTxt'].setValue(str(pixAspRnd)+':1')