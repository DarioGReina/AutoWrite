primerFrame = int(nuke.thisNode()['primerFrame'].value())-1
ultimoFrame = int(nuke.thisNode()['ultimoFrame'].value())
writeNode = nuke.toNode('Write_rgb')

scriptroot = nuke.script_directory()

shotPath = ''
i = 0
while i < len(scriptroot.split('/'))-1:
    shotPath += scriptroot.split('/')[i]+'/'
    i += 1

renderPath = shotPath + '30_RENDER/'


#### WriteExr INICIO
codename = scriptroot.split('/')[len(scriptroot.split('/'))-2]

scriptPath = nuke.root().knob('name').value()
scriptName = ((scriptPath.split('/'))[(len((scriptPath.split('/')))-1)]).split('.')[0]
vCliente = (scriptName.split('_')[5])[1]

writeExrPath = renderPath + codename + '_V0' + vCliente + '/' + '3840x2160/' + codename + '_comp_V0' + vCliente + '.####.exr'
#### WriteExr FIN

writeNode['file'].setValue(writeExrPath)		#Asigna el path correcto para cada pc


if nuke.thisNode()['rangoManual'].value() == False:
   nuke.execute(writeNode,primerFrame,ultimoFrame)
else:
   writeNode['Render'].execute()